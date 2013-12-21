~~~~ 
title: Simulation and ghdl
type: post
status: publish
id: 380
tag: EE 668
tag: ghdl
tag: vlsi design lab
category: Programming
category: Technology and Engineering
~~~~

**\`\`To leave error unrefuted is to encourage intellectual
immorality.\`\`** Karl Marx.

quoted in 'The Poverty Of Theory' by E. P. Thompson. The only Western
Historian who could think beyond the nations of Atlantis.

 

Simulation
----------

An engineer should be able to not only correct an error but also locate
them. Simulation is mostly used for these two puposes. Failure in
detecting errors could be very costly. Later you detect it, costlier it
gets. Intel has witnessed it once. It may be not a matter of life an
death but surely it can throw a mid-size design house out of business.
Big corporations can survive but it costs a lot. A minor
 [FDIV](//en.wikipedia.org/wiki/Pentium_FDIV_bug) bug in Intel Pentium
processor cost \$500 million.After you have implemented your design as
per given 'specifications', first task is to test whether it is giving
what was expected (verification). While designing, one might have taken
clues from on one's common sense in addition to what one knows for sure.
Simulation protect you from this common sense (or intuitions), same way
mathematics protect natural sciences from common senses of humans which
by the way hardly have anything in common 2. Studying social sciences is
beset with ills. There is no protection from 'common sense'. No wonder,
two economists seldom agree on anything.Simulation is a big part of
today design activity and consumes about 60-80% time. In VHDL, you will
create 'test benches'3 to test your design against certain set of test
inputs. For all these possible inputs, if output satisfies given 'truth
table' (or behavioral description) then the design is said to be
correct. One should test his/design for all possible faults which is not
possible for large enough input ports. One should catch error as early
as possible for cost grows exponentially with design stages . If design
is found faulty at later stages, you might loose your job (or get
transfered if in government job). In any case, it will be a blot on your
claim to be an engineer.Simulation's present is bright, future is surely
bleak 4 . VLSI has grown up in size tremendously. A modern chip has many
input combinations that one can possibly be tested in resonable amount
of time even though computer run faster than Chacha Cahudhary's brain.
To overcome this, what one generally does is to break a large design
into smaller one and simulate smaller parts. Most of simulation is done
for moderate size components like adder, multiplexer etc.There have been
tremendous growth in the area of formal verification (you can google it
if you like) but you can not do away with simulation, at least for next
6-7 decades. Reduced Binary decision diagrams (RBDD) and Kripke
Structures are very prominent tools these days. In the past, using
formal methods in practice seemed hopeless, only few crazy people stuck
to them. Recently, industries are trying out formal verification like Z
notation to document system properties more rigorously. Model checking
and theorem proving (on certain structures) are being plugged in to
complement more traditional one of simulation.

Making a case for GHDL
----------------------

Since I am 'lobbying' for ghdl, it is understood that I am heavily
baised and like electrons under bias my ideas will move in a certain
direction (towards supporting ghdl ).Why ghdl? I can give two arguments,
one is solely driven by my love for free softwares, second is put
forward my Prof M. P. Desai in his lecture. Free softwares (as defined
by [Richard R. Stallman](http://www.gnu.org/philosophy/free-sw.html))
allow one to understand how a particular software works by providing you
with its source code. That makes improvement as well as enhancement
faster. This is the right way of making this planet 'smarter'. Another
more effective way is by dumbing down the users by taking away their
rights to know that they are using. Adding a fancy Graphical User
Interface (GUI) may not necessarily translates into a better software.
We all have experiences with Microsoft Word!Second, according to Prof
Desai (quoting in spirit, not the exact words),

> I'll prefer giving 5 lacs more to someone who is an expert in free
> software rather than spending 10 lacs buying a license of a propriety
> softwares given that my job is done. Its like preferring a musician
> who is better trained with his instruments over someone who is backed
> by costly electronic gadgets.

First argument is a truism given that one is suffering from the mental
necessity 'to know' like http://www-cs-faculty.stanford.edu/ uno/Donald
E. Knuth; second is also a truism if one works with (for) people who
have the same vision. But most of the time, this is not the case. Only
first rate mind appreciate first rate minds. N'th level mediocrity
always support N+1'th level mediocrity. So it should not be surprising
to note that most of the people prefer Madona over Pt. Ravishankar,
Daniel Steele over R. K. Narayanan, T-Shirt over Kurta - I plead guilty
(Albert Einstein would have looked more graceful in Kurta!) and 'some
Indian Idol' over Indian Ocean. On same lines, Modelsim over ghdl
(offense indented!). Bottom line is Your real skills (with
free-softwares) may be grossly undervalued (in propriety softwares
driven world). To survive in Industries, it is useful to have
familiarity with 'standard' tools. Internet is flooded with articles
about them.

Installing GHDL inside IITB
---------------------------

### Linux Users

### Before using package managers such as synaptic, yast etc make sure proxy variables are set. On Ubuntu, synaptic is installed by default. Go to , go to the and set the proxy. Search and mark for installation. If you prefer using utility from command line then make sure to put proxy information in file. For example, if my user-name is and password is then my file will look like this.

>      Acquire::http::proxy "http://prof_chaos:khooni_darinda@netmon.iitb.ac.in:80/"; Acquire::ftp::proxy "http://prof_chaos:khooni_darinda@netmon.iitb.ac.in:80/"; Acquire::https::proxy "http://prof_chaos:khooni_darinda@netmon.iitb.ac.in:80/";

    For other linux distribution, please google about it. If you are new to linux, you may not be able to get things right for first few hours. That suppose to happen, but don't let it put you off.

### Windows user

Guys! Learn linux if you have not started learning it. As someone has
said, \`\`We learn to live in the world of linux where there is no Gates
or Windows''. . For Modelsim student edition, you have to use windows as
expected. In VLSI lab, it is installed on linux and can be invoked by
command from terminal. Modelsim tutorial is given on its website.

Text Editor
-----------

**ghdl** now have an inbuilt text editor but it may not be available on
vlsi lab. You have to use or . is the most advanced and simple (as a
rule of thumb, takes quite a lot of practice to learn) text editor. is
also a good editor. Spend some time with vim every week. You can curse
me while learning but you will surely thank me after a year. is like a
light saber, it is only effective in the hand of a 'Jedi Knight'. First
timer can not do anything significant with it. has a lot of tutorial and
free books available on its website.

Coding
------

Get into habit of commenting your code properly. Not only because it
will be readable by others but also you can remember what you have done
a week ago. [Literate Programming](http://www.literateprogramming.com)
is a school of thought which deals with readability of codes. Writing
readable codes not only recommended but also mandatory these days. When
a team of many people works on a single project, non-readability consume
much more time then it saves.You make also like to read about subversion
(or git). Its a 'version control system' which keeps track of what you
have done in the past. You can easily recover any past version of your
file. You can use google-code to make your svn repository or can set up
your own local repository on your personal machine. There are many
[blogs](http://civicactions.com/blog/2010/may/25/how_set_svn_repository_7_simple_%20steps)
written about how to do it.

Few words of wisdom
-------------------

[![](http://dilawarnotes.files.wordpress.com/2011/01/ch940127.png "ch940127")](http://dilawarnotes.files.wordpress.com/2011/01/ch940127.png)

### About this document ...

Notes on GHDL and Simulation 1Prepared for EE 705 (VLSI design lab)
taken by Prof. Dinesh K. Sharma

Footnotes
=========

... Simulation1These notes have nothing to do with your course content.
Usual disclaimer of 'I am not responsible for any damages caused etc.
etc' applies.... common2As far as common sense is concerned, it make
sense asking whether an electron is a wave or a particle. For
mathematics, this question in itself is absurd. An electron is what its
equation implies, nothing less, yet could be more than that....
benches'3While using ghdl you have to write test bench in vhdl only, in
Modelsim you have another option called do files... bleak4I'm Done
Simulating; Now What? Verification Coverage Analysis and Correctness
Checking of the DECchip 21164 Alpha microprocessor; Michael Kantrowitz,
Lisa M.
Noack;[http://ieeexplore.ieee.org/iel3/3826/11178/00545595.pdf?arnumber=545595](http://ieeexplore.ieee.org/iel3/3826/11178/00545595.pdf?arnumber=545595)
