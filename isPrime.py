#### Is Prime Program ####
#### 4.1.3.9 LAB: Prime numbers - how to find them


def isPrime(num):
    if num <= 1:
        return False
    else:
      for i in range(2, num):
         # checking for factor
         if num % i == 0:
            return False
      # returning True
    return True



for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")

print()
