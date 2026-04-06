from itertools import zip_longest
name=["kohli","dhoni","rohit","surya"]
Jnum=[18,7,45,9]
runs=(12000,10000,9000,8000)
team=["Rcb","Chennai","Mumbai","Sunrisers"]
players=list(zip_longest(name,Jnum,runs,team,fillvalue="#"))
print(players)