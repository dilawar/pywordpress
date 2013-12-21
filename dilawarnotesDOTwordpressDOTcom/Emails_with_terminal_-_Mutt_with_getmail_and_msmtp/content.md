~~~~ 
title: Emails with terminal - Mutt with getmail and msmtp
type: post
status: publish
id: 367
tag: Getmail
tag: iitb ee
tag: iitb gpo
tag: mutt
tag: smstp
tag: terminal email clien
category: Technology and Engineering
~~~~

Hello, terminal lovers. There are many other blogs written about 'mutt'
and 'getmail'. Surely you can take hints from any of them. This post is
written for IIT Bombay email servers. You pathetic Windows guys, piss
off!!

### Get Emails from Server

First of all, we need to use 'something' to fetch emails from gpo
server. Mutt can be used to read directly from server. But I like
storing my emails on my machine. I prefer
['getmai](http://en.wikipedia.org/wiki/Getmail)l' over fetchmail to do
that for reasons I don't know. It is an awesome tool to do that since it
never gave me trouble.  IIT Bombay email server supports IMAP. We have
to configure getmail to fetch mails from there using IMAP and store it
somewhere. Here is the script of this. Make sure you have three
directories in /GPO-IITB/ directory named 'cur', 'new', and 'temp'
(without single quote). We are storing emails in two type of mainboxes,
maildir and mboxrd. To understand these concepts read
[this](http://pyropus.ca/software/getmail/configuration.html). Name this
file 'getmail.gpo' and store it in \~/.getmail directory. [sourcecode
language="txt"] [retriever] type = SimpleIMAPRetriever server =
imap.iitb.ac.in username = khookhar password = darinda [destination]
type = MultiDestination destinations = ('[mboxrd-destination]',
'[maildir-destination]') [mboxrd-destination] type = Mboxrd path =
\~/Mail/GPO-IITB/gpo\_backup.mbox [maildir-destination] type = Maildir
path = \~/Mail/GPO-IITB/ [options] verbose = 2 read\_all = False
message\_log = \~/.getmail/gpo.log [/sourcecode] If you also wants EE
account then create one more file getmail.ee as following. [sourcecode
language="text"] [retriever] type = SimpleIMAPRetriever server =
sandesh.ee.iitb.ac.in username = profchaos password = ihatekartman
[destination] type = MultiDestination destinations =
('[mboxrd-destination]', '[maildir-destination]') [mboxrd-destination]
type = Mboxrd path = \~/Mail/EE-IITB/ee\_backup.mbox
[maildir-destination] type = Maildir path = \~/Mail/EE-IITB/ [options]
verbose = 2 read\_all = False message\_log = \~/.getmail/ee.log
[/sourcecode] Now run from terminal.
` $getmail -r getmail.gpo $getmail -r getmail.ee` First line will
download all new messages into local directories. Now you are ready to
read them using mutt or some other client. This will not delete messages
from your server.

### Using mutt to read and send emails

Here is my \<p\>\~/.muttrc\</p\> file for this purpose. Not that even if
you are storing a same message in two mailbox we are only using one
mailbox to read and send message. Other one is for backup. [sourcecode]
\# Name set realname = 'Prof Chaos' \#\#\#\#\#\#\#\#\#\# \# This is to
read gmail message directly from server. set folder =
"imaps://imap.gmail.com:993" set spoolfile = "+INBOX" set postponed =
"+[Gmail]/Drafts" set trash = "imaps://imap.gmail.com/[Gmail]/Trash" set
username = "profchaos@gmail.com" set password = "ihatekartman" \#\# set
local folder. set header\_cache = \~/.mutt/cache/headers set
message\_cachedir = \~/.mutt/cache/bodies set certificate\_file =
\~.mutt/certificates \# \#\# where mails are stored set folder =
\~/Mail/ mailboxes = GPO-IITB mailboxes = EE-IITB mailboxes = INBOX set
record = \~/Mail/GPO-IITB/sent set sort = threads set postponed =
\~/Mail/GPO-IITB/drafts set mbox\_type = MailDir set content\_type =
"text/html" set signature = "\~/Mail/sign.html" \#message-hook \~A 'set
pager=vim' \#\# message-hook '\~f rfs' 'set pager="less"+/\^ subject:
.\*\\""' \#\# this our send email client. set sendmail =
"/usr/bin/msmtp" \#\# Editor set editor = "vim" ignore \* unignore date
from subject to cc \# \#\#\# mutt option \#\#\# set folder\_format =
"%2C %t %N %8s %d %f" set edit\_headers = no set askbcc = yes set
text\_flowed = yes set abort\_nosubject = ask-yes set abort\_unmodified
= ask-yes set copy = yes set include = yes set metoo = yes \# send reply
to myself. set hdrs my\_hdr From: Dilawar my\_hdr X-Mailer: 'mutt -v|
head -n 1' macro generic "1" ":set from 'Dilawar '" color hdrdefault
brightcyan black color header brightwhite black "\^from:" color header
brightwhite black "\^subject:" color quoted brightgreen blue color
quoted brightwhite blue color quoted brightwhite blue color signature
brightwhite black color indicator blue green color error red black mono
error bold color status black cyan mono status bold color tree yellow
blue color tilde brightmagenta blue color body red black
"[-a-z\_0-9.]+@[-a-z\_0-9.]+" mono body bold
"[-a-z\_0-9.]+@[-a-z\_0-9.]+" color body red black "\^Good signature"
mono body bold "\^Good signature" color body brightwhite red "\^Bad
signature from.\*" mono body bold "\^Bad signature from.\*" color normal
white black color message red white color attachment red blue \#\# Here
is address-book alias epw-circulation Circulation alias harami harami
alias pilla pilla [/sourcecode] Now we need to send email. We have
choses 'msmtp' as our send-mail client. Configure it too. We are using
iitb-gpo for sending emails. [sourcecode] account default host
smtp-auth.iitb.ac.in port 25 protocol smtp auth on from
profchaos@iitb.ac.in user profchaos password ihatecartman tls on
tls\_starttls on tls\_certcheck off [/sourcecode]
