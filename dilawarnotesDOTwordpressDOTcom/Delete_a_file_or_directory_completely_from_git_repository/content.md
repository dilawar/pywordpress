~~~~ 
title: Delete a file or directory completely from git repository
type: post
status: publish
id: 625
tag: git
tag: purge a file from git history
category: git
~~~~

Committed a large file which is not needed. Committed a file containing
password. Git rm does not remove the file completely form history.
Either the size of
`.git becomes unnecessarily large or sensitive information is still in the repository history.`[**`git-filter-branch`**](http://www.kernel.org/pub/software/scm/git/docs/git-filter-branch.html)
is your friend. You should have a look at its manual page. I wrote a
python script to purge a file or directory from repo history. It can be
found
[here](https://raw.github.com/dilawar/Scripts/master/purge_git_history.py).
Pass the filename as `-f filename` and directory as `-d dirname` to this
script. It will do the rest. It only works on master branch. On other
branches, you have to push yourself.Make sure to provide full path of
file or directory. I am not sure if it would work on regex.

###### Related articles

-   [How the Heck Do I Use
    GitHub?](http://lifehacker.com/5983680/how-the-heck-do-i-use-github)
    (lifehacker.com)
-   [Source Control with
    Git](http://blog.nexcess.net/2011/09/11/source-control-with-git/)
    (nexcess.net)
-   [Git Tips From the
    Pros](http://net.tutsplus.com/tutorials/tools-and-tips/git-tips-from-the-pros/)
    (net.tutsplus.com)

