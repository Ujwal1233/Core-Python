# Function to check Armstrong
def is_armstrong(num):
    digits = len(str(num))
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10
    return sum == num
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))
print("Armstrong numbers in the given range are:")
for i in range(start, end + 1):
    if is_armstrong(i):
        print(i)