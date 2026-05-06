#Remove the duplicate word from sentence without using inbuilt function and without using slicing
#input:"Rama is singing and Rama is dancing"
#output:"Rama is singing and dancing"
def remove_duplicate_words(sentence):
    words = []
    word = ""
    for ch in sentence:             
        if ch != " ":
            word = word + ch     
        else:
            if word != "":
                words = words + [word]   
                word = ""
    if word != "":                          
        words = words + [word]
    seen = {}
    unique_words = []
    for w in words:
        if w not in seen:
            seen[w] = True
            unique_words = unique_words + [w]
    result = ""
    first = True
    for w in unique_words:                  
        if first:
            result = w
            first = False
        else:
            result = result + " " + w
    return result
sentence = "Rama is singing and Rama is dancing"
print("Input :", sentence)
print("Output:", remove_duplicate_words(sentence))
