import re
text="Python is easy"
regex=r"Python"
data=re.match(regex,text)
print(data)