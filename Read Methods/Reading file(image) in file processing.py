fptr=open("Img.jpg.png","rb")
data=fptr.read()
fptr1=open("Img1.jpg.png","wb")
fptr1.write(data)
fptr.close()
fptr1.close()
print("Print the reference if img")


fptr=open("Img.jpg.png","rb")
data=fptr.read()
print(data)
for byte in data:
    print(format(byte,"08b"),end=" ")
