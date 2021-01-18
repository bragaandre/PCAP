##Module 3 - 3.1.2.10 LAB: The continue statement - the Ugly Vowel Eater#

# Prompt the user to enter a word
# and assign it to the userWord variable.

Final_Word = ""

userWord = input("Input a word: ")

userWord = userWord.upper()


for letter in userWord:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        Final_Word += letter

print(Final_Word)

