# Function to check Armstrong number
def is_armstrong(num):
    digits = len(str(num))
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == num


n = int(input("Enter how many Armstrong numbers you want: "))

count = 0
num = 1

print("First", n, "Armstrong numbers are:")

while count < n:
    if is_armstrong(num):
        print(num, end=" ")
        count += 1
    num += 1