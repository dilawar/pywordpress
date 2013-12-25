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
import atom
import BloggerUpdater as BloggerUpdater
from pyblog.colored_print import printDebug
import pyblog.formatter as formatter
import pprint
import lxml.html as lh
from lxml.etree import tostring
      
class Blogger:

    def __init__(self, args):
        self.blogName = args.blogName
        self.initBlogger(args.user, args.password)
        if args.fetch :
            printDebug("INFO", "Fetching the post : {0}".format(args.fetch))
            self.fetchBlogPost(args.fetch)
        else:
            if args.post:
                fileName = args.post
                txt = self.readFile(fileName)
                self.createNewPost(txt)
            elif args.update:
                fileName = args.update
                txt = self.readFile(fileName)
                self.updatePost(txt)
            else:
                printDebug("WARN", "Unsupported option")


    def readFile(self, filePath):
        """ read text from file and set the format accordingly
        """
        fmt, txt = formatter.readInputFile(filePath)
        self.format = fmt
        return txt
        
    def initBlogger(self, user, password):
        """Initialize the blogger client.
        """
        try:
            self.updater = BloggerUpdater.BloggerUpdater(user, password)
        except Exception as e:
            printDebug("ERR", "Failed to communicate with blogger")
            print("Error was {0}".format(e))
            sys.exit(-1)
        self.blog = self.updater.GetBlogByTitle(self.blogName)
        if self.blog is None:
            printDebug("ERR", "Unable to find requested blog: " + self.blogName) 
            sys.exit(1)
        printDebug("DEBUG"
                , "Requested blog found: {0}".format(self.blog.title.text)
            )
        print "Blog name", self.blogName
        self.blogDir = formatter.titleToBlogDir(self.blogName)
        if not os.path.isdir(self.blogDir):
            os.makedirs(self.blogDir)
        else: pass
   
 
    def createNewPost(self, txt):
        """ Create a new post on blogger
        """
        content = formatter.formatContent(txt, self.format)

        mdict = formatter.metadataDict(txt)
        title = mdict['title'][0]
        # Getting post entry
        title = title.strip()
        postEntry = self.updater.GetPostsByTitle(title)
        if len(postEntry) == 0:
            printDebug("USER", "Creating a new post. In format %s" % self.format)
            newpost = self.updater.CreatePost(title, content, mdict)
            self.writePost(newpost, title)
            printDebug("INFO", "New post created with title : {0}".format(title))
        else :
            printDebug("WARN"
                    , "A post with the same title exists." +
                    " Use --update option to update it."
                    )
        return 0 

    def updatePost(self, txt):
        """Update an existing post
        """
        mdict = formatter.metadataDict(txt)
        title = mdict['title'][0]
        published_on = mdict['published'][0]
        if published_on:
            postEntry = self.updater.GetPostByPublishedDate(published_on)
            if len(postEntry) == 0: pass
            else:
                postEntry = postEntry[0]
                content = formatter.formatContent(txt, self.format)
                return self.updater.UpdatePost(postEntry, content, mdict)

        postEntry = self.updater.GetPostsByTitle(title)
        if len(postEntry) == 0:
            printDebug("WARN", "I can't update a non-existing post.")
            printDebug("WARN", " - You better use --post option")
            return 

        # Format is accordingly.
        if len(postEntry) > 1:
            printDebug("WARN", "More then one post found with matching title")
            printDebug("WARN", "Using the last one.")
        postEntry = postEntry[0]
        content = formatter.formatContent(txt, self.format)
        self.updater.UpdatePost(postEntry, content, mdict)
            
    def fetchBlogPost(self, title):
        """Fetch the given blog with a title
        """
        posts = self.updater.GetPostsByTitle(title)
        print "Total post found %s "  % len(posts)
        [self.writePost(post, title) for post in posts]

    def writePost(self, post, title):
        """
        Write a fetched post to directory
        """
        for c  in post.category:
            print c
        filedir = formatter.titleToFilePath(post.title.text, self.blogDir)
        if not os.path.isdir(filedir):
            os.makedirs(filedir)
        metadata = []
        metadata.append("~~~~~")
        metadata.append("title: {0}".format(post.title.text))
        if post.control is not None:
            if post.control.__dict__['draft'].text == "yes":
                metadata.append("status: draft")
            else:
                published_on = post.published.text
                metadata.append("published: {0}".format(published_on))
        else:
            metadata.append("status: published")
            published_on = post.published.text
            metadata.append("published: {0}".format(published_on))

        if post.__dict__['category']:
            for c in post.__dict__['category']:
                metadata.append("tag: {0}".format(c.term))
        metadata.append("~~~~~~\n\n")
        metadata = "\n".join(metadata)

        with open(filedir+"/content.md", 'w') as md:
            with open(filedir+"/content.html", "w") as html:
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
