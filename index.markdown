---
layout: page
title: Home
comments: true
repository_url: http://github.com/dilawar/sniffer
---

Post, edit update your post on [Wordpress](http://wordpress.org).

## Summary 

- Fetch all posts.

~~~
$ twordpress --blog 1 --fetch all
~~~

- Fetch a post with a title matching the given string. This will fetch posts
  whose title matches given after `--fetch` option.

~~~
$ twordpress --blog 0 --fetch "Python is awesome"
~~~~

- Update a post with given markdown content. See the format of file
  [here]({{site.url}}/Format).

~~~
$ twordpress --blog 0 --update path_to_new_content.md
~~~

- Update a post on blog 1 with a raw html content.

~~~
$ twordpress --blog 1 --new new_blog.html
~~~

We support `jekyll` post format.
