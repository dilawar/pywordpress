import re 

with open("../dilawarnotesDOTwordpressDOTcom/Attachment_missing_warning_with_mutt.blog", "r") as f :
 txt1 = f.read()
with open("../dilawarnotesDOTwordpressDOTcom/Hangman_game_in_Haskell.blog", "r") as ff :
  txt2 = ff.read()

def formatWithNoChangeOnTag(txt, tag) :
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

txt1 = formatWithNoChangeOnTag(txt1, "sourcecode")
txt1 = formatWithNoChangeOnTag(txt1, "pre")
print txt1.replace("+QUQ+", "\n")
