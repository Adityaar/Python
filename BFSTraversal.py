import os, sys
'''
Usage:
======
BFSTraversal.py <directory path>

The program traverses entire directory structure in Breadth-First manner.
It gives collects all files returns the list object

'''
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

def BFStraversal(path):

        files = []
        fullpath = path
        q = Queue()
        q.enqueue(path)
        while not q.isEmpty():
                dir = q.dequeue()
                dirs = os.listdir(dir)
                for f in dirs:
                        fullpath = dir+'/'+f
                        files.append(fullpath)
                        if os.path.isdir(fullpath):
                                q.enqueue(fullpath)
        return files

if __name__ == '__main__':

        if len(sys.argv) > 1:
                path = sys.argv[1]

                '''
                The below function will return a list of files collected in BFS order. The files have fullpaths.
                '''
                all_files = BFStraversal(path)
                
                for f in all_files:
                        print f
        else:
                print 'Usage: BFSTraversal.py <directory path>'
