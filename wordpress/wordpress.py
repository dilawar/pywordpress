#!/usr/bin/env python

import argparse
import os 

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, GetPost, NewPost, EditPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import media, posts 

from blogger.BloggerUpdater import BloggerUpdater

import argparse
import os
import re
import errno
import difflib 
import subprocess
import logging
import pyblog.formatter as formatter
from pyblog.colored_print import printDebug

logging.basicConfig(filname='.wordpress.log')

class Wordpress:
    def __init__(self, args):
        self.blogDir = args.blogName
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
        with open(fileName, "r") as f :
            txt = f.read()
        try:
            self.updatePost(post, txt) 
        except Exception as e:
            logging.warning("Failed to send post to wordpress")
            logging.debug("Error was {0}".format(e))

        logging.info('Post is sent successfully')
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
        posts = self.wp.call(GetPosts( {'number': 200, 'offset': 0}))
        pages = self.wp.call(GetPosts({'post_type' : 'page'}))
        if  postsToFetch == "all" :
            self.writePosts(posts + pages)
        elif len(postsToFetch) > 2 :
            # search for a post with similar titles.
            matchedPosts = list()
            for post in posts :
                title = post.title 
                match = difflib.SequenceMatcher(None, title, postsToFetch).ratio()
                if match > 0.65 :
                    matchedPosts.append(post)
            self.writePosts(matchedPosts)
            # Why not pages.
            matchedPages = list()
            for page in pages :
                title = page.title 
                match = difflib.SequenceMatcher(None, title, postsToFetch).ratio()
                if match > 0.65 :
                    matchedPages.append(post)
            self.writePosts(matchedPages)
            
    def getTitle(self, txt):
        titleRegex = re.compile("title:(?P<title>.+)", re.IGNORECASE)
        m = titleRegex.search(txt)
        if m :
            title = m.groupdict()['title']
        else :
            print("[W] Empty title!")
            title = ""
        return title.strip()

    def appendMetadataToPost(self, metadata, post):
        """
        Append metadata to post.
        """
        try:
            id = post.id 
        except AttributeError:
            idregex = re.compile(r'id:(?P<id>.+)', re.IGNORECASE)
            m = idregex.search(metadata) 
            if not m :
                raise UserWarning, "[Warning] This looks like a new post, use --post option"
            id = m.group('id').strip()
    
        post.id = id
        title = self.getTitle(metadata)
        post.title = title.strip()
    
        self.attachType(metadata, post)
        self.attachStatus(metadata, post)
        
        termsAndCats = dict()
        termsAndCats = self.attachTags(metadata, post, termsAndCats)
        termsAndCats = self.attachCategories(metadata, post, termsAndCats)
        post.terms_names = termsAndCats 

        return post
    
    def attachType(self, metadata, post):
        # type wordpress.
        pat = re.compile(r'type:\s*(?P<type>.+)', re.IGNORECASE)
        m = pat.search(metadata)
        if not m:
            print("Warnng. This post has no type. Assuming post")
            post.post_type = 'post'
        else:
            post.post_type = m.group('type').strip()
    
    def attachStatus(self, metadata, post):
        # status 
        statusRegex = re.compile("status:\s*(?P<status>.+)", re.IGNORECASE) 
        m = statusRegex.search(metadata)
        if m :
            status = m.groupdict()['status']
            post.post_status = status.strip()
        else :
            print("[W] Post with uncertain status. Default to publish")
            post.post_status = "publish"
    
    def attachTags(self, metadata, post, termsAndCats):
        # tags 
        tagRegex = re.compile("tag:\*(?P<name>.+)", re.IGNORECASE)
        ms = tagRegex.findall(metadata)
        tags = list()
        for m in ms :
            name = m.strip()
            tags.append(name)
        termsAndCats['post_tag'] = tags 
        return termsAndCats
    
    def attachCategories(self, metadata, post, termsAndCats):
        # categories
        catRegex = re.compile("category:\*(?P<cat>.+)", re.DOTALL)
        mm = catRegex.findall(metadata)
        cats = list()
        for m in mm :
            cat = m.strip()
            cats.append(cat)
        termsAndCats['category'] = cats
        return termsAndCats
    
    def updatePost(self, post, txt, format) :
        # Check if there is no id.

        pat = re.compile(r'~~~+(?P<metadata>.+?)~~~+', re.DOTALL)
        metadata = pat.search(txt).group('metadata')
        content = re.sub(pat, "", txt)
        assert len(metadata) > 0
    
        post = self.appendMetadataToPost(metadata, post)

        printDebug("STEP", "Updating post", post.title)
        assert post.post_type
        # content 
        if content :
            if len(content.strip()) == 0 :
                print("[E] : No content in file.")
                return 
        else :
            print("[W] : Post with empty content.")
            content = ""
    
        if format == "html":
            content = formatter.htmlToHtml(content)
        elif format == "markdown":
            content = formatter.markdownToHtml(content)
            post.content = content
        else:
            post.content = content

        logging.debug(
                "[I] Sending post : {0} : {1}.".format(post.id, post.title)
                )
        try:
            self.wp.call(EditPost(post.id, post))
        except Exception as e:
            logging.debug("[DEBUG] I was trying to update but failed")
            logging.debug(" + You sure that this post exist on the blog.")
            logging.debug("Error was : {0}".format(e))
            raise UserWarning, "Failed to update post", e
    
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
                f.write("~~~~ \n")
                f.write("title: ")
                f.write(title)
                f.write("\ntype: " + post.post_type)
                f.write("\nstatus: " + post.post_status)
                f.write("\nid: " + post.id)
                ff.write("~~~~ \n")
                ff.write("title: ")
                ff.write(title)
                ff.write("\ntype: " + post.post_type)
                ff.write("\nstatus: " + post.post_status)
                ff.write("\nid: " + post.id)
                cats = []
                tags = []
                for t in terms :
                    if t.taxonomy == 'post_tag':
                        tags.append(t.name)
                    elif t.taxonomy == 'category':
                        cats.append(t.name)
                    else:
                        cats.append(t.name)
                if tags:
                    for t in tags:
                        f.write('\ntag: {0}'.format(t)) 
                if cats:
                    for c in cats:
                        f.write('\ncategory: {0}'.format(c))
                f.write('\n')
                ff.write('\n')

                f.write("~~~~\n\n")
                ff.write("~~~~\n\n")

                # TODO: Get links from the post
                # Write content to file.
                self.writeContent(f, content, format)
                self.writeContent(ff, content, "html")
    
    def run(self, args):
        p = os.environ.get('http_proxy')
        if p is not None:
            printDebug("DEBUG", "Using http_proxy evvironment variable")
            if 'http://' in p :
                p = p.replace('http://', '')
            else:pass
            self.wp = Client(self.blog, args.user, args.password, proxy=p)
        else:
            self.wp = Client(self.blog, args.user, args.password)
        # Send a file to wordpress.
        if args.update :
            fileName = args.update
            if not os.path.exists(fileName):
                raise IOError, "File %s does not exists" % fileName
            # Check the format of file.
            format = os.path.splitext(fileName)[1].lower()
            if format in ["htm", "html", "xhtml"]:
                format = "html"
            elif format in ["md", "markdown"]:
                format = "markdown"
            else:
                format = "markdown"

            # Open the file.
            with open(fileName, "r") as f:
                txt = f.read()
            post = WordPressPost()
            assert post is not None
            self.updatePost(post, txt, format) 

        elif args.post :
            self.newPostToWordpress(args.post)

        # Fetch blogs from wordpress.
        elif args.fetch :
            # Get all posts 
            self.fetchWpPosts(args.fetch)

        else : # get recent posts 
            printDebug("STEP", "Getting recent posts")
            posts = self.wp.call(GetPosts( {'post_status': 'publish'}))
            self.writePosts(posts)
