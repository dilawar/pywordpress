'''
Created on Apr 17, 2012
Originall written by : Vlad Gorloff

Modified by Dilawar for personal use.
'''

import sys
if sys.version_info < (3, 0) :
  from ConfigParser import RawConfigParser
else :
  from configparser import RawConfigParser 

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, EditPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import media, posts 

import formatter as formatter
import argparse
import os
import re
import lxml.html as lh
import codecs
import errno
import difflib 

blogDir = "./blogs"

def newPostToWordpress(wp, postName):
    print("[INFO] You are going to create a new post ...")
    post = WordPressPost()
    post.id = wp.call(NewPost(post))
    # get the text of new post
    fileName = postName
    with open(fileName, "r") as f :
        txt = f.read()
    
    txt = "<id>"+post.id+"</id>\n" + txt
    title = getTitle(txt)
    savePath = titleToBlogDir(title)+'/content.md'
    with open(savePath, "w") as ff:
        ff.write(txt)
    updatePost(post, wp, txt)
    print("== You should now delete : {0}.".format(postName))
    return 0

def fetchWpPosts(wp, postsToFetch):
    """
    Fetch given posts from wordpress.
    """
    posts = wp.call(GetPosts( {'number': 200, 'offset': 0}))
    pages = wp.call(GetPosts({'post_type' : 'page'}))
    if  postsToFetch == "all" :
        fetchPosts(posts, "post", wp)
        fetchPosts(pages, "page", wp)
    elif len(postsToFetch) > 2 :
        # search for a post with similar titles.
        matchedPosts = list()
        for post in posts :
            title = post.title 
            match = difflib.SequenceMatcher(None, title, postsToFetch).ratio()
            if match > 0.65 :
                matchedPosts.append(post)
        fetchPosts(matchedPosts, "post", wp)
        # Why not pages.
        matchedPages = list()
        for page in pages :
            title = page.title 
            match = difflib.SequenceMatcher(None, title, postsToFetch).ratio()
            if match > 0.65 :
                matchedPages.append(post)
        fetchPosts(matchedPages, "page", wp)
  

def getTitle(txt):
    titleRegex = re.compile("title:(?P<title>.+)", re.IGNORECASE)
    m = titleRegex.search(txt)
    if m :
        title = m.groupdict()['title']
    else :
        print("[W] Empty title!")
        title = ""
        
    return title.strip()
  
def titleToBlogDir(title):
    global blogDir
    fileName = title.replace(" ","_").replace(':', '-').replace('(', '')
    fileName = fileName.replace("/", "_").replace(')', '')
    fileName = os.path.abspath(os.path.join(blogDir, fileName))
    return fileName
  
def appendMetadataToPost(metadata, post):
    """
    Append metadata to post.
    """
    idregex = re.compile(r'id:(?P<id>.+)', re.IGNORECASE)
    m = idregex.search(metadata) 
    if not m :
        print("This looks like a new post, use --post option")
        return 
    id = m.group('id').strip()
    post.id = id
    title = getTitle(metadata)
    post.title = title

    # status 
    statusRegex = re.compile("status:(?P<status>.+)", re.IGNORECASE) 
    m = statusRegex.search(metadata)
    if m :
        status = m.groupdict()['status']
        post.post_status = status 
    else :
        print("[W] Post with uncertain status. Default to publish")
        post.post_status = "publish"
    
    termsAndCats = dict()

    # tags 
    tagRegex = re.compile("tag:(?P<name>.+)", re.IGNORECASE)
    ms = tagRegex.findall(metadata)
    tags = list()
    for m in ms :
        name = m
        tags.append(name)
    termsAndCats['post_tag'] = tags 
  
    # categories
    catRegex = re.compile("category:(?P<cat>.+)", re.DOTALL)
    mm = catRegex.findall(metadata)
    cats = list()
    for m in mm :
        cat = m
        cats.append(cat)
    termsAndCats['category'] = cats
    post.terms_names = termsAndCats 
    return post

def updatePost(post, wp, txt) :
    # Check if there is no id.
    pat = re.compile(r'~~~(~*)(?P<metadata>[^~.]+)~~~(~*)', re.DOTALL)
    metadata = pat.search(txt).group('metadata')
    content = re.sub(pat, "", txt)
    assert len(metadata) > 0
    
    post = appendMetadataToPost(metadata, post)
  
    # content 
    if content :
        if len(content.strip()) == 0 :
            print("[E] : No content in file.")
            return 
    else :
        print("[W] : Post with empty content.")
        content = ""

    content = formatter.contentToHTML(content)
    post.content = content
    print("[I] Sending post : {0} : {1}.".format(post.id, post.title))
    wp.call(EditPost(post.id, post))
    return

def fetchPosts(posts, postType, wp):
    """ Fetch all posts in list posts with postType
    """
    global blogDir
    pat = re.compile(r'\<img(?P<src>[^>]+)>', re.DOTALL)
    for post in posts :
        title = post.title.encode('utf-8')
        terms = post.terms
        print("[I] : Downloading : {0}".format(title))
        content = post.content 
        content = formatter.formatContent(content)
        fileName = titleToBlogDir(title)
        # Create directory for this filename in blogDir.
        postDir = os.path.join(blogDir, fileName)
        if not os.path.isdir(postDir):
            os.makedirs(postDir)

        # Good now for this post, we have directory. Download its content in
        # content.md file.
        fileName = os.path.join(postDir, 'content.md')
        f = codecs.open(fileName, "w", encoding="utf-8", errors="ignore")
        f.write("".join("~" for x in range(10))+'\n')
        f.write("title: ")
        f.write(title)
        f.write("\ntype: "+postType)
        f.write("\nstatus: "+post.post_status)
        f.write("\nid: "+post.id)
        cats = []
        tags = []
        for t in terms :
            if t.taxonomy == 'post_tag':
                tags.append(t.name)
            elif t.taxonomy == 'category':
                cats.append(t.name)
            else:
                raise RuntimeError, "Unknown taxonomy {0} found".format(t.name)
        if tags:
            for t in tags:
                f.write('\ntag: {0}'.format(t)) 
        if cats:
            for c in cats:
                f.write('\ncategory: {0}'.format(c))
        f.write('\n')
        f.write("".join("~" for x in range(10))+'\n')

        # TODO: Get links from the post
        srcs = pat.findall(content)
        i = 0
        for src in srcs:
            i += 1

        f.write(content)
        f.close()

def run(args):
    # Getting command line arguments   
    global blogDir 
    configFilePath = args.config
    cfg = RawConfigParser()
    with open(configFilePath, "r") as configFile :
        cfg.readfp(configFile)
    blogId = "blog"+str(args.blog)
    blog = cfg.get(blogId, 'url')
    blog = blog.replace("www.", "")
    blog = blog.replace("http://", "")
    blogDir = blog.replace(".", "DOT")
    blog = blog.replace("/xmlrpc.php", "")
    blog = "http://"+blog+"/xmlrpc.php"
    user = cfg.get(blogId,'username')
    password = cfg.get(blogId, 'password')
  
    try :
        os.makedirs(blogDir)
    except OSError as exception :
        if exception.errno != errno.EEXIST :
            raise 
    
    ## Now cleate a client 
    p = os.environ['http_proxy']
    if 'http://' in p :
        p = p.replace('http://', '')

    wp = Client(blog, user, password, proxy=p)
    
    # Send a file to wordpress.
    if args.update :
        fileName = args.update
        if not os.path.exists(fileName) :
            print("File {0} doesn't exists.. Existing...".format(fileName))
            return 
        # Open the file.
        with open(fileName, "r") as f :
            txt = f.read()
        post = WordPressPost()
        updatePost(post, wp, txt) 
    elif args.post :
        newPostToWordpress(wp, args.post)
    # Fetch blogs from wordpress.
    elif args.fetch :
    # Get all posts 
        fetchWpPosts(wp, args.fetch)
    else : # get recent posts 
        posts = wp.call(GetPosts( {'post_status': 'publish'}))
        fetchPosts(posts, "post", wp)
        

