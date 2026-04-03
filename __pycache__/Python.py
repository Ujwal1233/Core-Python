A=[[1,2,3],
   [4,5,6],
   [7,8,9]]
[A[i][len(A)-1-i]for i in range(len(A))]
A[2][3-1-2]
A[0][2]
A[1][1]
A[2][0]
a=[1,2,3]
b=a.append(4)
print(a)
print(b)


def fun():
    yield 1
    yield 2
    yield 3
    yield 4
res=fun()
print(res.__next__())
print(res.__next__())
for i in res:
    print(i)