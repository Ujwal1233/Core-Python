import re
text="Python is super super super easy."
regex=r"is|super"
data=re.findall(regex,text)
print(data)