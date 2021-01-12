## 3.1.1.9 Making Decisions on Python

print("-This Program will tell you the bigger number-")

#read two numbers

number1 = int(input("Enter the first number->"))
number2 = int(input("Enter the second number->"))

#choose the larger number

if number1 > number2:larger_number = number1
else:larger_number = number2

#print the result

print("The larger number is:", larger_number)


print("Second Part of the program - MAX test")
## add 3 numbers
number1 = int(input("Enter the 1st number->"))
number2 = int(input("Enter the 2nd number->"))
number3 = int(input("Enter the 3rd number->"))

largest_number = max(number1, number2, number3)

print("The largest number is:", largest_number)
#end program
