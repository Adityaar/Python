
a = [[ 0 for x in range(12)] for x in range(12)]
for i in range(1,13):  
    #print    
    for j in range(1,13):
        a[i-1][j-1] = str(i*j).rjust(4)

for i in range(1,13):  
    print    
    for j in range(1,13):
        if j==1:
            if len(str(i)) == 2:
                print a[i-1][j-1].strip(),
        else:
            print a[i-1][j-1],
                
            
    