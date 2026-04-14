def strDecreRev(s):
    nstr=" "
    for i in range(len(s)-1,-1,-1):
        nstr=nstr+s[i]  
    return nstr
def strDecreRevRec(s,nstr,i):
    if i<0:
        return nstr
    nstr=nstr+s[i]
    return strDecreRevRec(s,nstr,(i-1))

s=input("Enter :")
print("Original String:",s)
res=strDecreRev(s)
print("Reverse String:",res)
res=strDecreRevRec(s," ",len(s)-1)
print("Reverse String using Recursion:",res)