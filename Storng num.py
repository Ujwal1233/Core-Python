def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def is_strong(num):
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10

    return total == num


n = int(input("Enter number: "))
print("Strong" if is_strong(n) else "Not Strong")