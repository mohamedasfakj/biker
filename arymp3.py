#india nict


input_str = input("enter the string")  # "india nict"
words = input_str.split()  # "india", "nict"
max_vowel_word = ""# india
max_vowel_count = 0#3

for word in words: # india   nict
    vowel_count = 0
    for char in word:#n i  c t
        if char in 'aeiouAEIOU':#i
            vowel_count += 1   # 1
    if vowel_count > max_vowel_count:  # 3>1
        max_vowel_count = vowel_count # 3
        max_vowel_word = word#india

print("Word with max vowels:", max_vowel_word)