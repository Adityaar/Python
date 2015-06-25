s = 'azcbobobegghakl'
match='bob'
x=0
n=0
while n <=len(s)-2:
    if s.startswith('bob',n,len(s)):
        x=x+1    
    n=n+1
print x    
print s.count('bob')
