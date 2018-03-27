#-------------------------------------------------------------------------------------------------------#
#_____________________________________ QUESTION ____________________________________________________#
#-------------------------------------------------------------------------------------------------------#

#Python class definition for a priority queue container. named PriorityQueue with following functionality
#Class definition for implemented PriorityQueue
class PriorityQueue:
    #Creating an empty dictionary to hold keys:values
    list = {}

    #Code for constructor function __init__
    def __init__(self, item):
        self.__item = item

    #Code for function add_element(k,v)
    def add_element(self, k, v):
        val = [] #initializing list
        if k in self.list:
            val = self.list[k] #assigning dictionary items in val
            val.append(v) #assigning value for key items
            self.list[k] = val
        else:
            val.append(v)
            self.list[k] = val

    #Code for function length           
    def length(self):
        return len(self.list)

    #Code for function check_empty
    def check_empty(self):
        if not self.list:
            return True
        else:
            return False

    #Code for function minimum_element
    def minimum_element(self):
        min_ele = 0
        value = 0
        if len(self.list) != 0:
            min_ele = min(self.list.keys())
            value = self.list[min_ele]
            return min_ele , value
        else:
            return ("Empty Queue\n")

    #Code for function remove_element
    def remove_element(self):
        min_key = 0
        #minimum_value = 0
        if len(self.list) > 0:
            for key in self.list:
                min_key = min(self.list.keys())
                #min_value = min(self.items[min_key])
            return min_key, self.list.pop(min_key)
        else:
             print("No-items in Queue\n")
            return False

    #Code for function summary
    def summary():
        return PriorityQueue.list
    
#Creating class objects to call class functions
pq1=PriorityQueue(1)
pq2=PriorityQueue(1)
pq3 = PriorityQueue(1)
pq1.add_element(1,'X')
pq2.add_element(2,'Y')
pq3.add_element(3,'Z')
print("Is Empty : ", end='')
print(pq1.check_empty())
print(pq1.minimum_element())
print(pq1.remove_element())
print(PriorityQueue.summary())
print(pq1.length())
