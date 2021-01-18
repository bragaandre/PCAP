### Module 3 - 3.1.2.3 LAB exercise #

secret_number = 777

n_in = 0 ###number input variable

print(
"""
+================================+

| Welcome to my game, muggle!    |

| Enter an integer number        |

| and guess what number I've     |

| picked for you.                |

| So, what is the secret number? |

+================================+
""")

while n_in != secret_number:
    print("Ha ha! You're stuck in my loop!")
    n_in = int(input("Enter a number to exit the maze! ->"))


print("Well done, muggle! You are free now.")
