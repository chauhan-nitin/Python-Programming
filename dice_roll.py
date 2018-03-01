#Python function named play_one()
import random as r
def play_one():
    result = []
    x=2
    a=r.randint(1,6)
    result.append(a)
    b=r.randint(1,6)
    result.append(b)
    while a+b!=12:
        a=b
        b=r.randint(1,6)
        x+=1
        result.append(b)
    print("\nResult of Each Throw:",result)
    print("Total number of throws",x)
    print("Game Ends!!")
    return x

play_one()

#Python function named play_many(n)
def play_many(n):
    s = []
    total = 0
    for i in range(1,n+1):
        p= play_one()
        s.append(p)
    min1 = min(s)
    max1 = max(s)
    l = len(s)
    for i in range(0,l):
        total+=s[i]
    mean = int(total/n)
    print("\nTotal Number of Throws each time",s)
    print("\n{0}:min {1}:max {2}:mean".format(min1,max1,mean))

n = int(input("\nPlease Enter number of iterations n:\t"))
play_many(n)

