#Python function named play_one()
import random as r
def play_one():
    result = []
    throw=2
    first=r.randint(1,6)
    result.append(first)
    second=r.randint(1,6)
    result.append(second)
    while first+second!=12:
        first=second
        second=r.randint(1,6)
        throw+=1
        result.append(second)
    print("\nResult of Each Throw:",result)
    print("Total number of throws",throw)
    print("Game Ends!!")
    return throw

play_one()

#Python function named play_many(n)
def play_many(n_it):
    #Empty list to hold values for each iteration of dice throws
    s = []
    sum_all = 0
    for i in range(1,n_it+1):
        p= play_one()
        s.append(p)
    min1 = min(s)
    max1 = max(s)
    s_len = len(s)
    for i in range(0,s_len):
        sum_all+=s[i]
    mean = int(sum_all/n_it)
    print("\nTotal Number of Throws each time",s)
    print("\nmin:{0},  max:{1}, mean:{2}".format(min1,max1,mean))

n_it = int(input("\nPlease Enter number of iterations n:\t"))
play_many(n_it)

