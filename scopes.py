###
###Scopes Exercises
###
def myFunction():
    global var ## This makes the variable ou of the function
    var = 2 
    print("Do I know that variable?", var)


var = 1
myFunction()

print(var)
