import re
text="a python is ython not pppython and pppppython"
regex=r"[p]"
data=re.findall(regex,text)
print(data)
print("The length is",len(data))