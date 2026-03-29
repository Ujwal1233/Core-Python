# Function to check palindrome
def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    return original == reverse


# User input
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Palindrome numbers in the given range are:")

for i in range(start, end + 1):
    if is_palindrome(i):
        print(i, end=" ")