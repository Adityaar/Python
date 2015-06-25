import sys
f = open(sys.argv[1],'r')

for line in f:    
    st = line.strip().split(',')
    #print st[1].strip()
    new_st = st[0]
    for i in st[1].strip():        
        #print i ,
        new_st = new_st.replace(i,'')    
    print new_st , 
    print
f.close()    
