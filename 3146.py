###3.1.4.6 LAB: The basics of lists###

hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

print("This is the list:", hatList)

number = int(input("Enter a number to put in the middle:"))

hatList[2] = number #Step1

del hatList[4]# Step 2: write a line of code here that removes the last element from the list.

print(len(hatList))# Step 3: write a line of code here that prints the length of the existing list.

print(hatList)
