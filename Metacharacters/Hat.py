import re
text="a python is ython not pppython and pppppython"
regex=r"^n"
data=re.findall(regex,text)
print(data)