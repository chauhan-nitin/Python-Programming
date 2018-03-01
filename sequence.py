#Python function all_equal(s) return True if all elements in sequence 'S' are same as one another and False otherwise.
#Here the sequence can be described as [1,1,1] or [2,6] or [8,8,8,8] or [3]
def all_equal(S):
    #flagging variable to check whether Sequence elements are same or not
    flag=0

    #length of the sequence 'S'
    S_length = len(S)
    
    #Condition will be true if sequence 'S' has one or no element
    if (S_length==0)or (S_length==1):
        flag=1
    else:
        for digit in range(0,S_length-1):
            if S[digit]==S[digit+1]:
                flag=1
            else:
                flag=0
    #test condition for flagging variable to return final result
    if(flag==1):
        return("TRUE\n")
    else:
        return("FALSE\n")

#Calling the function with different trial of sequences inside print function
print(all_equal([1]))
print(all_equal([2,4,2]))
print(all_equal([2,2,2,2]))
print(all_equal([]))


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


#Python function named distinct(s) return the string formed from the first occurrence of each element in string 'S'.
def distinct(S):
    #empty string to hold first occurence of each element in string 'S'
    pos = ""
    for i in S:
        if i in pos:
            continue
        else:
            pos+=i
    return pos
#Creating a variable 'S' to hold the input string from the user
S = input("Enter any String  ")
print(distinct(S))


            
