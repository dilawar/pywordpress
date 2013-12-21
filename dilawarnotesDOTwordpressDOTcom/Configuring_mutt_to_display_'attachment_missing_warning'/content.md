~~~~ 
title: Configuring mutt to display 'attachment missing warning'
type: post
status: publish
id: 884
category: mutt
~~~~

This method works if you are using vim as your editor. In file
`~/.vim/ftplugin/mail.vim`, write this function definition.

[sourcecode language="bash"] function! CheckAttach() let
check='attach,angehängt,attachment,Anhang' let oldPos=getpos('.') let
ans=1 let val = join(split(escape(check,' \\.+\*'), ','),'\\|') 1 if
search('\\%('.val.'\\)','W') let ans=input(&quot;Attach file?: (leave
empty to abbort): &quot;, &quot;&quot;, &quot;file&quot;) while (ans !=
'') normal magg}- call append(line('.'), 'Attach: '.ans) redraw let
ans=input(&quot;Attach another file?: (leave empty to abbort): &quot;,
&quot;, &quot;file&quot;) endwhile endif exe &quot;:write &quot;.
expand(&quot;&lt;amatch&gt;&quot;) call setpos('.', oldPos) endfu
augroup script au! au BufWriteCmd,FileWriteCmd mutt\* :call
CheckAttach() augroup END [/sourcecode] And in `.muttrc`, you should
have something like this.

    set editor = "vim -c 'set spell spelllang=en syntax=mail ft=mail enc=utf-8' '+/^$'"

Notice that we have `ft=mail`. This will automatically load the funtion.

### Reference

​1. http://www.mail-archive.com/mutt-users@mutt.org/msg37580.html

Or you can use [this
script.](http://www.vim.org/scripts/script.php?script_id=2796). Remove
the above line from `.vimrc`.
