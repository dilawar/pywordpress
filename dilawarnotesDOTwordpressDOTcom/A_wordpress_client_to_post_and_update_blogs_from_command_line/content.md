~~~~ 
title: A wordpress client to post and update blogs from command line
type: post
status: publish
id: 855
tag: NoGuiNoMouseNoProblem
category: NoGuiNoMouseNoProblem
category: Python
category: Scripts
~~~~

There is a fascinating [python
library](https://github.com/maxcutler/python-wordpress-xmlrpc/blob/master/docs/index.rst)
which uses xmlrpc to communicate with Wordpress. Unfortunately it does
not support `http_proxies` yet but he has promised to support it in next
release. Till then, one can set-up transparent proxies [See my
[repository on how to set-up transparent proxies inside IIT
Bombay](http://github.com/dilawar/Transparent-Proxy)]. \

Benefits? Nothing unless you are a command like junkie like me. I am
editing this post in vim editor and using github to maintain my blogs.
When I am satisfied, I'll update it or create a new post. I can also
**tags** and **category** to post. And I have all the power of html and
vim. Ha ha! With so much power, I'll bring this world down at its knees.

Till today Sat 23 Mar 2013, I can not send an image with post from
terminal. I'll add this feature in near-future.

This script is available [here](http://github.com/dilawar/pywordpress).
If you plan to update it, let me know. There is another script in the
same repo `blogger.py` which does the same stuff with **blogspot**. I no
longer use blogspot therefore I'd not be updating that script.
