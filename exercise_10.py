import os
dict_word = {

}

def word_occur ():

    word = str(input("Enter a word: "))

    for num in word:
        if num in dict_word:
            dict_word[num] += 1
        else:
            dict_word[num] = 1

    print (f"Occurance of all characters in {word}: {str(dict_word)}")

os.system('cls')
word_occur()
            
        

