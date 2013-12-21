~~~~ 
title: A circuit containing multiplexer drawn using tikz (pgf)
type: post
status: publish
id: 576
tag: circuit drawing using pgf and tikz
tag: mux with tikz
tag: pgf
tag: tikz
category: Pgf (Tikz)
category: Technology and Engineering
~~~~

[caption id="attachment\_589" align="aligncenter"
width="640"][![](http://dilawarnotes.files.wordpress.com/2012/07/fig_circuit_mux.jpg "fig_circuit_mux")](http://dilawarnotes.files.wordpress.com/2012/07/fig_circuit_mux.jpg)
Circuit drawn using tikz[/caption] [sourcecode language="text"]
\\documentclass{article} \\usepackage{tikz,pgf}
\\usetikzlibrary{circuits.logic.US} \\usetikzlibrary{arrows}
\\begin{document} \\begin{figure}[h] \\begin{tikzpicture}[circuit logic
US] %% \\draw[help lines, draw, very thin, step=0.5cm, color=gray!20]
(0,-10) grid +(10,10); \\def\\mux { -- ++(0,-1) node [above right]
{\$1\$} -- ++(0.6,0.2) -- ++(0,0.6) -- ++(-0.6,0.2) -- cycle};
\\def\\muxr { -- node [below left] {\$1\$} ++(1,0) -- ++(-0.2,-0.6) --
++(-0.6,0) -- ++(-0.2,0.6) -- cycle}; % This node is data node. \\node
(data) [draw, dotted, minimum width=1.8cm, minimum height=4cm,
rectangle] at (0,-1.5) {}; \\foreach \\x / \\id in {0/0, 1.5/k, 3/31} {
% node represents one row. \\node (pb\\id) [draw, rectangle] at
(0,0-\\x) {PB[\\id]}; % node represents locationofNonZero element
function. \\node (lnz\\id) [draw, circle] at (2,0-\\x) {LNZ}; % node
represent and gate. \\node (and\\id) [and gate] at (3.5,0-\\x) {}; %
node represents isZero function. \\node (isZero\\id) [draw, circle] at
(5,0-\\x) {isZero}; % node represents mux. \\node (mux\\id) [] at
(7,-0.2-\\x) {}; \\draw[] (\$(isZero\\id)+(1.5,0.05)\$)\\mux; \\node
(zero\\id) [] at (6.0,-0.2-\\x) {\$0\$}; \\draw[-\>, style={-\>\>}]
(pb\\id.east) -- node[above right] {\$32\$} (lnz\\id.west); \\draw[-\>,
style={-\>\>}] (\$(pb\\id.east)+(0.5,0)\$) -- ++(0,-0.7) -- ++(5.45,0);
\\draw[-\>, style={-\>\>}] (lnz\\id.east) -- +(0.1,0) |- node[above
right] {} (and\\id.input 1); \\draw[-\>, style={-\>\>}] (and\\id.output)
node [above right] {\$32\$} -- (isZero\\id.west); \\draw[-\>,
style={-\>}] (isZero\\id.east) -- ++(0.3,0) -- ++(0.0,0.2) -|
(\$(mux\\id.north)+(-0.2,0.0)\$); \\draw[-\>, style={-\>\>}] (zero\\id)
-- (\$(mux\\id.west)+(-0.4,0)\$); }; \\node (e0) [rectangle] at (0,-0.5)
{\$\\vdots\$}; \\node (e0) [rectangle] at (0,-2.0) {\$\\vdots\$}; \\node
(xor) [minimum width=2cm, minimum height=4cm , rectangle, draw ] at
(9,-1.7) {XOR tree}; \\draw[-\>, style={-\>\>}]
(\$(mux0.east)+(0,-0.2)\$) -- ++(right:3mm) |- (\$(xor.west)+(0,1)\$);
\\draw[-\>, style={-\>\>}] (\$(muxk.east)+(0,-0.2)\$) -- ++(right:3mm)
|- (\$(xor.west)+(0,0)\$); \\draw[-\>, style={-\>\>}]
(\$(mux31.east)+(0,-0.2)\$ -- ++(0.5,0) |- (\$(xor.west)+(0,-1)\$);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %% section two of image
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \\node (rcrb) [draw,rectangle] at (0,
-4.8) {REDUCED\\\_CR}; \\node (muxb) [rectangle, minimum height=1cm] at
(\$(rcrb.west)+(2.5,-1.5)\$) {}; \\draw[]
(\$(rcrb.west)+(2.0,-1.0)\$)\\muxr; \\node (zerob) [ ] at
(\$(muxb)+(0.75,0.75)\$) {0}; \\node (xorb) [draw, circle] at
(\$(muxb)+(0,-1)\$) {\$+\$}; \\node (iszerob) [draw, circle] at
(\$(muxb)+(-2,0.2)\$) {isZero}; \\node (andb) [and gate, rotate=90] at
(\$(iszerob)+(0,-1.5)\$) {}; \\node (pbk) [draw, rectangle] at
(\$(xorb)+(1,-1)\$) {PB[k]}; \\node (lnzb) [draw, circle] at
(\$(andb)+(-0.1,-1.5)\$) {LNZ}; \\draw[-\>, style={-\>\>}] (rcrb.south)
-- +(0,-0.5) -| node[below left]{32} (\$(muxb.north)+(-.3,0)\$);
\\draw[-\>, style={-\>\>}] (\$(zerob.west)+(0,0)\$) ++(-0.1,0) -|
(\$(muxb.north)+(+.3,0)\$); \\draw[-\>, style={-\>\>}]
(\$(muxb.south)+(-0,0.4)\$) -- (xorb.north); \\draw[-\>, style={-\>\>}]
(xorb.east) -- ++(0.5,0) -| (pbk.north); \\draw[-\>, style={-}]
(xorb.west) -- ++(-0.5,0) |- (pbk.west); \\draw[-\>, style={-\>}]
(iszerob.east) -- (\$(muxb.west)+(-0.3,0.2)\$); \\draw[-\>,
style={-\>\>}] (lnzb.north) -- node[above left] {32} (andb.input 1);
\\draw[-\>, style={-\>\>}] (pbk.west) -| node [above right] {32}
(andb.input 2); \\draw[-\>, style={-\>\>}] (andb.output) --
(iszerob.south); %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %% section three of
image %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \\node (crc) [rectangle,
minimum width=2cm, draw] at (\$(rcrb)+(4,0)\$) {CR}; \\node (xorc)
[draw, circle] at (\$(crc)+(.5,-1.5)\$) {\$+\$}; \\node (rcrc) [draw,
rectangle] at (\$(xorc)+(0,-1)\$) {REDUCED\\\_CR}; \\node (iszeroc)
[draw, circle] at (\$(rcrc)+(0,-1.5)\$) {isZero}; \\node (muxc) [
minimum height=1cm, rectangle] at (\$(crc)+(3,-.5)\$) {}; \\draw[]
(\$(crc)+(2.5,-1)\$)\\mux; \\node (muxc) [ minimum height=1cm,
rectangle] at (\$(crc)+(3,-.5)\$) {}; \\node (pbc) [draw,rectangle] at
(\$(muxc)+(1.7,-1)\$) {PB[count+1]}; \\node (zeroc) [] at
(\$(muxc)+(-.9,-0.75)\$) {0}; \\draw[-\>, style={-\>\>}] (crc.west) --
++(-0.2,0) |- (and0.input 2); \\draw[-\>, style={-\>\>}] (crc.west) --
++(-0.2,0) |- (and31.input 2); \\draw[-\>, style={-\>\>}] (crc.west) --
++(-0.2,0) |- (andk.input 2); \\draw[-\>, style={-\>\>}] (rcrc.south)
+(-1.2,0) |- node[above, near end] {32} (lnzb.east); \\draw[-\>,
style={-\>\>}] (crc.south) -- +(0,-0.5) -| node[below right] {32}
(xorc.north); \\draw[-\>, style={-\>\>}] (xorc.south) -- (rcrc.north);
\\draw[-\>, style={-\>\>}] (rcrc.east) -- ++(0.2,0) |-
(\$(muxc.west)+(-0.4,-1.2)\$); \\draw[-\>, style={-\>\>}]
(\$(muxc.east)+(0,-1)\$) -- ++(0.2,0) |- (pbc.west); \\draw[-\>,
style={-\>\>}] (rcrc.south) -- (iszeroc.north); \\draw[-\>, style={-\>}]
(iszeroc.east) -| (\$(muxc.west)+(-0.1,-1.4)\$); \\draw[-\>,
style={-\>\>}] (zeroc.east) -- ++(0.2,0); \\draw[-\>, style={-\>\>}]
(xor.south) |- ++(-3.5,-1) |- node[below left] {32} (\$(xorc.east)\$);
\\end{tikzpicture} \\end{figure} \\end{document} [/sourcecode]
