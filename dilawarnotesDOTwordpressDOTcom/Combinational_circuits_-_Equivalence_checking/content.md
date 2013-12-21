~~~~ 
title: Combinational circuits - Equivalence checking
type: post
status: publish
id: 253
tag: comparison of two circuits
tag: verification of vlsi
tag: vhdl
tag: vlsi
category: Electrical Network
category: Programming
category: VLSI
~~~~

Given a VLSI entity and its two description, establishing if both of
them are equivalent is fundamental problem in VLSI verification. In this
post, I am going to give describe an small part of this problem. Lets
say someone has provided us with an behavioral description of an entity.
For example lets say the given behavior of this entity is following.
[caption id="attachment\_255" align="aligncenter" width="326"
caption="a, b, c, and d are input to this entity and e is
output."][![](http://dilawarnotes.files.wordpress.com/2010/11/untitleddocument1.png "Cblock entity")](http://dilawarnotes.files.wordpress.com/2010/11/untitleddocument1.png)[/caption]
Lets say if \$latex a = 1\$ and \$latex b =1\$ then \$latex c = c
\\otimes d\$ and if \$latex a = 1\$ and \$latex b = 0\$ then \$latex e =
c \\bar{\\otimes} d\$. Otherwise, I don't give a damn! Ok! Now I have to
give a hardware description of this entity else no would care about it.
I give the following VHDL description (I hate verilog!). [sourcecode
language="text"] -- This is the entity entity Cblock is port(a,b,c,d: in
bit; e: out bit); end entity Cblock; -- this is the specification
architecture Behave of Cblock is begin process(a,b,c,d) begin if(a = '1'
and b = '1') then e &lt;= c xor d; elsif (a = '1' and b = '0') then e
\<= c xnor d; else end if; end process; end Behave; [/sourcecode] Next
task is to find an equivalent circuit description of this behavior. We
can surely use some synthesizer but they are not smart enough. Sometimes
they produce garbage (though this case is way too simple to make a
synthesizer go mad.). We are going to build our own. **We introduce one
more condition, say a, c, and d can never be same at any time. So we can
treat them as don't care condition.**Lets make the truth table of
Cblock. [caption id="attachment\_270" align="aligncenter" width="630"
caption="First table shows the truth table. Second shows truth table
after don't cares and third shows the minimization process. Note that
blue color is being overlapped by other one. We have three min terms
here."][![](http://dilawarnotes.files.wordpress.com/2010/11/truthtables.png "truthtables")](http://dilawarnotes.files.wordpress.com/2010/11/truthtables.png)[/caption]
After minimization, Cblock can be written as \$latex e = b
\\bar{c}\\bar{d} + abd + abc\$.  Notice that since \$latex a, c, d\$ are
not allowed to be same at any given time. We have  \$latex
\\bar{a}{b}\\bar{c}\\bar{d}\$, \$latex
\\bar{a}\\bar{b}\\bar{c}\\bar{d}\$, \$latex abdc\$, \$latex
{a}\\bar{b}{c}{d}\$ should not be taken into accout i.e. don't care
conditions.

### Build the circuit

Lets our life more miserable. We say that we have only **AND**and
**NOT**gates available. Can we realise the given function \$latex e\$.
Yes we can, remember that **AND**and **NOT**together represents
[**NAND**which is universal
gate](http://en.wikipedia.org/wiki/NAND_logic) and others gates can be
realised using it. Now we can construct the following circuit. [caption
id="attachment\_271" align="aligncenter" width="630" caption="Circuit
representing the function in
Qucs."][![](http://dilawarnotes.files.wordpress.com/2010/11/circuit.png "circuit")](http://dilawarnotes.files.wordpress.com/2010/11/circuit.png)[/caption]
This circuit can be simulated in any circuit simulator like **ngspice.**
If you are using **Qucs**than you can use the following file. Since I
can not attach this type of file, here is the code.

Verify both implementation
--------------------------

Now the final task to is to verify whether out implementation matches
with the given behaviour. To verify, I must check my implementation for
all the possible input combination and output must match the given
bahviorial description. We use **VHDL** to describe our implementation
and then we make a test-bench to verify it. Following is the code for
testbench. All entities are given in a single file. [sourcecode
language="text"] -- VHDL file for assignment 06. -- Dilawar Singh --
dilawar@ee.iitb.ac.in -- Modified from its original version. -- GHDL is
used to compile it. -- AND GATE entity And2 is port(a,b: in bit; c: out
bit); end entity And2; architecture Behave of And2 is begin c &lt;= a
and b; end Behave; -- Invertor entity Inv is port(a: in bit; b: out
bit); end entity Inv; architecture Behave of Inv is begin b &lt;= not a;
end Behave; -- This is the entity entity Cblock is port(a,b,c,d: in bit;
e: out bit); end entity Cblock; -- this is the specification
architecture Behave of Cblock is begin process(a,b,c,d) begin if(a = '1'
and b = '1') then e &lt;= c xor d; elsif (a = '1' and b = '0') then e
\<= c xnor d; else end if; end process; end Behave; -- this is the
implementation which you have to write. -- you may assume that the dont
care set is a=c=d architecture Impl of Cblock is component And2 is
port(a,b: in bit; c: out bit); end component; component Inv is port(a:
in bit; b: out bit); end component; -- fill in your implementation --
declare signals for interconnecting your gates signal i1\_out, i2\_out,
i3\_out, i4\_out, i5\_out, i6\_out, i7\_out, i8\_out : bit; signal
a1\_out, a2\_out, a3\_out, a4\_out, a5\_out, a6\_out : bit; begin --
fill in your implementation -- instantiate your gates. i1 : Inv port
map(a =\> c, b =\> i1\_out); i2 : Inv port map(a =\> d, b =\> i2\_out);
i3 : Inv port map(a =\> c, b =\> i3\_out); i4 : Inv port map(a =\> d, b
=\> i4\_out); i5 : Inv port map(a =\> a1\_out, b =\> i5\_out); i6 : Inv
port map(a =\> b, b =\> i6\_out); i7 : Inv port map(a =\> a4\_out, b =\>
i7\_out); i8 : Inv port map(a =\> a5\_out, b =\> i8\_out); i9 : Inv port
map(a =\> a6\_out, b =\> e); a1 : And2 port map(i1\_out, i2\_out,
a1\_out); a2 : And2 port map(a, b, a2\_out); a3 : And2 port map(i3\_out,
i4\_out, a3\_out); a4 : And2 port map(i5\_out, a2\_out, a4\_out); a5 :
And2 port map(i6\_out, a3\_out, a5\_out); a6 : And2 port map(i7\_out,
i8\_out, a6\_out); end Impl; entity Testbench is end entity Testbench;
-- testbench architecture Compare of Testbench is signal
a,b,c,d,eref,edut: bit; type bV2 is array(natural range \<\>) of
bit\_vector(3 downto 0); -- legal patterns. constant pattern: bV2(0 to
11) := ( ('0','0','0','1'), ('0','0','1','0'), ('0','0','1','1'),
('0','1','0','1'), ('0','1','1','0'), ('0','1','1','1'),
('1','0','0','0'), ('1','0','0','1'), ('1','0','1','0'),
('1','1','0','0'), ('1','1','0','1'), ('1','1','1','0')); component
Cblock is port(a,b,c,d: in bit; e: out bit); end component; for
ref:Cblock use entity work.Cblock(behave); for dut:Cblock use entity
work.Cblock(behave); -- use impl when ready begin ref: Cblock port
map(a=\>a,b=\>b,c=\>c,d=\>d,e=\>eref); -- change to implementation when
you have one ready dut: Cblock port
map(a=\>a,b=\>b,c=\>c,d=\>d,e=\>edut); process variable I : integer :=
0; begin while I &lt; 12 loop a &lt;= pattern(I)(3); b &lt;=
pattern(I)(2); c &lt;= pattern(I)(1); d &lt;= pattern(I)(0); I := I+1;
wait for 1 ns; assert(eref = edut) report "Mismatch between Reference
and DUT" severity error; end loop; assert false report &quot;Test
Over&quot; severity note; wait; end process; end Compare; [/sourcecode]

Results
-------

Now we have to run this testbench. There are few VHDL simulator
available, one is ghdl. We are going to use this. Make sure you can ghdl
installed. You can get it from[here](http://ghdl.free.fr/). Now we have
to run following commands. `$ghdl -a filename.vhd` `$ghdl -e testbench`
`$ghdl -r testbench --vcd=filename.vcd` Since my filename
was `dilawar.vhd` I got following output.
`dilawar.vhdl:118:8:@12ns:(assertion note):Test Over` Note that since we
have exhausted all the possible combination of inputs. This is not
possible in big circuits with a lot of inputs. Simulation is too slow to
handle all the cases. In future, we’ll be in need of better formal
verification tools. About that some other day. [caption
id="attachment\_287" align="aligncenter" width="630" caption="Waveform
of both of the implementation. Note that for given input combinations,
output is same. Thats is what an engineer establishes for
equivalence."][![](http://dilawarnotes.files.wordpress.com/2010/11/wave.png "wave")](http://dilawarnotes.files.wordpress.com/2010/11/wave.png)[/caption]
