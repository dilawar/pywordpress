~~~~ 
title: Testing memories for faults
type: post
status: publish
id: 298
tag: ghdl
tag: Memory testing
tag: Pattern sensitive faults
tag: stuck at faults
tag: verification
tag: vhdl
category: Semiconductor Devices
category: Technology and Engineering
category: VLSI
~~~~

As the VLSI memories are shrinking in their size, the density of cells
which holds data is increasing exponentially. If one is making a living
out of manufacturing them then he must make sure product he is releasing
in the market is fault free. So he must hire some trained person to test
memories of how much they are faulty. **I wish I could do that with my
natural memory**. So at least he can make an informed decision whether
he should sell his faulty product. In memories many kind of faults can
occur. Most prominent of those are **stuck-at faults** (when some bit is
permanently stuck to 0 or 1 value); **coupling faults** (write in in one
location of memory can change the values at some other location), and
**Pattern Sensitive Faults** (a certain pattern in some locations of
memory will not allow to write at some address.) Another kind of faults
are **Decoder faults** in which decoder itself have some faults (thus
more than one addresses are mapped onto one address and any write will
write at multiple locations). Not all of these faults can be test by a
single test. Testing for all the faults are time consuming because they
are so many of them. However if certain combination of tests, will
limited yet sufficient coverage, does not detect faults in memory then
one can be pretty sure that this memory does not contain many faults
which are undetected. [See
this](http://digitalelectronics.blogspot.com/2009/01/memories-memory-faults-part-4.html)
Here in this post, We give some primitive tests  to detect these faults.
Lets say following is my memory block. [sourcecode language="text"]
entity MemBlock is generic(has\_decoder\_fault, has\_stuck\_at\_fault,
has\_psf, has\_cf: boolean := false); port(addr, data\_in: in
bit\_vector(7 downto 0); read\_en, write\_en: in bit; data\_out: out
bit\_vector(7 downto 0)); end entity; architecture Behave of MemBlock is
type MemArray is array (natural range \<\>) of bit\_vector(7 downto 0);
-- procedure that models the update of the memory array, -- given an
incoming word (data\_in) and a row index (I) procedure
Update\_Mem(signal mem\_array: inout MemArray;I: in integer; data\_in:
in bit\_vector(7 downto 0)) is variable cword: bit\_vector(7 downto 0);
variable uI, dI: integer; variable aflag : boolean; -- set true when
write is over. begin aflag := false; -- PSF if(I = 128 and has\_psf)
then uI := 129; dI := 127; cword := mem\_array(I); for J in 7 downto 0
loop -- here is the PSF if not ( mem\_array(uI)(J) = '1' and
mem\_array(dI)(J) = '1') then mem\_array(I)(J) \<= data\_in(J); end if;
end loop; aflag := true; end if; if(I=127 and has\_cf) then
if(mem\_array(127)(0) = '0' and data\_in(0) = '1') then
mem\_array(128)(0) \<= '1'; end if; mem\_array(127) \<= data\_in; aflag
:= true; end if; if(I=129 and has\_cf) then if(mem\_array(129)(0) = '0'
and data\_in(0) = '1') then mem\_array(128)(0) \<= '0'; end if;
mem\_array(129) \<= data\_in; aflag := true; end if; if(not aflag) then
mem\_array(I) \<= data\_in; end if; if(has\_stuck\_at\_fault) then
mem\_array(129)(0) \<= '1'; mem\_array(128)(0) \<= '0'; end if; end
procedure; -- converts bit vector to a natural number function
To\_Natural(x: bit\_vector) return natural is variable ret\_var :
natural := 0; alias lx: bit\_vector(x'length downto 1) is x; begin for I
in 1 to lx'length loop if(lx(I) = '1') then ret\_var := ret\_var +
(2\*\*(I-1)); end if; end loop; return(ret\_var); end To\_Natural; --
output of the decoder signal decode\_sig: bit\_vector(255 downto 0); --
memory array signal mem\_array: MemArray(0 to 255); begin -- decoder
process process(addr) begin decode\_sig \<= (others =\> '0'); for I in 0
to 255 loop if(I=To\_Natural(addr)) then decode\_sig(I) \<= '1';
if(I=128 and has\_decoder\_fault) then decode\_sig(I+1) \<= '1'; end if;
end if; end loop; end process; -- memory array access process
process(addr, data\_in, read\_en, write\_en) variable data\_out\_var:
bit\_vector(7 downto 0); begin data\_out\_var := (others =\> '0'); for I
in 0 to 255 loop if decode\_sig(I) = '1' then if(read\_en = '1') then
data\_out\_var := data\_out\_var or mem\_array(I); -- Wired OR elsif
write\_en = '1' then Update\_Mem(mem\_array,I,data\_in); end if; end if;
end loop; data\_out \<= data\_out\_var; end process; end Behave;
[/sourcecode] Now here is another file which instantiate these memory
blocks with faults in it. [sourcecode language="text"] entity MemTest is
end entity MemTest; architecture Behave of MemTest is -- utility
function: to increment an address function Increment(x: bit\_vector)
return bit\_vector is alias lx: bit\_vector(1 to x'length) is x;
variable ret\_var: bit\_vector(1 to x'length); variable carry: bit;
begin carry := '1'; for I in x'length downto 1 loop ret\_var(I) := lx(I)
xor carry; carry := carry and lx(I); end loop; return(ret\_var); end
Increment; signal addr, data\_in, data\_out\_df, data\_out\_saf,
data\_out\_psf,data\_out\_cf : bit\_vector(7 downto 0); signal read\_en,
write\_en: bit; -- memory block -- array of 8 bit words, with 8 bit
address. -- with the following behaviour. -- -- if read\_en = '1' then
-- data\_out = memory\_contents(addr); -- elsif write\_en = '1' then --
memory\_contents(addr) = data\_in; -- component MemBlock
generic(has\_decoder\_fault, has\_stuck\_at\_fault, has\_psf, has\_cf:
boolean := false); port(addr, data\_in: in bit\_vector(7 downto 0);
read\_en, write\_en: in bit; data\_out: out bit\_vector(7 downto 0));
end component; constant zero8: bit\_vector(7 downto 0) := (others =\>
'0'); -- utility procedures -- Write addr/data pair into memory using
write\_en procedure Write(signal addr: out bit\_vector(7 downto 0);
signal data: out bit\_vector(7 downto 0); signal write\_en: out bit;
addr\_var: in bit\_vector(7 downto 0); data\_var: in bit\_vector(7
downto 0)) is begin addr \<= addr\_var; data \<= data\_var; wait for 1
ns; write\_en \<= '1'; wait for 1 ns; write\_en \<= '0'; wait for 1 ns;
end procedure; -- Read data from memory using read\_en, addr. -- NOTE:
data must be present on data\_out signal on -- completion of procedure.
procedure Read(signal addr: out bit\_vector(7 downto 0); signal
read\_en: out bit; addr\_var: bit\_vector(7 downto 0)) is begin addr \<=
addr\_var; wait for 1 ns; read\_en \<= '1'; wait for 1 ns; read\_en \<=
'0'; end procedure; begin -- four memory blocks, each of which has one
type of fault in it. -- this has a decoder-fault mb\_df: MemBlock
generic map(has\_decoder\_fault =\> true, has\_stuck\_at\_fault =\>
false, has\_psf =\> false, has\_cf =\> false) port map(addr =\> addr,
data\_in =\> data\_in, data\_out =\> data\_out\_df, read\_en =\>
read\_en, write\_en =\> write\_en); -- this has stuck-at-faults in the
array mb\_saf: MemBlock generic map(has\_decoder\_fault =\> false,
has\_stuck\_at\_fault =\> true, has\_psf =\> false, has\_cf =\> false)
port map(addr =\> addr, data\_in =\> data\_in, data\_out =\>
data\_out\_saf, read\_en =\> read\_en, write\_en =\> write\_en); -- this
has a pattern-sensitive-fault in the array. The neighbourhood for the --
fault is adjacent bits in the same column of the array. mb\_psf:
MemBlock generic map(has\_decoder\_fault =\> false,
has\_stuck\_at\_fault =\> false, has\_psf =\> true, has\_cf =\> false)
port map(addr =\> addr, data\_in =\> data\_in, data\_out =\>
data\_out\_psf, read\_en =\> read\_en, write\_en =\> write\_en); -- this
has some coupling faults in the array mb\_cf: MemBlock generic
map(has\_decoder\_fault =\> false, has\_stuck\_at\_fault =\> false,
has\_psf =\> false, has\_cf =\> true) port map(addr =\> addr, data\_in
=\> data\_in, data\_out =\> data\_out\_cf, read\_en =\> read\_en,
write\_en =\> write\_en); ------------- test process
------------------------------------------------ process variable
curr\_addr, next\_addr: bit\_vector(7 downto 0); variable err\_flag :
boolean := false; begin
----------------------------------------------------------------------------------------
-- TEST SEQUENCE STARTS HERE
----------------------------------------------------------------------------------------
read\_en \<= '0'; write\_en \<= '0'; wait for 1 ns; curr\_addr :=
(others =\> '0'); while true loop -- write followed by read
Write(addr,data\_in,write\_en,curr\_addr,curr\_addr);
Read(addr,read\_en,curr\_addr); -- check data\_out assert (data\_out\_df
= curr\_addr) report "Data mismatch in memory with decoder fault"
severity ERROR; assert (data\_out\_saf = curr\_addr) report "Data
mismatch in memory with stuck-at-fault" severity ERROR; assert
(data\_out\_psf = curr\_addr) report "Data mismatch in memory with
pattern-sensitive-fault" severity ERROR; assert (data\_out\_cf =
curr\_addr) report "Data mismatch in memory with coupling-fault"
severity ERROR; err\_flag := err\_flag or (data\_out\_df /= curr\_addr)
or (data\_out\_saf /= curr\_addr) or (data\_out\_psf /= curr\_addr) or
(data\_out\_cf /= curr\_addr); next\_addr := Increment(addr);
if(next\_addr = zero8) then exit; end if; curr\_addr := next\_addr; end
loop;
----------------------------------------------------------------------------------------
-- TEST SEQUENCE ENDS HERE
----------------------------------------------------------------------------------------
assert not err\_flag report "Test Failed" severity ERROR; assert
err\_flag report "Test Passed" severity NOTE; wait; end process; end
Behave; [/sourcecode] **If you run the simulation using the algorithm in
this existing test bench, the memory block seems to be functioning
correctly. However, each of the memory blocks has faults present in it
(as you can verify by examining the VHDL code). Why did the test fail to
detect the errors? Now one needs to modify the test-bench to use a
single test (sequence of reads and writes) that can detect any
decoder/stuck-at/coupling/pattern-sensitive fault in MemBlock.
Pattern-sensitive faults may be assumed to be for a neighbourhood which
consists of adjacent bits in the same column of the 256x8 array. Conﬁrm
that this modiﬁed test-bench detects that each of the MemBlock instances
is faulty.** This was given as an assignment in *Verification and
Testing of VLSI* course offered by **Prof M. P. Desai** at IIT Bombay.
Attached is the detailed solution to this problem. We attach the VHDL
code which is my solution. However, in my solution, I make an assumption
that only adjacent cells can cause coupling/pattern sensitive/decoder
faults. In practice, situation is much worse than that. We have used
**ghdl** compiler to test it.
[solution\_memory\_testing](http://dilawarnotes.files.wordpress.com/2010/11/solution.pdf)
[sourcecode language="text"] use std.textio.all; entity MemTest is end
entity MemTest; architecture Behave of MemTest is -- utility function:
to increment an address function Increment(x: bit\_vector) return
bit\_vector is alias lx: bit\_vector(1 to x'length) is x; variable
ret\_var: bit\_vector(1 to x'length); variable carry: bit; begin carry
:= '1'; for I in x'length downto 1 loop ret\_var(I) := lx(I) xor carry;
carry := carry and lx(I); end loop; return(ret\_var); end Increment;
signal addr, addr2, data\_in, data\_out\_df, data\_out\_saf,
data\_out\_psf,data\_out\_cf : bit\_vector(7 downto 0); signal read\_en,
write\_en: bit; component MemBlock generic(has\_decoder\_fault,
has\_stuck\_at\_fault, has\_psf, has\_cf: boolean := false); port(addr,
data\_in: in bit\_vector(7 downto 0); read\_en, write\_en: in bit;
data\_out: out bit\_vector(7 downto 0)); end component; constant zero8:
bit\_vector(7 downto 0) := (others =\> '0'); -- utility procedures --
Write addr/data pair into memory using write\_en procedure Write(signal
addr: out bit\_vector(7 downto 0); signal data: out bit\_vector(7 downto
0); signal write\_en: out bit; addr\_var: in bit\_vector(7 downto 0);
data\_var: in bit\_vector(7 downto 0)) is begin addr \<= addr\_var; data
\<= data\_var; wait for 1 ns; write\_en \<= '1'; wait for 1 ns;
write\_en \<= '0'; wait for 1 ns; end procedure; -- Read data from
memory using read\_en, addr. -- NOTE: data must be present on data\_out
signal on -- completion of procedure. procedure Read(signal addr: out
bit\_vector(7 downto 0); signal read\_en: out bit; addr\_var:
bit\_vector(7 downto 0)) is begin addr \<= addr\_var; wait for 1 ns;
read\_en \<= '1'; wait for 1 ns; read\_en \<= '0'; end procedure; begin
-- four memory blocks, each of which has one type of fault in it. --
this has a decoder-fault mb\_df: MemBlock generic
map(has\_decoder\_fault =\> true, has\_stuck\_at\_fault =\> false,
has\_psf =\> false, has\_cf =\> false) port map(addr =\> addr, data\_in
=\> data\_in, data\_out =\> data\_out\_df, read\_en =\> read\_en,
write\_en =\> write\_en); -- this has stuck-at-faults in the array
mb\_saf: MemBlock generic map(has\_decoder\_fault =\> false,
has\_stuck\_at\_fault =\> true, has\_psf =\> false, has\_cf =\> false)
port map(addr =\> addr, data\_in =\> data\_in, data\_out =\>
data\_out\_saf, read\_en =\> read\_en, write\_en =\> write\_en); -- this
has a pattern-sensitive-fault in the array. The neighbourhood for the --
fault is adjacent bits in the same column of the array. mb\_psf:
MemBlock generic map(has\_decoder\_fault =\> false,
has\_stuck\_at\_fault =\> false, has\_psf =\> true, has\_cf =\> false)
port map(addr =\> addr, data\_in =\> data\_in, data\_out =\>
data\_out\_psf, read\_en =\> read\_en, write\_en =\> write\_en); -- this
has some coupling faults in the array mb\_cf: MemBlock generic
map(has\_decoder\_fault =\> false, has\_stuck\_at\_fault =\> false,
has\_psf =\> false, has\_cf =\> true) port map(addr =\> addr, data\_in
=\> data\_in, data\_out =\> data\_out\_cf, read\_en =\> read\_en,
write\_en =\> write\_en); ------------- test process
------------------------------------------------ process variable
curr\_addr, next\_addr, temp\_n\_addr, temp\_nn\_addr, temp\_data,
next\_data: bit\_vector(7 downto 0); variable err\_flag : boolean :=
false; variable err\_add, l\_psf, l\_df, l\_saf, l\_cf : line; begin
----------------------------------------------------------- -- TEST
SEQUENCE STARTS HERE
----------------------------------------------------------- read\_en \<=
'0'; write\_en \<= '0'; wait for 1 ns; curr\_addr := (others =\> '0');
while true loop ----------------------------------------------------- --
This test will test the stuck at 1/0 faults.
----------------------------------------------------- temp\_data :=
(others =\> '0'); next\_data := (others =\> '1'); -- test for s-a-1
faults. Write(addr, data\_in, write\_en, curr\_addr, temp\_data);
Read(addr, read\_en, curr\_addr); -- assert yourself. assert
(data\_out\_saf = temp\_data) report "Data mismatch in memory with
stuck-at-1-fault" severity ERROR; -- log this error. if data\_out\_saf
/= temp\_data then write(l\_saf, String'("A: ")); write(l\_saf,
curr\_addr); write(l\_saf, String'(" D: ")); write(l\_saf, temp\_data);
write(l\_saf, String'(" saf1: ")); write(l\_saf, data\_out\_saf);
writeline(output, l\_saf); end if; Write(addr, data\_in, write\_en,
curr\_addr, next\_data); Read(addr, read\_en, curr\_addr); -- assert
yourself. assert (data\_out\_saf = next\_data) report "Data mismatch in
memory with stuck-at-0-fault" severity ERROR; -- log this error. if
data\_out\_saf /= next\_data then write(l\_saf, String'("A: "));
write(l\_saf, curr\_addr); write(l\_saf, String'(" D: ")); write(l\_saf,
next\_data); write(l\_saf, String'(" saf0: ")); write(l\_saf,
data\_out\_saf); writeline(output, l\_saf); -- NOTE : Must reset this
cell while doing cf testing. Else -- problem might occur in first and
last cells. end if; -- while true loop temp\_data := (others =\> '0');
next\_data := (others =\> '1'); temp\_n\_addr := Increment(curr\_addr);
-- reset the cell we are going to test. Write(addr, data\_in, write\_en,
temp\_n\_addr, temp\_data); -- give an up-transition at left location
and read data. If there isa -- coupling faults. This should change the
value of cell from 0 to 1 Write(addr, data\_in, write\_en, curr\_addr,
temp\_data); Write(addr, data\_in, write\_en, curr\_addr, next\_data);
Read(addr, read\_en, temp\_n\_addr); -- read the next address. -- Assert
yourserf if you got it right. assert (data\_out\_cf = temp\_data) report
"Data mismatch in memory with coupling l\_at\_0\_u faults" severity
ERROR; -- log this error. if data\_out\_cf /= temp\_data then
write(l\_cf, String'("A: ")); write(l\_cf, temp\_n\_addr); write(l\_cf,
String'(" 0lu ")); write(l\_cf, data\_out\_cf); writeline(output,
l\_cf); -- reset the memory cell. Write(addr, data\_in, write\_en,
temp\_n\_addr, temp\_data); end if; -- give a low transition at left
location and read data. If there is a -- coupling fault then this should
change the value of cell from 0 to 1 Write(addr, data\_in, write\_en,
curr\_addr, temp\_data); Read(addr, read\_en, temp\_n\_addr); -- read
the next address. -- Assert yourserf if you got it right. assert
(data\_out\_cf = temp\_data) report "Data mismatch in memory with
coupling l\_at\_0\_d faults" severity ERROR; -- log this error. if
data\_out\_cf /= temp\_data then write(l\_cf, String'("A: "));
write(l\_cf, temp\_n\_addr); write(l\_cf, String'(" 0ld "));
write(l\_cf, data\_out\_cf); writeline(output, l\_cf); -- reset the
memory cell. Write(addr, data\_in, write\_en, temp\_n\_addr,
temp\_data); end if; -- REPEAT IT FROM RIGHT SIDE temp\_nn\_addr :=
Increment(temp\_n\_addr); -- give an up-transition at right location and
read data. If there isa -- coupling faults. This should change the value
of cell from 0 to 1 Write(addr, data\_in, write\_en, temp\_nn\_addr,
next\_data); Read(addr, read\_en, temp\_n\_addr); -- read the next
address. assert (data\_out\_cf = temp\_data) report "Data mismatch in
memory with coupling r\_at\_0\_u faults" severity ERROR; -- log this
error. if data\_out\_cf /= temp\_data then write(l\_cf, String'("A: "));
write(l\_cf, temp\_n\_addr); write(l\_cf, String'(" 0ru "));
write(l\_cf, data\_out\_cf); writeline(output, l\_cf); -- reset the
memory cell. Write(addr, data\_in, write\_en, temp\_n\_addr,
temp\_data); end if; -- give a low transition at right location and read
data. If there is a -- coupling fault then this should change the value
of cell from 0 to 1 Write(addr, data\_in, write\_en, temp\_nn\_addr,
temp\_data); Read(addr, read\_en, temp\_n\_addr); -- read the next
address. -- Assert yourserf if you are right. assert (data\_out\_cf =
temp\_data) report "Data mismatch in memory with coupling r\_at\_0\_d
faults" severity ERROR; -- log this error. if data\_out\_cf /=
temp\_data then write(l\_cf, String'("A: ")); write(l\_cf,
temp\_n\_addr); write(l\_cf, String'(" 0rd ")); write(l\_cf,
data\_out\_cf); writeline(output, l\_cf); -- reset the memory cell.
Write(addr, data\_in, write\_en, temp\_n\_addr, temp\_data); end if;
temp\_data := "00000000"; next\_data := "11111111"; temp\_n\_addr :=
Increment(curr\_addr); temp\_nn\_addr := Increment(temp\_n\_addr); --
Following line will write 1 in next adress. Write(addr, data\_in,
write\_en, temp\_n\_addr, next\_data); -- Give an up transition at left
location and read for fault. Write(addr, data\_in, write\_en,
curr\_addr, next\_data); Read(addr, read\_en, temp\_n\_addr); -- assert
it. assert (data\_out\_cf = next\_data) report "Data mismatch in memory
with coupling l\_at\_1\_u faults" severity ERROR; -- log this error. if
data\_out\_cf /= next\_data then write(l\_cf, String'("A: "));
write(l\_cf, temp\_n\_addr); write(l\_cf, String'(" 1lu "));
write(l\_cf, data\_out\_cf); -- reset the memory cell. Write(addr,
data\_in, write\_en, temp\_n\_addr, next\_data); end if; -- Give a down
transition at left location. And read for faults. Write(addr, data\_in,
write\_en, curr\_addr, temp\_data); Read(addr, read\_en, temp\_n\_addr);
-- Assert yourserf if you are right. assert (data\_out\_cf = next\_data)
report "Data mismatch in memory with coupling l\_at\_1\_d faults"
severity ERROR; -- log this error. if data\_out\_cf /= next\_data then
write(l\_cf, String'("A: ")); write(l\_cf, temp\_n\_addr); write(l\_cf,
String'(" 1lu ")); write(l\_cf, data\_out\_cf); -- reset the memory
cell. Write(addr, data\_in, write\_en, temp\_n\_addr, next\_data); end
if; -- Give an up transition at right location. Write(addr, data\_in,
write\_en, temp\_nn\_addr, next\_data); Read(addr, read\_en,
temp\_n\_addr); -- Assert yourserf if you are right. assert
(data\_out\_cf = next\_data) report "Data mismatch in memory with
coupling r\_at\_1\_u faults" severity ERROR; -- log this error. if
data\_out\_cf /= next\_data then write(l\_cf, String'("A: "));
write(l\_cf, temp\_n\_addr); write(l\_cf, String'(" 1ru "));
write(l\_cf, data\_out\_cf); writeline(output, l\_cf); -- reset the
memory cell. Write(addr, data\_in, write\_en, temp\_n\_addr,
next\_data); end if; -- Give a down transition at right location.
Write(addr, data\_in, write\_en, temp\_nn\_addr, temp\_data); Read(addr,
read\_en, temp\_n\_addr); -- Assert yourserf if you are right. assert
(data\_out\_cf = next\_data) report "Data mismatch in memory with
coupling r\_at\_1\_d faults" severity ERROR; -- log this error. if
data\_out\_cf /= next\_data then write(l\_cf, String'("A: "));
write(l\_cf, temp\_n\_addr); write(l\_cf, String'(" 1rd "));
write(l\_cf, data\_out\_cf); -- reset the memory cell. Write(addr,
data\_in, write\_en, temp\_n\_addr, next\_data); end if;
---------------------------------------------- -- Test pattern for
Pattern Sensitive Faults. ----------------------------------------------
temp\_data := (others =\> '0'); next\_data := (others =\> '1');
temp\_n\_addr := Increment(curr\_addr); temp\_nn\_addr :=
Increment(temp\_n\_addr); -- reset the cell we are going to test.
Write(addr, data\_in, write\_en, temp\_n\_addr, temp\_data); -------
case 1 -- Write 1 in left and 0 in right and check for PSF. Write(addr,
data\_in, write\_en, curr\_addr, next\_data); Write(addr, data\_in,
write\_en, temp\_nn\_addr, temp\_data); -- Now write 1 in the cell and
read the same value. Write(addr, data\_in, write\_en, temp\_n\_addr,
next\_data); Read(addr, read\_en, temp\_n\_addr); assert (data\_out\_psf
= next\_data) report "Data can not be written due to l1r0 PSF." severity
ERROR; -- log this error. if data\_out\_psf /= next\_data then
write(l\_psf, String'("A ")); write(l\_psf, temp\_n\_addr);
write(l\_psf, String'(" l1r0 ")); write(l\_psf, data\_out\_psf);
writeline(output, l\_psf); end if; -- write 0 in the cell and check for
the PSF. Write(addr, data\_in, write\_en, temp\_n\_addr, temp\_data);
Read(addr, read\_en, temp\_n\_addr); assert (data\_out\_psf =
temp\_data) report "Data can not be written due to l1r0 PSF." severity
ERROR; -- log this error. if data\_out\_psf /= temp\_data then
write(l\_psf, String'("A ")); write(l\_psf, temp\_n\_addr);
write(l\_psf, String'(" l1r0 ")); write(l\_psf, data\_out\_psf);
writeline(output, l\_psf); end if; -------- case 2 -- Write 1 in left
and 1 in right and check for PSF Write(addr, data\_in, write\_en,
curr\_addr, next\_data); Write(addr, data\_in, write\_en,
temp\_nn\_addr, next\_data); -- Now write 1 in the cell and read the
same value. Write(addr, data\_in, write\_en, temp\_n\_addr, next\_data);
Read(addr, read\_en, temp\_n\_addr); assert (data\_out\_psf =
next\_data) report "Data can not be written due to l1r1 PSF." severity
ERROR; -- log this error. if data\_out\_psf /= next\_data then
write(l\_psf, String'("A ")); write(l\_psf, temp\_n\_addr);
write(l\_psf, String'(" l1r1 ")); write(l\_psf, data\_out\_psf);
writeline(output, l\_psf); end if; -- write 0 in the cell and check for
the PSF. Write(addr, data\_in, write\_en, temp\_n\_addr, temp\_data);
Read(addr, read\_en, temp\_n\_addr); assert (data\_out\_psf =
temp\_data) report "Data can not be written due to l1r1 PSF." severity
ERROR; -- log this error. if data\_out\_psf /= temp\_data then
write(l\_psf, String'("A ")); write(l\_psf, temp\_n\_addr);
write(l\_psf, String'(" l1r1 ")); write(l\_psf, data\_out\_psf);
writeline(output, l\_psf); end if; -------- case 3 -- Write 0 in left
and 1 in right and check for PSF Write(addr, data\_in, write\_en,
curr\_addr, temp\_data); Write(addr, data\_in, write\_en,
temp\_nn\_addr, next\_data); -- Now write 1 in the cell and read the
same value. Write(addr, data\_in, write\_en, temp\_n\_addr, next\_data);
Read(addr, read\_en, temp\_n\_addr); assert (data\_out\_psf =
next\_data) report "Data can not be written due to l0r1 PSF." severity
ERROR; -- log this error. if data\_out\_psf /= next\_data then
write(l\_psf, String'("A ")); write(l\_psf, temp\_n\_addr);
write(l\_psf, String'(" l1r1 ")); write(l\_psf, data\_out\_psf);
writeline(output, l\_psf); end if; -- write 0 in the cell and check for
the PSF. Write(addr, data\_in, write\_en, temp\_n\_addr, temp\_data);
Read(addr, read\_en, temp\_n\_addr); assert (data\_out\_psf =
temp\_data) report "Data can not be written due to l0r1 PSF." severity
ERROR; -- log this error. if data\_out\_psf /= temp\_data then
write(l\_psf, String'("A ")); write(l\_psf, temp\_n\_addr);
write(l\_psf, String'(" l0r1 ")); write(l\_psf, data\_out\_psf);
writeline(output, l\_psf); end if; -------- case 4 -- Write 0 in left
and 0 in right and check for PSF Write(addr, data\_in, write\_en,
curr\_addr, temp\_data); Write(addr, data\_in, write\_en,
temp\_nn\_addr, temp\_data); -- Now write 1 in the cell and read the
same value. Write(addr, data\_in, write\_en, temp\_n\_addr, next\_data);
Read(addr, read\_en, temp\_n\_addr); assert (data\_out\_psf =
next\_data) report "Data can not be written due to l0r0 PSF." severity
ERROR; -- log this error. if data\_out\_psf /= next\_data then
write(l\_psf, String'("A ")); write(l\_psf, temp\_n\_addr);
write(l\_psf, String'(" l0r0 ")); write(l\_psf, data\_out\_psf);
writeline(output, l\_psf); end if; -- write 0 in the cell and check for
the PSF. Write(addr, data\_in, write\_en, temp\_n\_addr, temp\_data);
Read(addr, read\_en, temp\_n\_addr); assert (data\_out\_psf =
temp\_data) report "Data can not be written due to l0r0 PSF." severity
ERROR; -- log this error. if data\_out\_psf /= temp\_data then
write(l\_psf, String'("A ")); write(l\_psf, temp\_n\_addr);
write(l\_psf, String'(" l0r0 ")); write(l\_psf, data\_out\_psf);
writeline(output, l\_psf); end if; -------------------------------------
-- Decoder fault. ------------------------------------ -- NOTE : Ideally
one should write 0 to a cell and write 1 to -- all the cells which are 1
hamming distance away to cover all -- the stuck-at-fautls in decoder.
Here, we check immediate left -- and right cell for fautls. Write(addr,
data\_in, write\_en, temp\_n\_addr, next\_data); -- write all 1 in left
and right cell. Write(addr, data\_in, write\_en, curr\_addr,
temp\_data); Write(addr, data\_in, write\_en, temp\_nn\_addr,
temp\_data); Read(addr, read\_en, temp\_n\_addr); assert (data\_out\_df
= next\_data) report "Decoder fault - value written into some adjacent
cell." severity ERROR; -- log this error if data\_out\_df /= next\_data
then write(l\_df, String'("To ")); write(l\_df, temp\_n\_addr);
write(l\_df, String'(" From ")); write(l\_df, curr\_addr); write(l\_df,
String'(" DF ")); write(l\_df, data\_out\_df); writeline(output, l\_df);
-- reset cells for next test. Write(addr, data\_in, write\_en,
temp\_n\_addr, temp\_data); Write(addr, data\_in, write\_en,
temp\_nn\_addr, temp\_data); -- to make sure this does not interfere
with other test. Write(addr, data\_in, write\_en, curr\_addr,
temp\_data); end if; next\_addr := temp\_n\_addr; -- if all addresses
have been reached, exit if(next\_addr = "11111111") then exit; end if;
curr\_addr := next\_addr; end loop; assert false report "Test
completed." severity NOTE; wait; end process; end Behave; [/sourcecode]

Solution
--------

Use following commands to run the test. [sourcecode language="text"]
ghdl -i \*.vhd ghdl -m memtest ghdl -r memtest --stop-time=40ms
--vcd=dilawar.vcd [/sourcecode]
