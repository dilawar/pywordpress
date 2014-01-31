import subprocess
import re
import os 
import sys
import html2text 
import logging
import collections
from pyblog.colored_print import printDebug

# check if pandoc exists
panDoc = True
try:
    subprocess.call(["pandoc", '--version']
            , stdout=subprocess.PIPE
            , stdin=subprocess.PIPE
            )
except OSError:
    logging.debug("Pandoc not found")
    panDoc = False
    
if not panDoc:
    import text.html2text as html2text
    import markdown 

def decodeText(text):
    return text.decode('utf-8')

def markdownToHtml(content, convertor='pandoc'):
    global panDoc
    if panDoc:
        printDebug("DEBUG", "Using pandoc for markdown -> html")
        cmd = ["pandoc", "-s", "--highlight-styles", "--pygments"
                , "-f", "markdown+tex_math_dollars", "-t", "html"]
        p = subprocess.Popen(cmd
                , stdin = subprocess.PIPE
                , stdout = subprocess.PIPE
                )
        p.stdin.write(content)
        content = p.communicate()[0]
        return decodeText(content)
    # else use inbuild html2text.py 
    else:
        printDebug("DEBUG", "Using python-markdown for markdown -> html")
        return markdown.markdown(decodeText(content))


def htmlToMarkdown(content, convertor='pandoc'):
    global panDoc
    if panDoc and convertor == 'pandoc':
        logging.debug("using pandoc for html -> markdown")
        cmd = ["pandoc", "-t", "markdown+tex_math_dollars", "-f", "html"]
        p = subprocess.Popen(cmd
                , stdin = subprocess.PIPE
                , stdout = subprocess.PIPE
                )
        p.stdin.write(content)
        content = p.communicate()[0]
        return decodeText(content)
    # Use markdown package to convert markdown to html
    else:
        printDebug("INFO", "html2text for html -> markdown")
        h = html2text.HTML2Text()
        content = h.handle(decodeText(content))
        return content
  
def titleToBlogDir(title):
    if title is None:
        return ''
    if len(title.strip()) == 0:
        return ''
    blogDir = title.replace(" ","_").replace(':', '-').replace('(', '')
    blogDir = blogDir.replace('/', '').replace('\\', '').replace('`', '')
    blogDir = blogDir.replace(')', '').replace("'", '').replace('"', '')
    return blogDir

def titleToFilePath(title, blogDir):
    if len(blogDir.strip()) == 0:
        return ''
    fileName = os.path.join(blogDir, titleToBlogDir(title))
    return fileName
  

def htmlToHtml(html):
    return decodeText(html)

def metadataDict(txt):
    mdict = dict()
    md = getMetadata(txt)
    for c in ["title", 'type', "layout", "status", "id", "published"
                , "categories", "tags"]:
        pat = re.compile(r'{0}\s*:\s*(?P<name>.+)'.format(c), re.IGNORECASE)
        m = pat.search(txt)
        if m:
            mdict[c] = m.group('name')
    return mdict

def getMetadata(txt):
   """
   Get metadata out of a txt
   """
   if not "---" in txt:
       printDebug("ERROR", "The text does not contain any metadata header")
       print txt
       sys.exit(1)

   pat = re.compile(r'\-\-\-+(?P<metadata>.+?)\-\-\-+', re.DOTALL)
   m = pat.search(txt)
   if m:
       return m.group('metadata')
   else:
       printDebug("ERROR", "No metadata found in text")
       sys.exit(0)

def getContent(txt):
    """ 
    Return only text of the post.
    """
    pat = re.compile(r'\-\-\-+(?P<metadata>.+?)\-\-\-+', re.DOTALL)
    return re.sub(pat, "", txt)

def readInputFile(fileName):
    """
    read file and return its format. html or markdown
    """
    assert fileName
    if not os.path.exists(fileName):
        raise IOError, "File %s does not exists" % fileName

    # Check the fmt of file.
    fmt = os.path.splitext(fileName)[1].lower()
    if fmt in ["htm", "html", "xhtml"]:
        fmt = "html"
    elif fmt in ["md", "markdown"]:
        fmt = "markdown"
    else:
        fmt = "markdown"
    txt = open(fileName, 'r').read()   
    return (fmt, txt)

def formatContent(txt, fmt):
    """
    Format the content as per fmt.
    """
    content = getContent(txt)
    if fmt == "html":
        content = htmlToHtml(content)
    elif fmt == "markdown":
        content = markdownToHtml(content)
    else:
        printDebug("WARN", "Unsupported format %s " % fmt)
        printDebug("WARN", " - Assuming markdown")
        content = markdownToHtml(content)
    return content


