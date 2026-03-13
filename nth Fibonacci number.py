def nthfibnum(pos):
    if pos<=1:
        return pos
    return nthfibnum(pos-1)+nthfibnum(pos-2)
pos=int(input("Enter a position:"))
res=nthfibnum(pos)
print(f"The position of {pos} is {res}")