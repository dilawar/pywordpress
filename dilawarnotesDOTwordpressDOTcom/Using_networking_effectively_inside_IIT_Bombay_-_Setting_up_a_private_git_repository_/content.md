~~~~ 
title: Using networking effectively inside IIT Bombay : Setting up a private git repository 
type: post
status: publish
id: 789
tag: git
tag: git on sharada
category: git
category: IIT Bombay
category: Utility
~~~~

Ever felt like screaming when your file is not backed-up and you deleted
it? Ever felt like screaming twice when you made a small change in your
file and code stopped working. Well then, [version control
system](http://en.wikipedia.org/wiki/Revision_control "Revision control")
is all you need. We use **`git`** and lobby for it also. For public
work, such as assignment etc, you can use
[github.com](https://github.com/) and code.google.com . Both provides
support for git. You should read about what git is before you continue.
It would not make much sense to you otherwise. There are two ways to use
git. One is to use it locally when there is no network. Your local
changes are stored on local computer only and not mirrored to a remote
server. Second, to use a server to store the history. This is very
useful should your personal computer crashes or you have to work in a
team. We'll show how to use our sharada server for such purpose. If you
belong to Electrical Engineering department at IIT Bombay then you must
be having an account on sharada server (`10.107.1.2`). I know, I know,
you haven't logged onto it for a while; we'll do it today. If you have
account on some other machine which you can access via `ssh` then you
can also read on. Let's log-on to sharada.

    dilawar@hobbes:~$ ssh -X dilawar@sharada.ee.iitb.ac.in
    Last login: Sun Jan 27 17:27:28 2013 from 10.107.105.13
    dilawar@sharada:~$

You may have to accept the signature of machine and enter your password.
I am using public-private key based authentication mechanism (no need
for password, but can be dangerous sometimes). Anyway, we are inside
sharada and in my home.

    dilawar@sharada:~$ pwd
    /pg/rs/dilawar

Let's initialize a repository which we'll use for our private work;
let's call it **repo\_on\_sharada**.

    dilawar@sharada:~$ ls
    mail  mbox  public_html  Scripts
    dilawar@sharada:~$ mkdir repo_on_sharada
    dilawar@sharada:~$ ls
    mail  mbox  public_html  repo_on_sharada  Scripts
    dilawar@sharada:~$ cd repo_on_sharada/
    dilawar@sharada:~/repo_on_sharada$ ls

Great, now we are good to go. Since it is our storehouse and we'll never
work on sharada we will initialize a repo which is bare.

    dilawar@sharada:~/repo_on_sharada$ git init --bare
    Initialized empty Git repository in /pg/rs/dilawar/repo_on_sharada/
    dilawar@sharada:~/repo_on_sharada$

Great, we have a bare initialized repo. Notice that its path on sharada
server is **`/pg/rs/dilawar/repo_on_sharada/ `**. Now logout from
sharada and forget about it. On your lapton, cd to some location and do
the following.

    dilawar@hobbes:~/Works$ git clone ssh://sharada.ee.iitb.ac.in/pg/rs/dilawar/repo_on_sharada 
    Cloning into 'repo_on_sharada'...
    warning: You appear to have cloned an empty repository.

Now we have cloned a empty repository. Now we are ready to make our
first commit. Create a file named `readme` with few lines, add and
commit it.

    dilawar@hobbes:~/Works/repo_on_sharada (master)*$ git add readme
    dilawar@hobbes:~/Works/repo_on_sharada (master)*$ git commit -m "my first commit"
    [master (root-commit) 03e612d] my first commit
     1 file changed, 1 insertion(+)
     create mode 100644 readme
    dilawar@hobbes:~/Works/repo_on_sharada (master)$

This file readme is stored locally and has not yet sent to sharada.
Since this is our first commit, our repo still doesn't know about
branch. We need to specify a branch to which this local repository
should be pointed to (the term branch is not used here in strict sense).

    dilawar@hobbes:~/Works/repo_on_sharada (master)$ git push origin master
    Counting objects: 3, done.
    Writing objects: 100% (3/3), 232 bytes, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To ssh://sharada.ee.iitb.ac.in/pg/rs/dilawar/repo_on_sharada
     * [new branch]      master -> master

Origin usually means the remote server which is sharada in our case.
Branch master is a branch on this remote. We can have more than one
branch such as dilawar, vinay etc. Anyway how to branch and merge
branches is advanced topic and can be learned later. For now, we have a
private repo to work with. Now even if you delete the directory, you can
clone the repository again. Now go to any computer, clone your
repository, work till your ass start sweating.  Add and commit your work
and push to origin. When it is done delete the folder and go home. Your
work, along with its history, is safe. You should play with github for
sometime to learn more about git. You can now read how to use
git-workflow for your work. There are [great many
tutorial](http://git-scm.com/documentation) around on the web. There is
no need to write one more. However, if you run into trouble, I'll be
happy to help you!

###### Related articles {.zemanta-related-title style="font-size:1em;"}

-   [Using networking effectively inside IIT Bombay : SSHing to hostel
    room](http://dilawarnotes.wordpress.com/2013/02/21/using-networking-effectively-in-iit-bombay-sshing-to-hostel-room/)
    (dilawarnotes.wordpress.com)
-   [Source Control with
    Git](http://blog.nexcess.net/2011/09/11/source-control-with-git/)
    (nexcess.net)
-   [Getting Started with
    Git](http://techportal.inviqa.com/2013/02/19/getting-started-with-git/)
    (techportal.inviqa.com)

