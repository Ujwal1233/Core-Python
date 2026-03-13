def fibonacci(pos,n1,n2):
    if pos<=0:
        return
    print(n1,end=" ")
    fibonacci((pos-1),n2,(n1+n2))    
pos=int(input("Enter a number:"))
fibonacci(pos,0,1)