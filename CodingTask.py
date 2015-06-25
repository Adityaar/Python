import os, sys
from Checksum import giveChecksum

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

        '''
        This function collects all files given a directory path by traversing in Breadth-First order.
        '''
        files = []
        fullpath = path
        q = Queue()
        q.enqueue(path)
        while not q.isEmpty():
                dir = q.dequeue()
                dirs = os.listdir(dir)
                for f in dirs:
                        fullpath = dir+'/'+f

                        if os.path.isfile(fullpath):
                                files.append(fullpath)
                        if os.path.isdir(fullpath):
                                q.enqueue(fullpath)
        return files

if __name__ == '__main__':

        if len(sys.argv) > 1:
                path = sys.argv[1]

                fdict = {}
                dups = {}
                all_files = BFStraversal(path)

                for f in all_files:
                        fhash = giveChecksum(f)         #Compute MD5 HASH of each file and store in dict. Duplicate files will have same HASH.
                        if fhash in fdict:
                                l = []
                                l = fdict[fhash]
                                l.append(f)
                                dups[fhash] = l
                        else:
                                fdict[fhash] = [f]

                for k,v in dups.items():
                        print 'Duplicate files with same content (md5sum=' + k + ') are:'
                        for file in v:
                                print file + ' '

        else:
                print 'Usage: CodingChallenge.py <directory path>'
