import re 

with open("../dilawarnotesDOTwordpressDOTcom/Hangman_game_in_Haskell.blog", "r") as f :
 txt = f.read()

def formatWithNotChangeOnTag(txt, tag) :
  newText = ""
  beginPre = False 
  endPre = True
  preRegex = re.compile("\<"+tag+"\>")
  endPreRegex = re.compile("\<\/"+tag+"pre\>")
  for line in txt.split("\n") :
    if len(line.strip()) == 0 : continue 
    if preRegex.search(line) and endPreRegex.search(line) : continue
    else : 
      if preRegex.search(line) :
        beginPre = True
        endPre = False
      if re.search(r"\<\/pre\>", line) :
        endPre = True
        beginPre = False
    #check 
    if beginPre is True and endPre is False:
      newText += (line+"\n")
    else : # format it 
      newText += (line.strip()+" ")
  return newText

