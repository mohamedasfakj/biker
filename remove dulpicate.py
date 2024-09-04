size = int(input("Enter the size of the array: "))
words_array = [input(f"Enter word {i+1}: ") for i in range(size)]  
prev_word = "" 
for word in words_array:  
    if word != prev_word:  
        print(word, end=" ") 
    prev_word = word 