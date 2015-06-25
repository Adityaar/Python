import os
import hashlib


def giveChecksum(path):
        '''
                To compute MD5 Checksum of a given file. It computes the checksum block by block with each block of size 2k
        '''
        blocksize=2048
        fp = open(path,'rb')
        checksum = hashlib.md5()
        while True:
                buf = fp.read(blocksize)
                if not buf:
                        break
                checksum.update(buf)
        fp.close()
        return checksum.hexdigest()

def compare_Nbytes(path_list):
        '''
                path_list : List of all files which are of EQUAL sizes.
                To compute MD5 Checksum for list of files. It computes the checksum block by block with each block of size 2k.
                The function is still INCOMPLETE and NOT being used yet...

                The main reason i started to write this function is to compare HUGE FILES.
                For instance, take a case where there are many files each with 2Gb size...ex: f1.csv, f2.csv , f3.csv ....fn.csv(very much possible if
                you receive data from some Finance firms)

                The straight forward way is to generate hash of all files irrespective of their sizes. The files with same hash are duplicate files.
                My assumption(1st) is that MD5 HASH of huge files( size>= 1 or 2G or 5G+) can take long time on a machine with RAM=1G!
                I thought it is much efficient to compare the HASH of first Nbytes(N=2048) of all files. If there is any file having different HASH
                for the 1st block itself, it means that though the file is huge and is having same size as other files, the first few lines itself are
                different from other equal sized files and it can be filtered out from my search for duplicate files(assumption-2).
                But the 2nd assumption is having its own probs(i can discuss more) and realized this is only good if we need to compare only 2 HUGE files
                and not N huge files.
        '''
        blocksize=2048
        same_files = {}
        diff_files = []
        for path in path_list:
                fp = open(path,'rb')
                checksum = hashlib.md5()
                buf = fp.read(blocksize)
                checksum.update(buf)
                fHash = checksum.hexdigest()

                if fHash in same_files:
                        l = []
                        l = same_files[fHash]
                        l.append(path)
                else:
                        same_files[fHash] = [path]
                fp.close()
