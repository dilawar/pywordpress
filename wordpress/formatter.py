#!/usr/bin/env python

"""formatter.py:  Format text

Last modified: Fri Dec 20, 2013  11:33PM

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2013, NCBS Bangalore"
__credits__          = ["NCBS Bangalore", "Bhalla Lab"]
__license__          = "GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@iitb.ac.in"
__status__           = "Development"

import re

paragraphMark = "\nQQQQ\n"

def formatParagraph(paraTxt):
    if "<pre>" in paraTxt:
        return paraTxt
    if "[sourcecode" in paraTxt:
        return paraTxt
    pat = re.compile(r'\<h\d+\>(?P<text>.+)\<\/h\d+\>', re.DOTALL)
    m = pat.search(paraTxt)
    if m:
        paraTxt = re.sub(pat, ' ', paraTxt)
        headText = m.group('text')
        paraTxt = headText + '\n' + ''.join(['-' for x in headText]) + '\n' + paraTxt 
    paraTxt.replace("\n", "")
    newTxt = ""
    lenght = 0
    for c in paraTxt:
        newTxt += c
        lenght += 1
        if lenght > 80 and c == ' ':
            newTxt += '\n'
            lenght = 0
        else:pass
    return newTxt 



def formatContent(content):
    content = content.replace("&amp;", "")
    # Introduce paragraph marks in page.
    content = content.replace("<p>", paragraphMark)
    content = content.replace("</p>", paragraphMark)
    content = content.replace("[sourcecode", "%s[sourcecode" % paragraphMark)
    content = content.replace("[/sourcecode]", "[/sourcecode]%s\n" % paragraphMark)
    content = content.replace("<pre>", "%s<pre>\n" % paragraphMark)
    content = content.replace("</pre>", "\n</pre>%s\n" % paragraphMark)
    content = content.replace("<h" , "%s<h" % paragraphMark)
    contentList = [formatParagraph(x) for x in content.split(paragraphMark)]
    return "\n".join(contentList)

if __name__ == "__main__":
    with open("./dilawarnotesDOTwordpressDOTcom/Managing_music_using_mpd_mpc.blog") as f:
        txt = f.read()
    import re
    m = re.compile(r'<content>(.*)</content>', re.DOTALL | re.IGNORECASE)
    print formatContent(m.search(txt).group(1))
