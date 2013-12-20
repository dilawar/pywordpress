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
    savePath = titleToFileName(title)
    print("|- Adding id to new post and saving it to : \n {0}".format(savePath))
    with open(savePath, "w") as ff :
        ff.write(txt)
    sendPostToWordpress(post, wp, txt)
    print("== You should now delete : {0}.".format(postName))
    return 0

def fetchWpPosts(wp, postsToFetch):
    """
    Fetch given posts from wordpress.
    """
    posts = wp.call(GetPosts( {'number': 200, 'offset': 0}))
    pages = wp.call(GetPosts({'post_type' : 'page'}))
    if  postsToFetch == "all" :
        fetchPosts(posts, "post")
        fetchPosts(pages, "page")
    elif len(postsToFetch) > 2 :
        # search for a post with similar titles.
        matchedPosts = list()
        for post in posts :
            title = post.title 
            match = difflib.SequenceMatcher(None, title, postsToFetch).ratio()
            if match > 0.65 :
                matchedPosts.append(post)
        fetchPosts(matchedPosts, "post")
        # Why not pages.
        matchedPages = list()
        for page in pages :
            title = page.title 
            match = difflib.SequenceMatcher(None, title, postsToFetch).ratio()
            if match > 0.65 :
                matchedPages.append(post)
        fetchPosts(matchedPages, "page")
  

def formatWithNoChangeOnTag(txt, tag) :
  ''' Notice :
  +QUQ+ should be replace by \n after using this function last time.
  '''
  newText = ""
  bTag = False 
  eTag = True
  beginTag = re.compile("[\<\[]\s*"+tag+"\s*(\w+\s*=\s*[\"\w\']+\s*)?[\>\]]",
      re.IGNORECASE)
  endTag = re.compile("[\<\[]\s*\/"+tag+"\s*[\>\]]", re.IGNORECASE)
  for line in txt.split("\n") :
    if len(line.strip()) == 0 : continue 
    if beginTag.search(line) and endTag.search(line) : newText += line
    else : 
      if beginTag.search(line) :
        newText += "\n"
        bTag = True
        eTag = False
      if endTag.search(line) :
        eTag = True
        bTag = False
    #check 
    if bTag is True and eTag is False:
      newText += (line+"+QUQ+")
    else : # format it 
      newText += (line.strip()+"\n")
  return newText

def formatContent(content) :
  content = formatWithNoChangeOnTag(content, "sourcecode")
  content = formatWithNoChangeOnTag(content, "pre")
  content = re.sub("\n+", " ", content)
  content = content.replace("+QUQ+", "\n")
  return content

def getTitle(txt, format='native'):
    if format == "markdown":
        print("Support markdown")
        sys.exit(0)
  
    titleRegex = re.compile("\<title\>\s*(?P<title>[\w\W\s]+)\s*\</title\>",
          re.IGNORECASE | re.DOTALL)
    m = titleRegex.search(txt)
    if m :
      title = m.groupdict()['title']
    else :
      print("[W] Empty title!")
      title = ""
    return title
  
def titleToFileName(title) :
    global blogDir
    fileName = title.replace(" ","_")+".blog"
    fileName = fileName.replace("/", "_")
    fileName = os.path.abspath(blogDir+"/"+fileName)
    return fileName
  

def sendPostToWordpress(post, wp, txt) :
    # Check if there is no id.
    idregex = re.compile('\<id\>\s*(?P<id>\d+)\s*\</id\>', re.IGNORECASE | re.DOTALL)
    m = idregex.search(txt) 
    if not m :
        print("This looks like a new post, use --post option")
        return 
    id = m.groupdict()['id']
    post.id = id
    title = getTitle(txt)
    post.title = title
    
    print("[I] Sending post : {0} : {1}.".format(id, title))
  
    # content 
    contentRegex = re.compile("\<content\>(?P<content>.+)\<\/content\>"
        , re.IGNORECASE | re.DOTALL
        )
    m = contentRegex.search(txt)
    if m :
        content = m.groupdict()['content']
        if len(content.strip()) == 0 :
            print("[E] : No content in file.")
            return 
        content = formatContent(content)
    else :
        print("[W] Post with empty content.")
        content = ""
    post.content = content
    
    # status 
    statusRegex = re.compile("\<status\>\s*(?P<status>\w+)\s*\</status\>"
        , re.IGNORECASE | re.DOTALL)
    m = statusRegex.search(txt)
    if m :
        status = m.groupdict()['status']
        post.post_status = status 
    else :
        print("[W] Post with uncertain status. Default to publish")
        post.post_status = "publish"
    
    termsAndCats = dict()
    
    # tags 
    tagRegex = re.compile("\<post_tag\s+id\=\"(?P<id>\d*)\"\>\s*"+\
        "(?P<tag>[\s\w]+)\s*\</post_tag\>"
        , re.IGNORECASE | re.DOTALL
        )
    ms = tagRegex.findall(txt)
    tags = list()
    for m in ms :
        id, name = m
        tags.append(name)
    termsAndCats['post_tag'] = tags 
  
    # categories
    catRegex = re.compile("\<category\s+id\=\"(?P<id>\d*)\"\>\s*"+\
        "(?P<cat>[\s\w]+)\s*\</category\>"
        , re.IGNORECASE | re.DOTALL
        )
    mm = catRegex.findall(txt)
    cats = list()
    for m in mm :
        id, cat = m
        cats.append(cat)
    termsAndCats['category'] = cats
  
    post.terms_names = termsAndCats 
    wp.call(EditPost(post.id, post))
    return


def fetchPosts(posts, postType, fmt="native") :
  """ Fetch all posts in list posts with postType
  """
  global blogDir
  for post in posts :
    title = post.title.encode('utf-8')
    terms = post.terms
    print("[I] : Downloading : {0}".format(title))
    content = post.content 
    content = formatter.formatContent(content)
    fileName = titleToFileName(title)
    f = codecs.open(fileName, "w", encoding="utf-8", errors="ignore")
    
    if fmt == "native":
        f.write("<type>"+postType+"</type>\n")
        f.write("<status>"+post.post_status+"</status>\n")
        f.write("<id>"+post.id+"</id>\n")
        f.write("<title>")
        f.write(title)
        f.write("</title>\n\n")
        f.write("<content>\n")
        f.write(content)
        f.write("\n</content>\n")
        for t in terms :
          f.write("\n<"+t.taxonomy.upper()+" id=\""+t.taxonomy_id+"\">"\
              +t.name+"</"+t.taxonomy.upper()+">\n")
    elif fmt == "markdown":
        content = content.replace("<br/>", "\n\n")
        content = content.replace("<br />", "\n\n")
        content = content.replace("<br>", "\n\n")
        content = content.replace("<pre>", "\n\n<pre>") 
        content = content.replace("</pre>", "</pre>\n\n") 
        content = content.replace("<p>", "\n\n<p>")
        content = content.replace("[/sourcecode", "\n\n[/sourcecode")
        f.write("~~~\n")
        f.write("title: {0} \n".format(title))
        f.write("status: {0} \n".format(post.post_status))
        f.write("type: {0} \n".format(postType))
        f.write("id: {0} \n".format(post.id))
        f.write("category: {0}".format(post.terms))
        f.write("~~~\n\n")
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
    if 'http::/' in p :
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
        sendPostToWordpress(post, wp, txt) 
    
    elif args.post :
        newPostToWordpress(wp, args.post)
    # Fetch blogs from wordpress.
    elif args.fetch :
    # Get all posts 
        fetchWpPosts(wp, args.fetch)
    else : # get recent posts 
        posts = wp.call(GetPosts( {'post_status': 'publish'}))
        fetchPosts(posts, "post")

