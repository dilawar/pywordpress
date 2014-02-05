---
layout: page
title: Home
comments: true
repository_url: http://github.com/dilawar/sniffer
---

Post, edit update your post on [Wordpress](http://wordpress.org).

## Summary 

- Fetch all posts

~~~
$ twordpress --blog 1 --fetch all
~~~

- Fetch a post matching a tile

~~~
$ twordpress --blog 0 --fetch "Python is awesome"
~~~~

- Update a post with given markdown format.

~~~
$ twordpress --blog 0 --update path_to_new_content.md
~~~

- Update a post on blog 1 given html post

~~~
$ twordpress --blog 1 --new new_blog.html
~~~

We support `jekyll` post format.
