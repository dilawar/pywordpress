#!/usr/bin/env python
'''
Created on Apr 17, 2012
Originall written by : Vlad Gorloff

Modified by Dilawar for personal use.
'''
import argparse
import os
import sys
import getopt
import re
import BloggerUpdater as BloggerUpdater
from pyblog.colored_print import printDebug
import pyblog.formatter as formatter
import pprint
import lxml.html as lh
from lxml.etree import tostring
      
class Blogger:

    def __init__(self, args):
        blog = args.blog
        self.initBlogger(args.user, args.password)
        if args.fetch :
            printDebug("INFO", "Fetching the post : {0}".format(args.fetch))
            self.fetchBlogPost(args.fetch)
        elif args.post :  
            file = args.post
            if not os.path.exists(file) :
                print("File {0} does not exists".format(file))
                return
            # Opening source HTML for reading
            txt = open(file, 'r').read()   
            self.createNewPost(txt)
        elif args.update:
            file = args.update
            if not os.path.exists(file) :
                print("File {0} does not exists".format(file))
                return
            # Opening source HTML for reading
            txt = open(file, 'r').read()   
            self.updatePost(txt)
        else:
            printDebug("WARN", "Unsupported option {0}")


    def initBlogger(self, user, password):
        """Initialize the blogger client.
        """
        try:
            self.updater = BloggerUpdater.BloggerUpdater(user, password)
        except Exception as e:
            printDebug("ERR", "Failed to communicate with blogger")
            print("Error was {0}".format(e))
            sys.exit(-1)
        self.blog = self.updater.GetBlogByTitle(blog)
        if self.blog is None:
            printDebug("ERR", "Unable to find requested blog: " + blog) 
            sys.exit(1)
        debugPrint("DEBUG"
                , "Requested blog found: {0}".format(blogEntry.title.text)
            )
        blog = formatter.titleToBlogDir(blog)
        if not os.path.exists(blog):
            os.mkdirs(blog)
        else: pass
        self.blogdir = blog
   
 
    def createNewPost(self, txt):
        """ Create a new post on blogger
        """
        medadata = formattter.getMetadata(txt)
        content = formattter.getContent(txt)
        mdict = formatter.metadataDict(metadata)
        title = mdict['title'][0]
        # Getting post entry
        title = title.strip()
        postEntry = updater.GetPostByTitle(title)
        if len(postEntry) == 0:
            printDebug("Creating a new post")
            newpost = updater.CreatePost(title, content)
            printDebug("INFO", "New post created with title : {0}".format(title))
        else :
            printDebug("WARN"
                    , "A post with the same title exists." +
                    " Use --update option to update it."
                    )
        return 

    def updatePost(self, txt):
        medadata = formattter.getMetadata(txt)
        content = formattter.getContent(txt)
        mdict = formatter.metadataDict(metadata)
        title = mdict['title'][0]
        # Getting post entry
        title = title.strip()
        postEntry = updater.GetPostByTitle(title)
        postEntry = postEntry.pop()
        printDebug("INFO"
            , "Requested post found: {0}. Last update: {1}. Updating..".format(
                postEntry.title.text
                , postEntry.updated.text
                )
            )
        # Updating post with new content
        resultEntry = updater.UpdatePost(postEntry, content)
        printDebug("USER"
                , "Successfully updated: {0}. Last update: {1}. Done!".format(
                    resultEntry.title.text
                    , resultEntry.updated.text
                    )
                ) 
        return 
            
    def fetchBlogPost(self, title):
        """Fetch the given blog with a title
        """
        posts = self.updater.GetPostByTitle(title)
        [self.writePost(post, title) for post in posts]

    def writePost(self, post, title):
        """
        Write a fetched post to directory
        """
        filename = formatter.titleToFilePath(title)
        filePath = os.path.join(self.blogdir, filename)
        if not os.path.isdir(filePath):
            os.makedirs(filePath)

        metadata = []
        metadata.append("~~~~~")
        metadata.append("title: {0}".format(post.title.text))
        metadata.append("status: {0}".format(post.status))
        metadata.append("id: {0}".format(post.id))
        metadata.append("tahs: {0}".format(post.labels))
        metadata.append("~~~~~~")
        metadata = "\n".join(metadata)

        with open(filePath+"/content.md", 'w') as md:
            with open(filePath+"/content.html", "w") as html:
                md.write(metadata)
                html.write(metadata)
                content = post.content.text 
                html.write(formatter.htmlToHtml(content))
                md.write(formatter.htmlToMarkdown(content))

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Blogger client")
  parser.add_argument('--fetch', metavar="f"
      , help="Fetch a post with similar looking name. If 'recent' is given, it  \
          fetch and save recent posts. If 'all' is given then it fetches all\
          posts "
      )
  parser.add_argument('--send', metavar='s'
      , help="Update a post."
      )
  args = parser.parse_args()
  p = Blogger(args)
