import re
text="Python is super super super super easy"
regex=r"super"
data=re.findall(regex,text)
print(data)