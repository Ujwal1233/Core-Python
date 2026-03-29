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


start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

armstrong_list = []
non_armstrong_list = []

for i in range(start, end + 1):
    if is_armstrong(i):
        armstrong_list.append(i)
    else:
        non_armstrong_list.append(i)

# Output
print("Armstrong Numbers:", armstrong_list)
print("Non-Armstrong Numbers:", non_armstrong_list)