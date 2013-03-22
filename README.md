pywordpress
===========

A command line Wordpress client to post and edit posts

1. Configuration file 
---------------------
Create a file ~/.wordpressrc with following entry 

    # This file must be saved as ~/.wordpressrc 
    [blog]
    # Url of blog. 
    url=dilawarnotes.wordpress.com
    # Wordpress username
    username=dilawars
    password=mypassword

2. Dependencies 
----------------

  [Download and install this
  library](https://github.com/maxcutler/python-wordpress-xmlrpc/blob/master/docs/index.rst).
  It may be available on most of the linux distributions. It does not work when
  networks are behind proxy (such as mine at IIT Bombay). You can set-up
  transparent-proxies (one of my repository have scripts) to overcome this.
  Author of this library has indicated that he will support proxies in
  next release. 

3. Fetch posts 
--------------
  
    $./wordpress.py --fech all 

  And wait! 
  
  It will create a directory named after your blog and save all posts
  in that directory. Formatting is creepy. Open a file and see if you like it.

  You can edit file and send it back to Wordpress :

  $./wordpress.py --update filename.blog 

4. Creating or update a post 
----------------------

  You have to write a file in similar format as the blogs you got after fetch.
  You can discard the <ID> </ID> field. It will append a <ID> </ID> line to your
  blog and save it in the same directory in which you have downloaded other
  blogs. 

    $./wordpress.py --post file.blog 

  You can now delete file.blog .


See repo for some poorly written blogs fetched from by blog.

