import re 

with open("../dilawarnotesDOTwordpressDOTcom/Attachment_missing_warning_with_mutt.blog", "r") as f :
 txt = f.read()

def formatWithNotChangeOnTag(txt, tag) :
  newText = ""
  bTag = False 
  eTag = True
  beginTag = re.compile("[\<\[]\s*"+tag+"\s*(\w+\s*=\s*[\"\w\']+\s*)?[\>\]]",
      re.IGNORECASE)
  endTag = re.compile("[\<\]]\s*\/"+tag+"\s*[\>\]]", re.IGNORECASE)
  for line in txt.split("\n") :
    if len(line.strip()) == 0 : continue 
    if beginTag.search(line) and endTag.search(line) : continue
    else : 
      if beginTag.search(line) :
        print("source")
        bTag = True
        eTag = False
      if endTag.search(line) :
        eTag = True
        bTag = False
    #check 
    if bTag is True and eTag is False:
      newText += (line+"\n")
    else : # format it 
      newText += (line.strip()+" ")
  return newText

print formatWithNotChangeOnTag(txt, "sourcecode")
