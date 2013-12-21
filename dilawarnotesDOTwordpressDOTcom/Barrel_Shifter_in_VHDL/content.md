~~~~ 
title: Barrel Shifter in VHDL
type: post
status: draft
id: 413
category: Uncategorized
~~~~

Barrel Shifter is a combinational circuit which can rotate/shift any
number of bits in 'one operation'. Thus, this circuit is fastest
possible entity for rotation/shifting. A nice article about barrel
shifter is given
[here](http://answers.google.com/answers/threadview?id=388350). Please
read this before continuing. A great many tutorials and article are
available on the net. Some of the links are given in the previous link.
Here, we intend to do some math before the design. We may assume,
without the loss of generality, whatever we can say about right-shift is
also true for left shift. We also conclude that 'rotation' is nothing
but a composition of 'shifting operations'. For example, we have a
sequence \$latex ABCD\$
