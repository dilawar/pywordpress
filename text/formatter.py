import subprocess
import os 
import sys

def markdownToHtml(content, convertor='pandoc'):
    cmd = ["pandoc", "-f", "markdown", "-t", "html"]
    p = subprocess.Popen(cmd
            , stdin = subprocess.PIPE
            , stdout = subprocess.PIPE
            )
    p.stdin.write(content)
    content = p.communicate()[0]
    return content

def htmlToMarkdown(content, convertor='pandoc'):
    cmd = ["pandoc", "-t", "markdown", "-f", "html"]
    p = subprocess.Popen(cmd
            , stdin = subprocess.PIPE
            , stdout = subprocess.PIPE
            )
    p.stdin.write(content)
    content = p.communicate()[0]
    return content

def htmlToHtml(html):
    return html
