twordpress
==========
A command line tool to manage your blogs on ``wordpress.com``.

Configuration file 
------------------

Create configuration file ``~/.config/twordpressrc`` with following entry::

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

If you choose to store this file to some other location then you should pass
``--config path/to/twordpressrc`` like option to the ``twordpress`` command.

Dependencies
------------ 

A fork of the library
https://github.com/maxcutler/python-wordpress-xmlrpc/blob/master/docs/index.rst
is included in this version. 

You can install ``pandoc``. This application turn ``html`` to ``markdown``
format and vice-versa. I can do more but this is what we need. If ``pandoc`` is
not available then it uses a python script to turn html to text.

Proxy support is added recently to ``python-wordpress-xmlrcp``. It reads
environment variable ``http_proxy``. If you are behind proxied network, then
``export http_proxy=proxy.something.net:1212`` in your bash. And we are good to
go.
  

3. Fetch posts 
--------------
Following commands fetches post::

    twordpress --blog 1 --fetch all
    twordpress --blog 0 --fetch "Python is awesome"
    twordpress 

First command will download all posts and pages from ``blog1``. And second will
download all posts which matches the given query from ``blog0``. Third command
will download most recent entries from default blog (``blog0``). Currently it
does not download media.
  
Each post gets its own directory and two files ``conetent.md`` and
``content.html`` are created. Edit markdown file and run the following command
to update the post.

4. Updating post 
----------------

Following command update the blog. ::

    $twordpress --blog 0 --update path_to_new_content.md

5. Create new post 
------------------
This command post a new post::
    
    $twordpress --blog 1 --new new_blog.md

The new blog is written in markdown format but a meta-data has to be prefixed.
This is how your blog file should look like.::

     ---
     title: This is title of my awesome post
     status: publish
     tags: [some awesome tag, tag2]
     categories: [catA, some_category]
     ---

     Here is content of blog in markdown format.

     Too much has already been written. This ends my blog.

