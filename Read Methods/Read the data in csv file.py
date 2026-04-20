import csv
print("Enter the filename")
fname=input()
fptr=open(fname,"r")
data=csv.reader(fptr)
for i in data:
    print((i[0]))