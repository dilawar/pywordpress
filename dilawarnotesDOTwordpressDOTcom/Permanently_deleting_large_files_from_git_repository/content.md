~~~~ 
title: Permanently deleting large files from git repository
type: post
status: publish
id: 803
tag: git
tag: python script
category: git
~~~~

Gurus on [Stackoverflow](http://stackoverflow.com/ "Stack Overflow")
have already
[answered](http://stackoverflow.com/questions/5563564/remove-files-from-git-repo-completely)
it. I wrote a script which automate this process. I have written [a
python
script](https://github.com/dilawar/Scripts/blob/master/git_search_and_purge.py)
to automate this process. This script accepts size of the file after -s
switch (in bytes) and [regular
expression](http://en.wikipedia.org/wiki/Regular_expression "Regular   expression")
after -e switch to match against the name of the file. For example, if I
want to delete files bigger than 20000 bytes and with names prefixed by
pdf then I'll have to use the script as following :

     python git_search_and_purge.py -s 20000 -e .*pdf$ 

It might take a lot of time to complete the job. It writes full
branch-tree as many times are their are commits. I believe you know the
danger of doing this on a shared repository. Another script which only
searches files bigger than a given size and regular pattern. Regular
pattern is optional. If it is not given, all files bigger than given
size are printed on console. This script [is available
here](https://github.com/dilawar/Scripts/blob/master/git_find_big_files.py).
Using it is safe. It does not change the state of repository in any way.
You can dump its output to a file and then execute your evil plans
accordingly. On github, there is an article on 'removing sensitive data
from github' or something like that. Do read that article. Happy
gitting!

###### Related articles {.zemanta-related-title style="font-size:1em;"}

-   [Git Tips And Workflows, Round 2: basics, stashes and
    submodules](http://durdn.com/blog/2013/01/14/10-git-tips-and-workflows-round-2/)
    (durdn.com)

