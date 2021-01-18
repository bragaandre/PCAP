####LAB: Collatz's hypothesis

c0 = int(input("Enter a number to be calculated ->"))
counter=1

if c0 >= 0:
    while c0 != 1:
        if(c0 % 2) == 0:
            c0 = c0 / 2
            counter += 1
            print(int(c0))
        else:
            c0 = (3*c0) + 1
            counter += 1
            print(int(c0))

    print("Steps = ", counter)

else:
    print("That's not a valid number(>=0)")
