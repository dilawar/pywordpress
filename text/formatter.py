import subprocess
import os 
import sys
import html2text 

# check if pandoc exists
panDoc = True
try:
    subprocess.call(["pandoc1", '--version'], shell=False
            , stdout=subprocess.PIPE
            , stdin=subprocess.PIPE
            )
except OSError:
    panDoc = False
    
if not panDoc:
    import text.html2text as html2text
    import markdown 

def decodeText(text):
    return text.decode('utf-8')

def markdownToHtml(content, convertor='pandoc'):
    global panDoc
    if panDoc:
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
        h = html2text.HTML2Text()
        content = h.handle(content)
        return decodeText(content)


def htmlToMarkdown(content, convertor='pandoc'):
    global panDoc
    if panDoc:
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
        return markdown.markdown(decodeText(content))

def htmlToHtml(html):
    return decodeText(html)
