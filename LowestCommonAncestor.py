import sys

f = open(sys.argv[1],'r')

class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data        
    
    def insert(self,data):
        
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def path_to_node(self,data,p=None):                
        if data < self.data:
            #print str(self.data) + '-->',
            p.append(self.data)
            self.left.path_to_node(data,p)
                        
        elif data > self.data:
            #print str(self.data) + '-->',
            p.append(self.data)
            self.right.path_to_node(data,p)
        else:
            #print str(self.data)
            p.append(data)
        return p

'''
    def sum_root_to_node(self,data):
        if data < self.data:
            return self.data + self.left.sum_root_to_node(data)
        elif data > self.data:
            return self.data + self.right.sum_root_to_node(data)           
        else:
            return self.data
'''

bTree = Node(30)
bTree.insert(8)
bTree.insert(52)
bTree.insert(3)
bTree.insert(20)
bTree.insert(10)
bTree.insert(29)

for line in f:
    [num1,num2] = line.strip().split()
    #print num1,num2

#num1 = int(raw_input('Enter a number to give sum of root to node: '))
#print 'The sum is: '+ str(bTree.sum_root_to_node(num1))
#l1 = []
#print 'The path from Root to ' +str(num1) + ' is: '
#print 'path is : '+ str(bTree.path_to_node(num1,l1))
    
    l1=[]
    l1 = bTree.path_to_node(int(num1),l1)
    
    #num2 = int(raw_input('Enter 2nd number to give sum of root to node: '))
    #print 'The sum is: '+ str(bTree.sum_root_to_node(num2))
    #l2 = []
    #print 'The path from Root to ' +str(num2) + ' is: '
    #print 'path is : '+ str(bTree.path_to_node(num2,l2))
    
    l2=[]
    l2 = bTree.path_to_node(int(num2),l2)
    
    min_path = min(len(l1),len(l2))
    ancestor=0
    for i in range(min_path):
        if l1[i] == l2[i]:
            ancestor = l1[i]
            #print ancestor
        else:
            break
    print ancestor    
    
f.close()                