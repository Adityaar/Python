import os
import sys
from Checksum import giveChecksum

class DirWalk:
    def __init__(self, path):
        self.path = path

    def collectFilePaths(self):
        '''
                This function returns 2 dictionaries.
                This function creates a dictionary of the form = { size1 : [file1,file2,.....] , size2 = [file1,file2,file3...] }
                The assumption is that if two files are same, then thier sizes must also be equal.
        '''
        #path_list = []
        file_per_size = {}
        same_size_files = []

        small_dups = {}
        small_dict = {}

        for dirname,subdirpath,filelist in os.walk(path):
                for f in filelist:
                        fullpath = os.path.join(dirname,f)

                        if os.path.exists(fullpath):            # To check and remove stale sym links from search

                                size = os.path.getsize(fullpath)

                                '''

                                I wanted to collect all HUGE files based on their sizes and compare them differently. But there are certain hard cases
                                which will defeat the whole purpose. You can see more explanation in "Checksum.py"
                                So the below IF block does not work and commented out.
                                Instead all the files are compared the same way.

                                #if size >= 268435456 :                                         # To build dictionary for files with size > 256M

                                        path_list.append(fullpath)

                                        if size in file_per_size:
                                                same_size_files = file_per_size[size]
                                                same_size_files.append(fullpath)
                                                file_per_size[size] = same_size_files
                                        else:
                                                same_size_files = []
                                                same_size_files.append(fullpath)
                                                file_per_size[size] = same_size_files
                                else:

                                '''
                                fhash = giveChecksum(fullpath)
                                if fhash in small_dict:
                                        l = []
                                        l = small_dict[fhash]
                                        l.append(fullpath)
                                        small_dups[fhash] = l
                                else:
                                        small_dict[fhash] = [fullpath]

        return (small_dups,file_per_size)

if __name__ == '__main__':

        if len(sys.argv) > 1:
                path = sys.argv[1]
                obj = DirWalk(path)

                (dups,hugefiles) = obj.collectFilePaths()

                for k,v in dups.items():
                        print 'Duplicate files with same content (md5sum=' + k + ') are:'
                        for file in v:
                                print file + ' '
        else:
                print 'Usage: CodingChallenge.py <directory path>'
