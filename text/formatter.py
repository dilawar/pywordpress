import subprocess
import os 
import sys
import html2text 
import logging

# check if pandoc exists
panDoc = True
try:
    subprocess.call(["pandoc1", '--version'], shell=False
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
        h = html2text.HTML2Text()
        content = h.handle(decodeText(content))
        return content

def htmlToHtml(html):
    return decodeText(html)
