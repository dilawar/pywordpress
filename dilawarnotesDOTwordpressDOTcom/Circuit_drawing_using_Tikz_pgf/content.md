~~~~ 
title: Circuit drawing using Tikz (pgf)
type: post
status: publish
id: 482
tag: circuit drawing using pgf and tikz
tag: Electrical Circuits
tag: pgf
tag: tikz
category: Pgf (Tikz)
category: Programming
~~~~

[sourcecode language="latex"] \\begin{figure}[h]
\\usetikzlibrary[arrows] \\centering \\begin{tikzpicture}[circuit logic
US, minimum height=10mm] \\matrix[column sep=10mm] { \\node (i0)
{\$A\$}; & & & & \\\\ & \\node [xor gate] (xor1) {\$dev1\$}; &
\\node[xor gate] (xor2) {\$dev2\$}; & & \\\\ \\node (i1) {\$B\$}; & &
\\node (cin) {};&nbsp; & & \\node (o1) {\$S\$}; \\\\ & & \\node[and
gate] (and1) {\$dev3\$}; & & \\\\ \\node (i2) {\$C\_{in}\$}; & & &
\\node[or gate] (or1) {\$dev5\$};& \\node (o2) {\$C\$};\\\\ & &
\\node[and gate] (and2) {\$dev4\$}; & & \\\\ }; \\draw[\>-] (i0.east) --
++(right:3mm) |- (xor1.input 1); \\draw[\*-] (xor1.input 1)
++(-7mm,0.5mm) |- (and2.input 2); \\draw[\*-] (xor1.input 2)&nbsp;
++(-4mm,0.5mm) |- (and2.input 1); \\draw[\>-] (i1.east) -- ++(right:3mm)
|- (xor1.input 2); \\draw (xor1.output) -- ++(right:3mm) |- (xor2.input
1); \\draw[\*-] (and1.input 1) ++(-3mm,-0.5mm) |- (xor2.input 2);
\\draw[\>-] (i2.east) -- ++(right:15mm) |- (and1.input 1); \\draw[-\>]
(xor2.output) -- ++(right:3mm) |- (o1.west) ; \\draw (and1.output) --
++(right:3mm) |- (or1.input 1) node[midway, above right ] {\$e\$};
\\draw (and2.output) -- ++(right:3mm) |- (or1.input 2) node[midway,below
right] {\$f\$}; \\draw[-\>] (or1.output) -- (o2.west);
\\end{tikzpicture} \\caption{\\small A full adder.} \\end{figure}
[/sourcecode] Above code draws the circuit shown below. You have to use
\\usetikzlibrary{circuits.logic.US} in the preamble of latex document.
Also, make sure you have the recent version of texlive and you have
hashed the tex data-base using texhash if you have installed pgf as
standalone. Notice in the figure below that we have added a dot to
emphasis the connection. Usually this dot is drawn by using the arrow
which does not cover the wire. To put the dot on the wire, we shift the
starting point of arrow by ++ operator. Give it a try. You'll get to
know. NOTE : character '\>' may not be visible. It is used after
'\\draw'.  
[![](http://dilawarnotes.files.wordpress.com/2011/10/full_adder.png "full_adder")](http://dilawarnotes.files.wordpress.com/2011/10/full_adder.png)
 
