def permutate(seq):
    """permutate a sequence and return a list of the permutations"""
    if not seq:
        return [seq] # is an empty sequence
    else:
        temp = []
        for k in range(len(seq)):
            print seq[:k] + seq[k+1:]
            #print k, part # test
            #for m in permutate(part):
                #temp.append(seq[k:k+1] + m)
        #print m, seq[k:k+1], temp # test
    return temp
    
permutate('abc');    

