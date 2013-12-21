~~~~ 
title: Mail server info of National Center for Biological Sciences (NCBS) Bangalore
type: post
status: publish
id: 946
category: Linux
category: Mail
category: mutt
~~~~

If you are a mutt user like me and working at NCBS Bangalore, you need
to setup your account in mutt as following. Unfortunately, this
information is not available on NCBS intranet.
` set from="REAL_NAME " set from="USER NAME " set hostname="imaps://imap.ncbs.res.in" set folder="imaps://imap.ncbs.res.in" set record="+INBOX.Sent" set imap_user="NCBS_USER" set imap_pass="NCBS_PASS" set postponed="=Drafts" set spoolfile="+INBOX" set signature="sign.txt" set smtp_url="smtp://NCBS_USER@mailsvr.ncbs.res.in" smtp_pass="$NCBS_PASS" set realname="$REAL_NAME"`
In short incoming server is **imap.ncbs.res.in** and outgoing server is
**mailsvr.ncbs.res.in**. Use default ports. To get smtp server
information, you can always use
` msmtp -v --host=mailsvr.ncbs.res.in --serverinfo --tls=on --tls-certcheck=off --port 25`
\~
