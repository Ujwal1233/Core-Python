def rec_lcm(n,m,lcm):
    if lcm>m*n:
        return lcm
    if lcm%m==0 and lcm%n==0:
/        return lcm
    return rec_lcm(n,m,lcm+1)
data1=int(input("enter num "))
data2=int(input("enter num "))
lcm=max(data1,data2)
res=rec_lcm(data1,data2,lcm)
print(res)