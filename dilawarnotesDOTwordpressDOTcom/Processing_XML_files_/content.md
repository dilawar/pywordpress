~~~~ 
title: Processing XML files 
type: post
status: publish
id: 672
tag: Parsing XML
tag: XML and Java
category: Language
~~~~

XML files are a great way to store hierarchal information; so are the
databases. And with SQLITE3, you can embed the databases inside your
application. So which one to choose? Not at all easy to answer! This all
depends on what you need. If you have and embedded system, then having
sqlite will have so that you need not use XML parsing libraries (which
should be quite large vis a vis sqlite. Although I am not quite sure
about the sizes of various XML libraries.) It is recommended that when
XML files are small (upto 1-2 MB), they outperform any database. We can
parse XML and store it in memory. Searching this
in-memory-representation is much faster than querying databases. When
XML files are very large then we may consider using database such as
sqlite. For more discussion [see this
question](http://stackoverflow.com/questions/77726/xml-or-sqlite-when-to-drop-xml-for-a-database).
If we have chosen the XML to store our information, then we may also at
look the languages in which XMLs are relatively easy to handle. I found
JAVA (openjdk) to be very prolific with  XML. Have a look at XML-Schema
and how easy it is to parse an XML file to Java objects (it is easy once
you have become familiar with XML-Schema). There are some tools to
generate this schema automatically such
as[trang](http://www.thaiopensource.com/relaxng/trang.html) and to
generate JAVA classes automatically such as
[xjc](http://docs.oracle.com/cd/E17802_01/webservices/webservices/docs/1.6/jaxb/xjc.html).
But do not rely on these tools only. Learn to hand-code the schema.
It'll save to a lot of time later. If you need to search XML files, then
I'd recommend [XPath](http://www.w3.org/TR/xpath/). DOM is also good and
would beat XPath in terms of speed. DOM is lower level and should be
much faster than XPath. DOM and XPath are specifications and you need to
find a good implementation before comparing them. You should ask or
browse [stackoverflow.com](http://stackoverflow.com/)before making a
decision. Python is also a great candidate for parsing XML files. In
fact, Python is a very prolific language and if you are looking for an
easy and powerful language then Python is for you (Of course, no one can
beat C as far as performance is concerned).