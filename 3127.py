#####3.1.2.7 Loop control in Python | break and continue

# break - example

print("The break instruction:")

for i in range(1, 6):

    if i == 3:

        break

    print("Inside the loop.", i)

print("Outside the loop.")

# continue - example

print("\nThe continue instruction:")

for i in range(1, 6):

    if i == 3:

        continue

    print("Inside the loop.", i)

print("Outside the loop.")
