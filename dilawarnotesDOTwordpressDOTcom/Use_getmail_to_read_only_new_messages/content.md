~~~~ 
title: Use getmail to read only new messages
type: post
status: publish
id: 365
tag: Getmail
tag: multiple copies of email
tag: Random
category: Uncategorized
~~~~

If your getmail is giving multiple copies of messages are each run, then
do this in your configuration file in \~/.getmail/ directory.

    [options]
    verbose = 0
    read_all = false
    delete = true
    message_log = ~/.getmail/log

    read_all

is by default True. You need to set it false else it will create many
copies of same message and will make your life miserable.
