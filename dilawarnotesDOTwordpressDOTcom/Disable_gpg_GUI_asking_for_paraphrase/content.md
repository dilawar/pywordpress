~~~~ 
title: Disable gpg GUI asking for paraphrase
type: post
status: publish
id: 719
tag: disable gui in gpg
tag: GNU Privacy Guard
category: Linux
category: NoGuiNoMouseNoProblem
category: Utility
~~~~

1.  Someone suggested that if you have seahorse installed, remove it.
    **(I did, but it did not work)**
2.  Someone suggested that exporting `PINENTRY_USER_DATA="USE_CURSES=1"`
    will do the trick. It also did not work.

Add `--no-use-agent` to the command option. It worked with old version
of `gpg`. No gui is appeared while decrypting the file.

This does not work with `gpg2`. Program `gpg2` needs a use-agent. You
have to create a file `~/.gnupg/gpg-agent.conf` and add the line

    pinentry-program /usr/bin/pinentry-curses

. And we are done.

###### Related articles

-   [How to Encrypt and Decrypt a File using GnuPG in
    Linux](http://www.thegeekstuff.com/2013/02/gpg-encrypt-decrypt/)
    (thegeekstuff.com)
-   [GPG Key-Pair Encryption and Decryption and
    Signing](http://priyac91.wordpress.com/2013/01/13/gpg-key-pair-encryption-and-decryption-and-signing/)
    (priyac91.wordpress.com)

