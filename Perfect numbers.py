def is_perfect(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total == num


n = int(input("Enter number: "))
print("Perfect" if is_perfect(n) else "Not Perfect")