import os, sys

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
        
#q = Queue()

if __name__ == '__main__':

        if len(sys.argv) > 1:
                path = sys.argv[1]
                dirs = os.listdir( path )

                q = Queue()
                                
                for f in dirs:
                    #print f               
else:
    print 'Usage: CodingChallenge.py <directory path>'
