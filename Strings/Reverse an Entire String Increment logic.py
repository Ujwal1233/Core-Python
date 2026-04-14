def strIncreRev(s):
    nstr=" "
    for i in range(0,len(s)):
        nstr=s[i]+nstr  
    return nstr
s=input("Enter :")
print("Original String:",s)
res=strIncreRev(s)
print("Reverse String:",res)