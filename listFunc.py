#####List Function 
#####

def list_sum(lst): ##Intro method: list_sum([x,y,x])
    s = 0
    for elem in lst:
        s += elem
    return s
def strangeListFunction(n):
    strangeList = []
    for i in range(0, n):
        strangeList.insert(0, i)
    return strangeList


print(strangeListFunction(5))

print(list_sum([4,5,6,7,10]))


