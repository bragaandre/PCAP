####3.1.2.9 LAB: The break statement - Stuck in a loop

secret_word = "chupacabra"
word = ""

while word != secret_word:
    word = input("Enter the word to escape->")
    if word == "chupacabra":
        break

print("You escaped!")
