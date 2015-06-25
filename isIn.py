def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    def lenRecur(st):
        if st == '':
            return 0
        else:
            return 1 + lenRecur(st[0:-1]) 
                                
    #l = lenRecur(aStr)
    mid=0
    if lenRecur(aStr) == 0:
        return False
    elif lenRecur(aStr) == 1 and char == aStr:
        return True
    elif lenRecur(aStr) ==1 and char != aStr:
        return False
    elif lenRecur(aStr)>1:        
        #If String is of length ODD number
        if lenRecur(aStr)%2 !=0:           
            mid = int(lenRecur(aStr)/2)
            if char == aStr[mid]:
                return True
            elif char < aStr[mid]:
                return isIn(char,aStr[0:mid])
            else:
                return isIn(char,aStr[mid+1:])
                
        #If String is of length EVEN number                
        if lenRecur(aStr)%2 == 0:
            mid1 = lenRecur(aStr)/2
            mid2 = mid1 - 1
            if char == aStr[mid1] or char == aStr[mid2]:
                return True
            elif char < aStr[mid1]:
                return isIn(char,aStr[0:mid1])
            else:
                return isIn(char,aStr[mid2:])
    else:
        return False
                
