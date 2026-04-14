def strIncreRev(s):
    nstr=" "
    for i in range(0,len(s)):
        nstr=s[i]+nstr  
    return nstr
def strIncreRevRec(s,nstr,i):
    if i>=len(s):
        return nstr
    nstr=s[i]+nstr
    return strIncreRevRec(s,nstr,(i+1))

s=input("Enter :")
print("Original String:",s)
res=strIncreRev(s)
print("Reverse String:",res)
res=strIncreRevRec(s," ",0)
print("Reverse String using Recursion:",res)