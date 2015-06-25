class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

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
            else:
                return self.left.lookup(data,self)
        elif data > self.data:
            if self.right is None:
                return None, None
            else:
                return self.right.lookup(data,self)
        else:
            return self, parent
            
    def delete(self,data):
        
        node, parent = self.lookup(data)
                
                