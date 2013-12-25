'''
Created on Apr 17, 2012
@author: Vlad Gorloff
Edited: Dilawar Singh Wed Dec 25 06:16:19 2013

'''

import difflib
from gdata import service, GDataEntry
import atom
import sys
import time
from pyblog.colored_print import printDebug
import datetime as dt

"""Simple class for updating posts on www.blogger.com service"""

class BloggerUpdater:
    
    """Initializing instance and login into www.blogger.com"""
    def __init__(self, user, password):
        #self.fmt = '%Y-%m-%dT%H:%M:%S'
        self.fmt = ''
        self.blogger_service = service.GDataService(user, password)
        # Client software name
        self.blogger_service.source = 'gv-cl-blogger-updater-1.0'   
        self.blogger_service.service = 'blogger'
        self.blogger_service.account_type = 'GOOGLE'
        self.blogger_service.server = 'www.blogger.com'
        # Let's protect connection
        self.blogger_service.ssl = True                             
        printDebug("INFO"
                , "Logging into " + self.blogger_service.server
                )
        self.blogger_service.ProgrammaticLogin()
        if self.blogger_service.current_token is None:
            printDebug("ERR",
                    "Unable to login into {0}".format(
                        self.blogger_service.server
                        )
                    )
            sys.exit()
    
    """This will get blog entry by it's title (name)"""  
    def GetBlogByTitle(self, title):
        self.feed1 = '/feeds/default/blogs'
        query = service.Query()
        query.feed = '/feeds/default/blogs'
        feed = self.blogger_service.Get(query.ToUri())
        for entry in feed.entry:
            if entry.title.text == title:
                self.blog_id = entry.GetSelfLink().href.split("/")[-1]
                self.feed2 = '/feeds/%s/posts/default' % self.blog_id 
                return entry
        printDebug("ERR", "Can't find blog with title : {0}".format(title))
        sys.exit(0)
    
    def GetPostsByTitle(self, title):
      ''' Fetch a single post which matches the title most. If "all" or
      "recent" are given then fetches all or recents posts. 
      '''
      posts = list()
      if title != "all" :
          self.feed = self.blogger_service.GetFeed(self.feed2)
          for entry in self.feed.entry:
            if entry.title.text :
              if title != "recent" :
                match = difflib.SequenceMatcher(None
                        , entry.title.text,title
                        ).ratio()
                if match > 0.6 :
                  printDebug("INFO"
                          , "Found with title : {0} ".format(entry.title.text)
                          )
                  posts.append(entry) 
                  return posts
                else : pass 
              else : # We want all recent posts
                posts.append(entry)
            else : pass # Titleless post
          printDebug("DEBUG", "Total {0} posts fetched . ".format(len(posts)))
          return posts
    # fetch all
      else : 
          query = service.Query()
          query.feed = self.feed2
          frm = dt.datetime.now() - dt.timedelta(days=3650)
          to = dt.datetime.now()
          return self.GetPostsBetweenDates(
                  dt.datetime.strftime(frm, self.fmt)
                  , dt.datetime.strftime(to, self.fmt)
                  )
    
    def GetPostsBetweenDates(self, frm, to):
        """ Create a query and fetch posts
        """
        posts = []
        query = service.Query()
        query.feed = self.feed2
        query.published_min = frm
        query.published_max = to
        feed = self.blogger_service.Get(query.ToUri())

        printDebug("INFO"
                , " Fetching posts between " 
                + query.published_min + " and " 
                + query.published_max
                )
        for entry in feed.entry:
            posts.append(entry)
        return posts 

    def GetPostByPublishedDate(self, published_on):
        self.feed = self.blogger_service.GetFeed(self.feed2)
        posts = []
        for entry in self.feed.entry:
            if published_on in entry.published.text:
                posts.append(entry)
        return posts 
        
    def UpdatePost(self, postEntry, newContent, mdict):
        """ Update the give n post.
        """
        printDebug("INFO", "Updating", postEntry.title.text)
        postEntry.title = atom.Title('html', mdict.get('title')[0])
        postEntry.content = atom.Content(content_type='html',text=newContent)
        for t in mdict.get('tag'):
            postEntry.category.append(atom.Category(term=t))
        if mdict.get('status')[0] == 'draft':
            control = atom.Control()
            control.draft = atom.Draft(text='yes')
            postEntry.control = control
        try:
            self.blogger_service.Put(postEntry, postEntry.GetEditLink().href)
        except Exception as e:
            printDebug("WARN", "Failed to update this post.")
            print(" + Error : {0}".format(e))
            return 0

    """ Create a new post """
    def CreatePost(self, title, content, mdict) :
        printDebug("USER", "Creating a new post: {0}".format(title))
        entry = GDataEntry()
        entry.title = atom.Title('xhtml', title)
        for t in mdict.get('tag'):
            entry.category.append(atom.Category(term=t))
        if mdict.get('status')[0] == 'draft':
            control = atom.Control()
            control.draft = atom.Draft(text='yes')
            entry.control = control
        entry.content = atom.Content(content_type='xhtml', text=content)
        return self.blogger_service.Post(entry, self.feed2)
