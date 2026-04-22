import re
text="Python is super super super super easy"
regex=r"."
data=re.findall(regex,text)
print(data)