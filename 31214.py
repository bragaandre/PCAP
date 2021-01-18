###3.1.2.14 LAB: Essentials of the while loop


blocks = int(input("Enter the number of blocks: "))

i = 1 ### Number of layer

height = 0  ## Height aka number os lines

while i <= blocks:   
    blocks = blocks - i ##Construction of the line  
    i += 1 #Blocks needed
    height += 1 # Counter


print("The height of the pyramid:", height)
