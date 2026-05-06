# Remove the duplicate a letter from a string without using inbuilt function and without using slicing
#input:"Hello"
#output:"Helo"
def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result
input_string = "Hello"
output_string = remove_duplicates(input_string)
print(output_string)
