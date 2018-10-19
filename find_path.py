###############################################################
#----------------------- QUESTION ----------------------------#
###############################################################

#Defining class Queue
class Queue:
    #Creating a constructor function
    def __init__(self):
        self.items = []

    #Creating a function is_Empty
    def is_Empty(self):
        return self.items == []

    #Creating a function enqueue
    def enqueue(self, ele):
        self.items.insert(0,ele) #Adding element in queue

    #Creating a function dequeue
    def dequeue(self):
        return self.items.pop() #Removing element from queue

    #Creating a function size
    def size(self):
        return len(self.items)

#Defining class node
class node:
    #Creating a constructor function
    def __init__(self , name, visited , nextNodelist):
        self.name = name
        self.visited = visited
        self.nextNodelist = nextNodelist
        self.parentNode = ""

    #Creating a function get_Name
    def get_Name(self):
        return self.name

    #Creating a function get_Visited
    def get_Visited(self):
        return self.visited

    #Creating a function get_NextNodeList
    def get_NextNodeList(self):
        return self.nextNodelist

    #Creating a function change_Visited
    def change_Visited(self , visited):
        self.visited = visited

    #Creating a function setParentNode
    def setParentNode(self , node):
        self.parentNode = node

    #Creating a function getParentNode
    def getParentNode(self):
        return self.parentNode


def findNextRechableNode(row , col , rowRange , columnRange):
    nextNode = []
    for tempRow in rowRange:
        for tempCol in columnRange:
            if((tempRow == row + 2 or tempRow == row - 2 ) and (tempCol == col +1 or  tempCol == col -1)):
                tempName = str(chr(tempCol)) + str(tempRow)
                nextNode.append(tempName)
            elif ((tempRow == row + 1 or tempRow == row - 1 ) and (tempCol == col +2 or  tempCol == col -2)):
                tempName = str(chr(tempCol)) + str(tempRow)
                nextNode.append(tempName)
    return nextNode

rowRange = range(1,9)
columnRange = range(ord("a"),ord("i"))
nodelist = []

for row in rowRange:
    for col in columnRange:
        name = str(chr(col)) + str(row)
        nextNode = findNextRechableNode(row , col , rowRange , columnRange)
        nodeOb = node(name,False,nextNode)
        nodelist.append(nodeOb)
def getObjectfromName(name):
    for node in nodelist:
            if name == node.get_Name():
                return node


#Defining the function findPath(s,t)
def findPath(s,t):
    #To check if were'nt traversing on same node
    if(s==t):
        print("Same node traversal")
        return []
    #If not same node traversal
    q = Queue()
    q.enqueue(s) #Insert in queue
    getObjectfromName(s).change_Visited(True)
    print(q.size())
    while not q.is_Empty():
        v = q.dequeue() #Remove from queue
        if (v == t):
            break;
        nexttemp = getObjectfromName(v).get_NextNodeList();
        for nextnode in nexttemp:
            tempObj = getObjectfromName(nextnode)
            if not tempObj.get_Visited():
                tempObj.change_Visited(True)
                q.enqueue(nextnode)
                tempObj.change_Visited(True)
                tempObj.setParentNode(v)

    path = []
    path.append(t)
    x = getObjectfromName(t).getParentNode()
    print(x)
    path.append(x)
    while x != s:
        y = getObjectfromName(x).getParentNode()
        if(y == ""):
            print("No path found")
            break
        path.append(y)
        x=y
    return list(reversed(path))

#Calling the function findPath
print(findPath("d4", "c2"))
print(findPath("d4", "f5"))

    
    
            


                





    
