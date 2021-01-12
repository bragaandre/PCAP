####3.1.1.13 LAB###


year = int(input("Enter a year: "))

if year >= 1582:
    if year % 4:
        print("Common Year")
    else:
        print("Leap  Year")
else:
    print("Not within the Gregorian calendar period")
