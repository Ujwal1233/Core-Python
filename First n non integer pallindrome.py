def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return original == reverse


n = int(input("Enter value of n: "))

count = 0
num = 1

print("First", n, "non-palindrome numbers are:")

while count < n:
    if not is_palindrome(num):   # condition changed
        print(num, end=" ")
        count += 1
    num += 1