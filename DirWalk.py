import os

class DirWalk:
    def __init__(self, path):
        self.path = path
    def collectFilePaths(self):
        path_list = []
        for dirname,dirpath,filelist in os.walk(path):
                for f in filelist:
                        fullpath = os.path.join(dirname,f)
                        path_list.append(fullpath)
        return path_list
        
path = 'D:\MOOC\Python'

obj = DirWalk(path)
for p in obj.collectFilePaths():
    print p

                