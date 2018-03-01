#Python function all_equal(s) return True if all elements in sequence s the same as one another and False otherwise.
def all_equal(s):
    f=0
    l = len(s)
    if (l==0)or (l==1):
        f=1
    else:
        for i in range(0,l-1):
            if s[i]==s[i+1]:
                f=1
            else:
                f=0
    if(f==1):
        print("TRUE\n")
    else:
        print("FALSE\n")

all_equal([1])
all_equal([2,4,2])
all_equal([2,2,2,2])
all_equal([])

#Python function named all_pairs(s1,s2) Output, on separate lines, all pairs of elements from sequences s1 and s2, respectively,
#with the second element varying more rapidly than the first.
def all_pairs(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    for i in range(l1):
        for j in range(l2):
            print(str(s1[i])+s2[j])
            #print("{0} {1}".format(s1[i],s2[j]))

all_pairs([1,2],"abc")

#Python function named distinct(s) return the string formed from the first occurrence of each element in string s.
def distinct(s):
    pos = ""
    for i in s:
        if i in pos:
            continue
        else:
            pos+=i
    return pos
s = input("Enter any String  ")
print(distinct(s))


            
