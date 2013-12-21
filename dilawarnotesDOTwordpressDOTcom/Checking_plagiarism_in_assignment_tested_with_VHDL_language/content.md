~~~~ 
title: Checking plagiarism in assignment (tested with VHDL language)
type: post
status: publish
id: 548
tag: graph-tool python
tag: moodle
tag: plagiarism detection
tag: python scripts
tag: python-moodle
tag: similarity checking in vhdl codes
tag: similarity in codes
category: Graph Theory
category: Python
~~~~

I have developed some python scripts available
[here](https://github.com/dilawar/MyPublic/tree/master/MoodleIITB). I
have used them in EE705 (VHDL, verilog) and found them very useful. It
generates detailed log (which file matches which file) and sent emails
to offenders with an archive of all file which were matched. It is
integrated with my moodle-application (automatic download, extract,
compare, sending-emails.) It also generates graphs (using python
graph-tool) which shows the level of copying in the assignments. Few
graphs are attached in this post. Thickness of edge (and hotness of edge
color) shows the level of similarity. This gives a quite a picture of
the class. [caption id="attachment\_559" align="aligncenter" width="522"
caption="Graph shows suspects of plagiarism. Each edge represent a pair
of files containing significant matching. Edge thickness (and hotness of
color) is the amount of
similarity.[![](http://dilawarnotes.files.wordpress.com/2012/03/copy_all.png "copy_all")](http://dilawarnotes.files.wordpress.com/2012/03/copy_all.png)Similar
to previous one. But it shows the the level of interaction among
students. As usually heavy and red - edges shows significant copying
while light blue edges shows that fragments of text was similar (which
may shows the level of
discussion).[![](http://dilawarnotes.files.wordpress.com/2012/03/detailed.png "detailed")](http://dilawarnotes.files.wordpress.com/2012/03/detailed.png)This
is the dirty and detailed graph. It shows a overall interaction between
codes submitted by student. Many students have more than 1 file which
mathces (parallel
edge)"][![](http://dilawarnotes.files.wordpress.com/2012/03/copy_suspect.png "copy_suspect")](http://dilawarnotes.files.wordpress.com/2012/03/copy_suspect.png)[/caption]
