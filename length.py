def find_string_length(input_string):
    length=0
    #for i in input_string:
    while input_string:
        input_string=input_string[1:]
        length+=1
    return length

input_string=input("enter string:")
length=find_string_length(input_string)
print("length of the string:",length)