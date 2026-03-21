def countdigits(n,count):
    if n<=0:
        return count
    n=n//10
    count=count+1
    return countdigits(n,count)
def isASN(n,pow,asn,temp):
    if n<=0:
        return asn==temp
    base=n%10
    asn=asn+(base**pow)
    n=n//10
    return isASN(n,pow,asn,temp)
num=int(input("Enter a num:"))
pow=countdigits(num,0)
flag=isASN(num,pow,0,num)
if flag:
    print(f"{num} is ASN")
else:
    print(f"{num} is Not an ASN")
