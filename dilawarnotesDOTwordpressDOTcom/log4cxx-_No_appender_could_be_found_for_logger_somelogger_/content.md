~~~~ 
title: log4cxx: No appender could be found for logger (somelogger) 
type: post
status: publish
id: 708
tag: log4cxx
category: Uncategorized
~~~~

Whooa! If nothing is working, do the following :

> Put a log4cxx configuration file named log4cxx.properties under the
> same directory as your executable.

Most likely your application could not read the configuration file path
you have so hopefully coded while setting up your logger. Trust me, I
have spent an hour trying to debug my little logger.
