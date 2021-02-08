#### Fibonacci Sequence on the python ####



def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

limit = int(input("Fibonacci Sequence, please enter the number you want to reach->")) 

for n in range(1, limit+1): # testing
    print(n, "->", fib(n))
