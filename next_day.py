# Python function next.day(d,m,y)and returns next date
def next_day(d,m,y):
    leap = 0
    if (y%4 ==0) and (not y%100 ==0 or y%400 == 0):
        leap =1
    else:
        pass
    
    if d==31 and m==12:
        d=1
        m=1
        y+=1
    elif d==30 and (m==4 or m==6 or m==9 or m==11):
        d=1
        m+=1
    elif d==31:
        d=1
        m+=1
    elif (d==28 and leap==1):
        d+=1
    elif (d ==28 and m==2):
        d=1
        m+=1
    elif (d ==29 and leap==1 and m==2):
        d=1
        m+=1
    else:
        d+=1
    print("{0},{1},{2}".format(d,m,y))
    return 0

d = int(input("Enter the day\t"))
m = int(input("Enter the month\t"))
y = int(input("Enter the year\t"))
next_day(d,m,y)
