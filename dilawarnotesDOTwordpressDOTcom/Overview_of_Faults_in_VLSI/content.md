~~~~ 
title: Overview of Faults in VLSI
type: post
status: publish
id: 69
category: Technology and Engineering
category: VLSI
~~~~

Someone who has access to market and someone who has access to capital
came up with an evil plan. They want to make a VLSI circuit and then
they will fabricate it and sell it to puny humans to make money [Evil
laugh]. What they want to create will surely depend on what their
consumers will find useful. So they hire someone who has expertise in
consumer electronics and pays her to figure out what they can sell to
them with some good profit. After doing her tricks, she gives them
certain **[product
requirements](http://en.wikipedia.org/wiki/Product_requirements_document).**Now
these product requirements are sent to us - the engineers. We try very
hard to concentrate on them and after some time under the influence of
burnt-out neurons, we are able to draw up **[specifications of VLSI
circuit](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=04644754).**These
specification usually describes the [behaviour of the circuit (e.g. in
VHDL,
Verilog).](http://www.people.vcu.edu/~rhklenke/tutorials/vhdl/modules/m12_23/sld006.htm)
Moreover, this specifications are embedded inside the model of the
environment in which this circuit suppose to work. For example, a chip
designed to work over Himalayas needs to be tested for temperature range
-20 to -50 degree centigrade, however if the targeted consumers are
normal lesser mortals working in their cozy rooms, these conditions of
negative temperature can be relaxed or dropped altogether. Now, my job
starts. Based on these specifications, I have to come up with a design.
Depending on the level of my experiences and expertise in design, I
refine my design over the time mostly by trial and error, and educated
guesses. During all these trials, errors, and educated guesses, I 'll
have my moment of genius which even I can not control.  Normally, all
these testing and designing are done with [T-CAD
tools](http://www.gnu.org/software/electric/). Ultimately I'll produce a
[**layout****](http://opencircuitdesign.com/magic/)of the circuit which
is to be manufactured. The layout then converted into [masks which are
used to
fabricate](http://www.google.com/url?sa=t&source=web&cd=2&ved=0CBcQFjAB&url=http%3A%2F%2Fwww-micro.deis.unibo.it%2F~masetti%2FDida01%2FtecCMOS.pdf&ei=tcKMTPeQEcL98AbA1Nm2Cw&usg=AFQjCNE_uwbDnnSLEtz17dpKB0TF5ZeCxQ&sig2=rcBxcuCWfQ4df57MsPE0Vw)this
circuit in a fabrication facility.

Testing, Verification and Validation
====================================

I do have trouble making distinction among these words but there are few
things which are different in them and are easy to see. Here, I define
these terms as defined by our Professor, [Madhav P.
Desai](http://www.ee.iitb.ac.in/wiki/faculty/madhav)during the course on
*Verification and Testing of VLSI Circuits*.

-   By testing, we normally refer to the process used to determine
    **that the manufactured circuit is functional**. Every manufactured
    circuit needs to be tested, and the result of the test should, with
    a **high degree of confidence**, determine that the circuit is
    functional.
-   By verification, we normally refer to the process used to confirm
    that **refinements in the design process are consistent with the
    circuit specification**. For example, when a logic circuit is
    implemented using transistors, we need to verify that the transistor
    network is equivalent to the logic circuit which it is supposed to
    implement. This is done at each refinement step in the design
    process.
-   By validation, we normally refer to the process used to confirm that
    a functional manufactured **circuit will fulfill the requirements**
    to which it was designed. This usually involves construction of a
    prototype and a test setup which mimics reality to the **maximum
    extent possible**.

After the fabrication, circuit must behave the way it was designed for,
else we have failed as engineers. However, since no process is fault
free, it could happen that the end product behave in unexpected ways. I
like to think of it as **this chip has developed a sense of humor.**Now
all these above mentioned processes can be utilized to remove this
**sense of humor**out of the chip to make it behave in boring and rigid
ways again. At the end of the day, it should work as it is told. **Humor
is the prerogative of Humans, machines must be humorless.**

Faults in VLSI
==============

Faults in VLSI can occur due to various reasons. Most prominent among
them is due to flaws and variation fabrication processes (when engineer
is competent). These causes of faults are discussed in [[Mally,
1987]](http://portal.acm.org/citation.cfm?id=37888.37914). Break in
metal lines, over and under deposition of material, alien particles in
fabrication process are the major sources of faults. As a designer, we
need to test these faults as early as possible. Later the fault is
located, costlier it gets by an order of magnitude (I do not have exact
numbers here). Following figure 1 shows a messed-up device fabricated by
me with the help of lab-staff during my M. Tech. Though it was useless
for us then, it is useful for us for our present discussion. [caption
id="attachment\_85" align="alignleft" width="570"][![Faults in
Fabrication](http://dilawarnotes.files.wordpress.com/2010/09/it_faults1.jpg "it_faults")](http://dilawarnotes.files.wordpress.com/2010/09/it_faults1.jpg)
Figure 1 : Faults in fabrication[/caption] [caption id="attachment\_77"
align="alignright"
width="364"]![](http://dilawarnotes.files.wordpress.com/2010/09/alien_particle_short.jpg "alien_particle_short")
Figure 2 : Alien particles during fabrication. Short of tacks.[/caption]
Figure 2 shows the alien particles causing the short. Extra deposition
and less deposition of materials cause most of the shorts and open
circuits problem. Figure 3 shows the less deposition of material causing
a track to be less conductive. Any logic propagated through this track
will be weaker than the perfect track. Figure 4 shows that in spite of
material deposition was sufficient, part of the track may still come off
due to less adhesion between the deposited material and the substance.
[caption id="attachment\_88" align="alignleft" width="289"][![Gold
liftoff from
Si](http://dilawarnotes.files.wordpress.com/2010/09/lift_off_gold_dot_on_si.png "lift_off_gold_dot_on_si")](http://dilawarnotes.files.wordpress.com/2010/09/lift_off_gold_dot_on_si.png)
Figure 4 : SEM image shows that gold may not stick very well to the Si
substrate. Same thing can happen with other pairs of material.[/caption]
[caption id="attachment\_78" align="alignleft"
width="50"][![](http://dilawarnotes.files.wordpress.com/2010/09/partial_broken_track.jpg "partial_broken_track")](http://dilawarnotes.files.wordpress.com/2010/09/partial_broken_track.jpg)
Figure 3 : Less materical deposition causing partial break in
track.[/caption] These faults, among others, are classified as spot
defects. Geometrically, these are randomly distributed over the entire
fabrication area. For more details on these faults we refer to [[Mally,
1987]](http://portal.acm.org/citation.cfm?id=37888.37914). To summarize,

-   Spot defects are regions of missing or extra material, (or
    drastically changed with physical material characteristics) that may
    occur in any layer of the fabricated IC.
-   These are expressed as number of defects per unit area. However,
    some defects such as oxide pinholes and substrate dislocation can be
    expressed in density only.
-   Cluster per unit area describes proneness of a region for defects.
    Distribution of defect size is also a prominent fault-matrix
    component.
-   Short is generally caused by extra material deposition at a spot of
    missing insulating material between two conductive tracks.
-   Break is generally caused by missing conductive material or extra
    insulating material in insulating windows.
-   Shorts and breaks occur both in horizontal and vertical direction.
    Since these days there are multi layer fabrication process are done
    in modern chip fabrication. Vertical shorts and breaks are as
    important as the horizontal one.

Fault Modeling
==============

Test Sequence Detectability
---------------------------

Let's make a gauge to measure how fault-free my circuit is. If I do a
test, can I answer this question. **What are the chances that a
successfully tested IC still contains undetected faults?
[^[FOOTNOTE]^](#f1)**Such is measure which one can name **test sequence
detectability,**\$latex D\$**.**It is defined as,

\$latex D = \\prod\_{i=1}\^{n\_e}(1-{p\_i})\$

where, \$latex p\_i\$ is the probability of the occurrence of faults
and  \$latex n\_e\$ are the faults that can not be detected by a given
test sequence. Well, defining it this make sense to me. If I can list
out all the possible faults that can occur in my circuit and their
number is \$latex n\$. Let assume that \$latex n\_f\$ is the number of
faults which I am testing my circuit for and let  \$latex n\_e\$ are the
faults which I can NOT detect during my test. Then, \$latex
\\frac{{n\_f} -{ n\_e}}{n\_f}\$ represent traditional fault coverage
and, of course, \$latex n \> n\_f\$. Hence an ultimate fault model must
list out all the possible faults with their probability of occurrence.
Practically, these faults model are based on the experience of an
Institute or company. [[Birolini,
1994]](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=784281&tag=1)
gives details about fault occurrence in VLSI circuits. Some figures are
given below.

  -------------------------- ------------- ------------ ------------------- ------------------
  **Components**             **Short %**   **Open %**   **Degradation %**   **Functional %**
  digital, bipolar ICs       30            30           10                  30
  digital MOS ICs            20            10           30                  40
  linear ICs                 30            10           10                  50
  bipolar transistors        70            20           10                  --
  field-effect transistors   80            10           10                  --
  -------------------------- ------------- ------------ ------------------- ------------------

Stuck at Models
===============

A traditional model is **stuck at model**.**In this model, one prescribe
to the lines in the logic representation on the IC either state '1' or
state '0' as permanent state. TODO : Give a brief overview. Meanwhile
readers can refer to a book by Kohavi.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
[BACK TO POST](#reff1) [1] . Naturally, one uses probabilistic models
while studying them.
