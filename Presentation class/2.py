#Reverse the sentences in a given string without using inbuilt function and without using slicing
#input:"Rama is singing"
#output:"singing is Rama"
def reverse_sentence(s):
    words = s.split()
    reversed_sentence = ""
    for word in words:
        reversed_sentence = word + " " + reversed_sentence
    return reversed_sentence.strip()
input_string = "Rama is singing"
reversed_string = reverse_sentence(input_string)
print(reversed_string)
