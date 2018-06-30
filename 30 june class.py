#regular expression

import re
#
nameage="Abc is  18 years old"\
        "Xyz is 20 years  old"\
       " Mno is 22 years old"

names=re.findall(r'[A-Z][a-z]*',nameage)
print(names)

ages=re.findall('\d{1,3}',nameage)
print(ages)

email='''megha.ahuja177@gmail.com
          abc@gmail.com
          xyz@@gmail.com'''
match=re.findall("[\w.+$%_+-]{1,20}[@][\w]{1,20}[.][\w]{1,3}",email)
print(match)
#
a="hat cat rat mat"
regrex=re.compile("[m]at")
strr=regrex.sub("strr",a)
print(strr)



