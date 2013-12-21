~~~~ 
title: LD_LIBRARY_PATH is not working in Makefile
type: post
status: publish
id: 684
tag: LIBRARY_PATH vs LD_LIBRARY_PATH
tag: Makefile
category: Linux
category: Programming
~~~~

If LD\_LIBRARY\_PATH is exported in Makefile and makefile is not working
as you have expected, then you should try updating LIBRARY\_PATH.

> LIBRARY\_PATH is used by gcc before compilation to search for
> directories containing libraries that need to be linked to your
> program.

If you wish to link static libraries, you should update LIBRARY\_PATH
and not LD\_LIBRARY\_PATH. I made a mistake and suffered for 2 hours.

> LD\_LIBRARY\_PATH is used by your program to search for directories
> containing the libraries after it has been successfully compiled and
> linked.

See [this
question.](http://stackoverflow.com/questions/4250624/ld-library-path-vs-library-path)
