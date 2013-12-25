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

"""Simple class for updating posts on www.blogger.com service"""

class BloggerUpdater:
    
    """Initializing instance and login into www.blogger.com"""
    def __init__(self, user, password):
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
        query = service.Query()
        query.feed = '/feeds/default/blogs'
        feed = self.blogger_service.Get(query.ToUri())
        for entry in feed.entry:
            if entry.title.text == title:
                self.blog_id = entry.GetSelfLink().href.split("/")[-1]
                return entry
        printDebug("ERR", "Can't find blog with title : {0}".format(title))
        sys.exit(0)
    
    """This will get post entry by it's title (name)"""
    def GetPostByTitle(self, title):
      ''' Fetch a single post which matches the title most. If "all" or
      "recent" are given then fetches all or recents posts. 
      '''
      posts = list()
      if title != "all" :
          feed = self.blogger_service.GetFeed('/feeds/' 
                  + self.blog_id + '/posts/default'
                  )
          for entry in feed.entry:
            if entry.title.text :
              if title != "recent" :
                match = difflib.SequenceMatcher(None, entry.title.text 
                  ,title).ratio()
                if match > 0.7 :
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
          query.feed = '/feeds/' + self.blog_id + '/posts/default'
          query.published_min = '1980-01-01'
          query.published_max = time.strftime('%Y-%m-%d')
          feed = self.blogger_service.Get(query.ToUri())

          printDebug(feed.title.text 
                  + " posts between " 
                  + query.published_min + " and " 
                  + query.published_max
                  )
          for entry in feed.entry:
              if entry.title.text :
                  posts.append(entry)
          return posts 
    
    """This will update supplied post entry with new content
    Updated post entry returned as result"""
    def UpdatePost(self, postEntry, newContent):
        """ Update the give n post.
        """
        contentType = postEntry.content.type
        postEntry.content = atom.Content(contentType, None, newContent)
        return self.blogger_service.Put(postEntry, postEntry.GetEditLink().href)

    """ Create a new post """
    def CreatePost(self, title, content) :
        entry = GDataEntry()
        entry.title = atom.Title('xhtml', title)
        entry.content = atom.Content(content_type='html', text=content)
        return self.blogger_service.Post(entry, '/feeds/%s/posts/default' % self.blog_id)
