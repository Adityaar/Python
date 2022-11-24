class Node:       
    def __init__(self,data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data
        
    def getNext(self):
        return self.next
    
    def setData(self,data):
        self.data = data
    
    def setNext(self,nextdata):
        self.next = nextdata
    
    def hasNext(self):
        return self.next != None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def print_list(self):
        current = self.head
        while current != None:
            print(str(current.getData()) ),
            current = current.getNext()
            #if current is not None:
            #    print('-->')
        print()
                    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNext()                
        return found

    def remove(self,item):
        current = self.head
        prev = current
        found = False        
        
        #Head of the list is matching!
        if current.getData() == item:
            found = True
            self.head = current.getNext()
            del current

        #To check nodes other than Head of the list                                        
        while not found:
            if current.getData() == item :
                found = True
                prev.setNext(current.getNext())
                #current = current.getNext()        
                del current
            else:
                prev = current
                current = current.getNext()
                
    
mylist = LinkedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)                
mylist.add(27)
mylist.add(25)
mylist.add(23)
mylist.add(21)

print ("\nBefore deletion:")

mylist.print_list()
mylist.remove(21)
print ("\nAfter deletion:")
mylist.print_list()
#print mylist.size()
