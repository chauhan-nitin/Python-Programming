######################################################
#----------------------- QUESTION -------------------#
######################################################

#Save the provided insertion_sort and quick_sort in same folder as a6.py
import insertion_sort as in_sort
import quick_sort as q_sort
import sys

def quick_sort(lst):
    # Wrapper for GTG inplace quicksort
    q_sort.inplace_quick_sort(lst, 0, len(lst) - 1)

def insertion_sort(lst):
    #Wrapper for GTG inplace insertionsort
    in_sort.insertion_sort(lst)   

basketLength = 100
basketFinalLength = 1000
incrementBy = 25
minTimeIs = 0
maxTimeIs = 0
minTimeQs = 0
maxTimeQs = 0
avgTimeIs = 0
avgTimeQs = 0
bucketOflist = []
import random
import time

print("  n IS (min) IS (max) IS (ave) QS (min) QS (max) QS (ave) ")
print("-------------------------------------------------------------")

while basketLength <= basketFinalLength:
    accendinglist = list(range(1, basketLength))
    bucketOflist.append(accendinglist)
    decendinglist = list(reversed(range(1, basketLength)))
    bucketOflist.append(decendinglist)

    for ran in range(1,20):
        randomlist = random.sample(range(0, basketLength), basketLength)
        bucketOflist.append(randomlist)

    for oblist in bucketOflist:
        #print(oblist)
        currentTime = time.time()
        insertion_sort(oblist)
        afterTime = time.time()
        diffrenceTime = afterTime - currentTime
        if(diffrenceTime < minTimeIs or minTimeIs == 0):
            minTimeIs = diffrenceTime
        if(diffrenceTime > maxTimeIs):
            maxTimeIs = diffrenceTime
        avgTimeIs = avgTimeIs + diffrenceTime

        currentTime = time.time()
        quick_sort(oblist)
        sys.setrecursionlimit(1200)
        afterTime = time.time()
        diffrenceTime = afterTime - currentTime
        if(diffrenceTime < minTimeQs or minTimeQs == 0):
            minTimeQs = diffrenceTime
        if(diffrenceTime > maxTimeQs):
            maxTimeQs = diffrenceTime
        avgTimeQs = avgTimeQs + diffrenceTime

    avgTimeQs = avgTimeQs / len(bucketOflist)
    avgTimeIs = avgTimeIs / len(bucketOflist)
    

    print("" + str(basketLength) + " " + str(minTimeIs) +  " " + str(maxTimeIs) +  " " + str(avgTimeIs) +  " " + str(minTimeQs) +  " " + str(maxTimeQs) +  " " + str(avgTimeQs) +  " ")
    basketLength = basketLength + incrementBy

