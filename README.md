twordpress
===========

A command line tool to manage your blogs on ``wordpress.com``.

1. Configuration file 
---------------------
Create a file ~/.wordpressrc with following entry 

    # This file must be saved as ~/.wordpressrc 
    [blog0]
    # Url of blog. 
    url=dilawarnotes.wordpress.com
    # Wordpress username
    username=dilawars
    password=mypassword
    [blog1]
    url=blog2.wordpress.com
    username=gabbar
    password=thakur_ke_per_katne_the

2. Dependencies 
----------------

  [A fork of this
  library](https://github.com/maxcutler/python-wordpress-xmlrpc/blob/master/docs/index.rst).
  is included in this version. You need ``pandoc`` installed. This application
  turn ``html`` to ``markdown`` format and vice-versa. I am planning to replace
  pandoc with something more pythonic.

  Proxy support is added recently to ``python-wordpress-xmlrcp``. It reads
  environment variable ``http_proxy``. If you are behind proxied network, then
  export ``http_proxy`` variable in your bash and we are good to go.
  

3. Fetch posts 
--------------
  
    $twordpress --blog 1 --fetch all 
    $twordpress --blog 0 --fetch "Python is awesome"

First command will download all posts and pages from ``blog1``. And second will
download all posts which matches the given query from ``blog0``. Currently it
does not download media.
  
Each post gets its own directory and a file ``conetent.md`` is created. Edit
this file and run the following command to update the post.

4. Updating post 
----------------

    $twordpress --blog blog_id_in_int --update path_to_new_content.md 

5. Create new post 
----------------------
    
    $twordpress --blog 1 --post new_blog.md 

The new blog is written in markdown format but a meta-data has to be prefixed.
This is how your blog file should look like.

     ~~~~~
     title: This is title of my awesome post
     status: publish
     tags: some awesome tag
     category:
     ~~~~~~

     Here is content of blog in markdown format.

     Too much has already been written. This ends my blog.



