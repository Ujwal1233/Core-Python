def isPalinArray(arr):
    # Code heredef isPalinArray(arr):
    for i in range(len(arr)):
        arrx = str(arr[i])
        if arrx != arrx[::-1]:
            return False
    return True
# Example usage:
print(isPalinArray([121, 131, 20]))  # Output: False