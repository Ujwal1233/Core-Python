fptr=open("emp","rb")
data=fptr.read()
for byte in data:
    print(byte,end=" ")
for byte in data:
    print(format(byte,"08b"),end=" ")