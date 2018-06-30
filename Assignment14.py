
#question1
import re
emails='''"zuck26@facebook.com" "page33@google.com"
"jeff42@amazon.com"'''
userid=re.findall('[a-z0-9]+',emails)
print(userid)

#question2
import re
text ="Betty bought a bit of butter,But the butter was so bitter,so she bought some better butter,To make the bitter butter better."
words=re.findall('[bB][a-z]*',text)
print(words)

#question3
import re
text=''' "A,very very;irregular_sentence"'''
words=re.sub(r'[,;_\s]',' ',text)
print(words)
