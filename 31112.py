###3.1.1.12 LAB
income = float(input("Enter the annual income:"))

## conditions

if income >= 85528.00:
    tax = 14839.02 + (income*0.32)
else:    
    tax = (income*0.18)-552.02


tax = round(tax, 0)

print("The tax is:", tax, "thalers")
