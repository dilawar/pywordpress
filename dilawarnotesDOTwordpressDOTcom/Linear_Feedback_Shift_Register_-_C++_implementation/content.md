~~~~ 
title: Linear Feedback Shift Register : C++ implementation
type: post
status: publish
id: 125
tag: C++ implementation of LFSR
tag: Linear Feedback Shift Register
tag: svn repository
category: Communication
category: Programming
category: Technology and Engineering
~~~~

[Linear Feedback Shift
Registers](http://en.wikipedia.org/wiki/Linear_feedback_shift_register)
(LFSR) arises in many applications, especially in communications. See
wiki page for a good introduction
[http://en.wikipedia.org/wiki/Linear\_feedback\_shift\_register](http://en.wikipedia.org/wiki/Linear_feedback_shift_register).
We implemented LFSR in C++ which can be found here
[https://ee717-iitb.googlecode.com/svn/trunk/A5-1/](https://ee717-iitb.googlecode.com/svn/trunk/A5-1/)
. You can download this code by using
[svn](http://en.wikipedia.org/wiki/Apache_Subversion). If you are not
aware of **svn**then you can simply download these files manually. This
is a ` make ` file project. After having all these files in a directory;
command ` make all ` should build it. Make sure you have **make**
utility installed. Windows user can use
[**Cygwin**](http://www.cygwin.com/) compatibility layer, or for a
better world, you can switch to Unix for once and forever. The code is
sufficiently commented but not documented in single pdf file. I believe
that it has no bug but I take no responsibility for any harm caused by
its use. Nonetheless my best wishes. See **README** file before using
it. After compilation, `./lfsr --help ` should tell you what you need to
do. You can specify polynomial at run time but you will have no control
over public key.
