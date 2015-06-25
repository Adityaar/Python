def isPrime(a,b):
        '''
        a, b are positive integers, an adjacent pair of numbers.
        The function returns a boolean value: True if the sum of numbers is a PRIME
        False otherwise.        
        '''
        total = a+b
        flag = True
        if total>1:           
            for i in range(2,total):
                if ( total % i ) == 0:
                    flag = False
                    break
        return flag        

def checkList(aList):    
    '''
    Input is a list of numbers.
    Output is a boolean value. 
    Return True if sum of every adjacent pair of numbers is a prime. 
    Else false.
    '''      
    f=True   
                                                                        
    for k in range(0,len(aList)-1):
        if not isPrime(aList[k],aList[k+1]):
            f=False
            break
    return f
        
        
def isEven(n):
    if n%2 == 0 :
        return True


input = []
f = open('D:\MOOC\Python\input.txt')
for line in f:
    input.append(int(line))
    
#print input
output=[]
for i in input:
    #print i
    if i%2 != 0:
        output.append(0)
    else:
        comb=[]
        list_comb=[]
        for j in range(1,i+1):
            comb.append(j)
                
        if checkList(comb):
            list_comb.append(comb)
            print list_comb
