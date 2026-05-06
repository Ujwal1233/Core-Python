# Reverse a string without using inbuilt function and without using slicing
#input:"Rama"
#output:"amaR"
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
input_string = "Rama"
reversed_string = reverse_string(input_string)
print(reversed_string)
