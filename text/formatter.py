import subprocess
import os 
import sys
import html2text 

# check if pandoc exists
panDoc = True
try:
    subprocess.call(["pandoc", '--version'], shell=False
            , stdout=subprocess.PIPE
            , stdin=subprocess.PIPE
            )
except OSError:
    panDoc = False
    
if not panDoc:
    import text.html2text as html2text
    import markdown 

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
        return content
    # else use inbuild html2text.py 
    else:
        h = html2text.HTML2Text()
        return h.handle(content)


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
        return content
    # Use markdown package to convert markdown to html
    else:
        return markdown.markdown(content)

def htmlToHtml(html):
    return html
