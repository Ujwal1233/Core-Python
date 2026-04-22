import re
text="a python is ython not pppython and pppppython"
regex=r"p{,2}ython"
data=re.findall(regex,text)
print(data)