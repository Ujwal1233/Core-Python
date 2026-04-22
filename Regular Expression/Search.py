import re
text="Python is super super super easy"
regex=r"super"
data=re.search(regex,text)
print(data)