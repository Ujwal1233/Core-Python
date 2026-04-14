def strDecreRev(s):
    nstr=" "
    for i in range(len(s)-1,-1,-1):
        nstr=nstr+s[i]  
    return nstr
s=input("Enter :")
print("Original String:",s)
res=strDecreRev(s)
print("Reverse String:",res)