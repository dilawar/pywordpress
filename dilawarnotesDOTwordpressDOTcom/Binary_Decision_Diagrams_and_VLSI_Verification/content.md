~~~~ 
title: Binary Decision Diagrams and VLSI Verification
type: post
status: publish
id: 303
tag: Binary decision diagrams
tag: kripke structure
tag: state machine
tag: verification
tag: verification of vlsi
category: Technology and Engineering
category: VLSI
~~~~

[in progress : I'll put up the solution after Nov 28. I have to submit
it as assignment so can not take the risk of being copied or so.] These
days simulation is the most prominent technique for verification.
However, simulation can only cover a part of all cases possible thus
simulation does not guarantee that certain properties will hold
everywhere in the system. For example, any complex asynchronous boolean
circuit with 100 variables will have 2^100^ combination. Not everyone
can afford verifying all these combination with computers using
simulation. Only a handful of companies like Intel can afford to do so
with thousands of C.P.U. running in parallel verifying a chip design or
testing a chip before sending it to foundry. If you are a smaller
company, then you have to make sure that you hire smart people who can
break down a larger problem into smaller one. Partitioning a large
system into smaller one is an art and requires a lot of experience and
eyes for details though there are few techniques available such as
expander graphs and matroids etc. A good techniques which widely used
these days is *temporal logic model checking*. In this method the system
being verified is modeled as **finite state transition system** and by
exhaustively exploring the model, we check whether property holds or
not. The biggest advantage using this is, if some property does not hold
on this system then a *witness* (counterexample) is produces. This helps
a lot in improving and correcting the design. Now we are going to
consider a real time example to show how to use this method. Consider
the following VHDL description of an state machine with two
architecture. This was given to us as an assignment at IIT Bombay by
Prof. M. P. Desai. I am not sure which of his Teaching Assistant wrote
it. Anyway this entity of **FSM** has two architecture, **one\_hot** and
**encode**. Our job is to verify that both of them are **equal** without
using the simulation. [sourcecode language="css"] -- entity fsm has two
architectures entity fsm is port (up, down: in bit; done: out bit;
clock: in bit; reset: in bit); end fsm; -- this is the first.
architecture one\_hot of fsm is signal state\_sig: bit\_vector(3 downto
0); begin process(clock,up,down,state\_sig) variable next\_state:
bit\_vector(3 downto 0); variable done\_var : bit; begin done\_var :=
'0'; if(reset = '1') then next\_state := (0 =\> '1', others =\> '0');
else if(up = '1') then -- rotate left by 1 next\_state := state\_sig(2
downto 0) & state\_sig(3); if(state\_sig(3) = '1') then done\_var :=
'1'; end if; elsif (down = '1') then -- rotate right by 1 next\_state :=
state\_sig(0) & state\_sig(3 downto 1); else next\_state := state\_sig;
end if; end if; done \<= done\_var; if(clock'event and clock = '1') then
state\_sig \<= next\_state; end if; end process; end one\_hot; -- this
is the second architecture encode of fsm is signal
state\_sig,state\_sig\_p1, state\_sig\_m1: bit\_vector(1 downto 0);
begin state\_sig\_p1(0) \<= not state\_sig(0); state\_sig\_p1(1) \<=
state\_sig(0) xor state\_sig(1); state\_sig\_m1(0) \<= not
state\_sig(0); state\_sig\_m1(1) \<= state\_sig(1) xor (not
state\_sig(0));
process(clock,up,down,state\_sig,state\_sig\_p1,state\_sig\_m1) variable
next\_state: bit\_vector(1 downto 0); variable done\_var : bit; begin
done\_var := '0'; if(reset = '1') then next\_state := (others =\> '0');
else if(up = '1') then next\_state := state\_sig\_p1; if(state\_sig(1) =
'1' and state\_sig(0) = '0') then done\_var := '1'; end if; elsif (down
= '1') then next\_state := state\_sig\_m1; else next\_state :=
state\_sig; end if; end if; done \<= done\_var; if(clock'event and clock
= '1') then state\_sig \<= next\_state; end if; end process; end encode;
[/sourcecode]
