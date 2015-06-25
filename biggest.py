def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    maxKey=None
    vMax=0
    for l in aDict.keys():
        vLen = len(aDict[l])
        if vLen >= vMax:
            maxKey = l
            vMax = vLen
    return maxKey
    
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print biggest(animals)        