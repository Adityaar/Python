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
    
    def lookup(self,data,parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data,self)
        elif data > self.data:
            if self.right in None:
                return None, None
            return self.right.lookup(data,self)
        else:
            return self,parent

    def sum_root_to_node(self,data):
        if data < self.data:
            return self.data + self.left.sum_root_to_node(data)
        elif data > self.data:
            return self.data + self.right.sum_root_to_node(data)           
        else:
            return self.data

    def print_tree(self):        
        '''
        print the tree inorder: left, root and right
        '''    
        if self.left:
            self.left.print_tree()
        print self.data,
        if self.right:
            self.right.print_tree()

flag=True
cnt=0
while flag:
    ch=str(raw_input('Do you want to enter a number(y/n):  '))
    if ch == 'y' or ch == 'Y':
        num=int(raw_input('Enter a number:'))
        if cnt == 0:
            root = Node(num)
            cnt = cnt + 1
        else:
            root.insert(num)
    elif ch == 'n' or ch == 'N':
        flag = False
        if cnt != 0:
            root.print_tree()
            print "\nSum of path from Root to this leaf: " + str(root.sum_root_to_node(num))
        else:
            print "Empty Tree!!"
    else:
        break

search_num=int(raw_input('Enter the node to which you want to find sum: '))
print "\nThe sum of path from Root to node:" + str(search_num) + " is: " + str(root.sum_root_to_node(search_num))

#Sample input:
# 8, 3, 10, 1, 6, 4, 7, 14, 13
            
