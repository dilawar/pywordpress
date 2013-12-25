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
        logging.debug("Using pandoc for markdown -> html")
        cmd = ["pandoc", "-f", "markdown", "-t", "html"]
        p = subprocess.Popen(cmd
                , stdin = subprocess.PIPE
                , stdout = subprocess.PIPE
                )
        p.stdin.write(content)
        content = p.communicate()[0]
        return decodeText(content)
    # else use inbuild html2text.py 
    else:
        logging.debug("Using python-markdown for html -> markdown")
        return markdown.markdown(decodeText(content))


def htmlToMarkdown(content, convertor='pandoc'):
    global panDoc
    if panDoc and convertor == 'pandoc':
        logging.debug("using pandoc for html -> markdown")
        cmd = ["pandoc", "-t", "markdown", "-f", "html"]
        p = subprocess.Popen(cmd
                , stdin = subprocess.PIPE
                , stdout = subprocess.PIPE
                )
        p.stdin.write(content)
        content = p.communicate()[0]
        return decodeText(content)
    # Use markdown package to convert markdown to html
    else:
        logging.debug("Using html2text for html -> markdown")
        printDebug("INFO", "html2text for html -> markdown")
        h = html2text.HTML2Text()
        content = h.handle(decodeText(content))
        return content
  
def titleToBlogDir(title):
    blogDir = title.replace(" ","_").replace(':', '-').replace('(', '')
    blogDir = blogDir.replace('/', '').replace('\\', '').replace('`', '')
    return blogDir

def titleToFilePath(title, blogDir):
    fileName = title.replace(" ","_").replace(':', '-').replace('(', '')
    fileName = fileName.replace("/", "_").replace(')', '')
    fileName = os.path.join(blogDir, fileName)
    return fileName
  

def htmlToHtml(html):
    return decodeText(html)

def metadataDict(txt):
    mdict = collections.defaultdict(list)
    md = getMetadata(txt)
    for c in ["title", "status", "id", "category", "tag"]:
        pat = re.compile(r'{0}:\s*(?<name>.+?)', re.INGNORECASE)
        m = pat.finall(txt)
        for i in m:
            mdict[c].append(i.group('name'))
    return mdict

def getMetadata(txt):
   """
   Get metadata out of a txt
   """
   pat = re.compile(r'~~~+(?P<metadata>.+?)~~~+', re.DOTALL)
   metadata = pat.search(txt).group('metadata')
   return metadata 

def getContent(txt):
    """ 
    Return only text of the post.
    """
    pat = re.compile(r'~~~+(?P<metadata>.+?)~~~+', re.DOTALL)
    return re.sub(pat, "", txt)


