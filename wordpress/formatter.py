#!/usr/bin/env python

"""formatter.py:  Format text

Last modified: Sat Dec 21, 2013  12:44AM

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

def formatWithNoChangeOnTag(txt, tag) :
    ''' Notice :
    '''
    newText = ""
    bTag = False 
    eTag = True
    beginTag = re.compile("[\<\[]\s*"+tag+"\s*(\w+\s*=\s*[\"\w\']+\s*)?[\>\]]",
        re.IGNORECASE)
    endTag = re.compile("[\<\[]\s*\/"+tag+"\s*[\>\]]", re.IGNORECASE)
    for line in txt.split("\n") :
      if len(line.strip()) == 0 : continue 
      if beginTag.search(line) and endTag.search(line) : newText += line
      else : 
        if beginTag.search(line) :
          newText += "\n"
          bTag = True
          eTag = False
        if endTag.search(line) :
          eTag = True
          bTag = False
      #check 
      if bTag is True and eTag is False:
        newText += (line+"+QUQ+")
      else : # format it 
        newText += (line.strip()+"\n")
    return newText

def titleToFileName(title) :
    global blogDir
    fileName = title.replace(" ","_")+".blog"
    fileName = fileName.replace("/", "_")
    fileName = os.path.abspath(blogDir+"/"+fileName)
    return fileName

def contentToHTML(content):
    """Convert content to html
    """
    return content

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
