~~~~ 
title: getmail4 problem : invalid syntax in multidestination
type: post
status: publish
id: 443
tag: getmail4 syntax error
category: Uncategorized
~~~~

In getmail4, I was having problem with my multi-destination
configuration which was following, [sourcecode language="text"]
destinations = ('[other-destination-1]', '[other-destination-2]')
[other-destination-1] type = Mboxrd path = /var/spool/mail/alice user =
alice [other-destination-2] type = Maildir path = /home/joe/Maildir/
user = joe [/sourcecode] It did not work and gave me following error.
**             incorrect format (invalid syntax (, line 1))) .** Change
this to following and it worked [sourcecode language="text"]
destinations = ('\~/Mail/inbox/', '\~/Mail/archive/current/')
[/sourcecode]
