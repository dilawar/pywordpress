#!/usr/bin/env python

import argparse
import os 

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, GetPost, NewPost, EditPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import media, posts 

import argparse
import os
import sys
import re
import errno
import difflib 
import subprocess
import logging
import pyblog.formatter as formatter
from pyblog.colored_print import printDebug

logging.basicConfig(filname=os.environ['HOME']+'.wordpress.log')


deliminator = '---'

class Wordpress:
    ''' Wordpress classs'''

    def __init__(self, args):
        self.blogDir = formatter.titleToBlogDir(args.blogName)
        self.blog = args.blogUrl
        self.wp = None
        # Create blog directory if not exists.
        try :
            if len(self.blogDir.strip()) > 0:
                os.makedirs(self.blogDir)
        except OSError as exception :
            if exception.errno != errno.EEXIST :
                raise 
        self.run(args)
        
    
    def newPostToWordpress(self, postName):
        printDebug("STEP", "You are going to create a new post!")
        post = WordPressPost()
        post.id = self.wp.call(NewPost(post))
        ## get the text of new post
        fileName = postName
        fmt, txt = formatter.readInputFile(fileName)
        self.format = fmt
        try:
            self.updatePost(post, txt)
        except Exception as e:
            printDebug("WARN", "Failed to send post to wordpress")
            printDebug("DEBUG", "Error was {0}".format(e))
            return 

        printDebug("INFO", "Post sent successfully")
        # Now download the sent post and save it.
        postNew = self.wp.call(GetPost(post.id))
        self.writePosts([postNew])
        printDebug("ADVICE", "You should now delete : {0}.".format(postName))
        return 0
    
    def fetchWpPosts(self, postsToFetch):
        """
        Fetch given posts from wordpress.
        """
        posts = self.wp.call(GetPosts( {'number': 2000, 'offset': 0}))
        pages = self.wp.call(GetPosts({'post_type' : 'page'}))
        if  postsToFetch == "all" :
            self.writePosts(posts + pages)
        elif len(postsToFetch) > 2 :
            # search for a post with similar titles.
            matchedPosts = list()
            for post in posts :
                title = post.title 
                match = difflib.SequenceMatcher(None, title, postsToFetch).ratio()
                if match > 0.60 :
                    matchedPosts.append(post)
            self.writePosts(matchedPosts)
            # Why not pages.
            matchedPages = list()
            for page in pages :
                title = page.title 
                match = difflib.SequenceMatcher(None, title, postsToFetch).ratio()
                if match > 0.60 :
                    matchedPages.append(post)
            self.writePosts(matchedPages)
            
    def getTitle(self, txt):
        titleRegex = re.compile("title\s*:\*(?P<title>.+)", re.IGNORECASE)
        m = titleRegex.search(txt)
        if m :
            title = m.groupdict()['title']
        else :
            print("[W] Empty title!")
            title = ""
        return title.strip()

    def appendMetadataToPost(self, mdict, post):
        """
        Append metadata to post.
        """
        try:
            id = post.id 
        except AttributeError:
            id = mdict.get('id', None)
            if not id:
                printDebug("ERROR"
                        , "This looks like a new post, use --post option"
                        )
                sys.exit(0)
        post.id = id
        title = mdict['title']
        post.title = title.strip()
    
        self.attachType(mdict, post)
        self.attachStatus(mdict, post)
        
        termsAndCats = dict()
        termsAndCats = self.attachTags(mdict, post, termsAndCats)
        termsAndCats = self.attachCategories(mdict, post, termsAndCats)
        post.terms_names = termsAndCats 

        return post
    
    def attachType(self, mdict, post):
        # type wordpress.
        if not mdict.get('type'):
            print("Warnng. This post has no type. Assuming post")
            post.post_type = 'post'
        else:
            post.post_type = mdict.get('type')
    
    def attachStatus(self, mdict, post):
        # status 
        if mdict.get('status') :
            status = mdict['status']
            post.post_status = status.strip()
        else :
            print("[W] Post with uncertain status. Default to publish")
            post.post_status = "publish"
    
    def attachTags(self, mdict, post, termsAndCats):
        # tags 
        tagList = mdict['tags'].translate(None, '[]').split(', ')
        termsAndCats['post_tag'] = tagList
        return termsAndCats
    
    def attachCategories(self, mdict, post, termsAndCats):
        # categories
        catList = mdict.get('categories')
        if catList:
            catList = catList.translate(None, '][').split(', ')
            termsAndCats['category'] = catList
        return termsAndCats
    
    def updatePost(self, post, txt) :
        # Check if there is no id.

        mdict = formatter.metadataDict(txt)
        content = formatter.getContent(txt)
        post = self.appendMetadataToPost(mdict, post)

        printDebug("STEP", "Updating post .. ", post.title)
        assert post.post_type
        # content 
        if content :
            if len(content.strip()) == 0 :
                print("[E] : No content in file.")
                return 
        else :
            printDebug("WARN", "Post with empty content.")
            content = ""
    
        if self.format == "html":
            content = formatter.htmlToHtml(content)
        elif self.format == "markdown":
            content = formatter.markdownToHtml(content)
            # Fix the math class 
            pat = re.compile(r'\<span\s+class\=\"math\"\>\\\((.+?)\\\)\<\/span\>'
                    , re.DOTALL)
            for m in pat.findall(content):
                printDebug("INFO", "Latex expression: ", m) 
            content = pat.sub(r'$latex \1$', content)
                
            post.content = content.encode('utf-8')
        else:
            post.content = content.encode('utf-8')

        #logFile = os.path.join(self.blogDir, "sent_html") 
        #printDebug("DEBUG", "Logging content into %s" % logFile)
        #with open(logFile, "w") as f:
            #f.write(post.content.encode('utf-8'))

        printDebug("STEP"
                , "Sending post : {0} : {1}.".format(post.id, post.title)
                )
        try:
            self.wp.call(EditPost(post.id, post))
        except Exception as e:
            printDebug("DEBUG", "I was trying to update but failed")
            printDebug("INFO", "Error was : {0}".format(e))
            printDebug("DEBUG", "Content of post was written to log.txt file")
            with open("log.txt", "w") as f:
                f.write(post.content)
            sys.exit(0)
    
    def writeContent(self, fH, content, format):
        """Write content to file.
        """
        if format == "html":
            logging.info("Writing html content")
            content = formatter.htmlToHtml(content) 
        elif format in ["markdown", "md"]:
            logging.info("Writing markdown format")
            content = formatter.htmlToMarkdown(content)
        fH.write(content.encode('utf-8'))
    
    
    def writePosts(self, posts, format="markdown"):
        """ Fetch all posts in list posts.
        """
        [self.writePost(post, format) for post in posts]

    def writePost(self, post, format):
        """
        Fetch a single post and write it to file.
        """
        assert int(post.id.strip()) > 0, "Post must have an id"

        title = post.title.encode('utf-8')
        terms = post.terms
        logging.debug("Downloading : {0}".format(title))
        printDebug("INFO", "Downloading {0}".format(post.post_type)
                , title
                )

        content = post.content.encode('utf-8')
        postDir = formatter.titleToFilePath(title, self.blogDir)

        # Create directory for this filename in blogDir.
        if not os.path.isdir(postDir):
            os.makedirs(postDir)

        # Good now for this post, we have directory. Download its content in
        # content.md file.
        fileName = os.path.join(postDir, 'content.md')
        fileHtml2 = os.path.join(postDir, 'content.html')

        with open(fileHtml2, "w") as ff:
            with open(fileName, "w") as f:
                f.write("{}\n".format(deliminator))
                f.write("title: ")
                f.write(title)
                f.write("\ncomments: true")
                f.write("\ntype: " + post.post_type)
                f.write("\nlayout: " + post.post_type)
                f.write("\nstatus: " + post.post_status)
                f.write("\nid: " + post.id)
                ff.write("{}\n".format(deliminator))
                ff.write("title: ")
                ff.write(title)
                ff.write("\ntype: " + post.post_type)
                ff.write("\nlayout: " + post.post_type)
                ff.write("\nstatus: " + post.post_status)
                ff.write("\nid: " + post.id)
                cats = []
                tags = []
                for t in terms :
                    tname = t.name.encode('utf-8')
                    if t.taxonomy == 'post_tag':
                        tags.append(tname)
                    elif t.taxonomy == 'category':
                        cats.append(tname)
                    else:
                        cats.append(tname)
                if tags:
                    tags = filter(None, [t for t in tags])
                    tagLine = 'tags: [{}]'.format(', '.join(tags)) 
                    f.write('\n{}'.format(tagLine)) 
                    ff.write('\n{0}'.format(tagLine)) 
                if cats:
                    cats = filter(None, [c.encode('utf-8') for c in cats])
                    f.write('\ncategories: [{0}]'.format(', '.join(cats)))
                    ff.write('\ncategories: [{0}]'.format(', '.join(cats)))
                f.write('\n')
                ff.write('\n')
                f.write("{}\n\n".format(deliminator))
                ff.write("{}\n\n".format(deliminator))

                # TODO: Get links from the post
                # Write content to file.
                self.writeContent(f, content, format)
                self.writeContent(ff, content, "html")
    
    def run(self, args):
        p = args.proxy
        if p is None:
            p = os.environ.get('http_proxy')
            if p is not None:
                printDebug("DEBUG", "Using http_proxy evvironment variable")
                if 'http://' in p :
                    p = p.replace('http://', '')
            else:
                printDebug("DEBUG", "Not using proxy")
                self.wp = Client(self.blog, args.user, args.password)
        else:
            self.wp = Client(self.blog, args.user, args.password, proxy=p)

        # Send a file to wordpress.
        if args.update :
            fileName = args.update
            if not os.path.exists(fileName):
                raise IOError, "File %s does not exists" % fileName
            fmt, txt = formatter.readInputFile(fileName)
            self.format = fmt
            post = WordPressPost()
            assert post is not None
            self.updatePost(post, txt) 

        elif args.new :
            self.newPostToWordpress(args.new)

        # Fetch blogs from wordpress.
        elif args.fetch :
            # Get all posts 
            self.fetchWpPosts(args.fetch)

        else : # get recent posts 
            printDebug("STEP", "Getting recent posts")
            posts = self.wp.call(GetPosts( {'post_status': 'publish'}))
            self.writePosts(posts)
