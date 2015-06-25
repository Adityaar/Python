s = 'azcbobobobegghakl'
curr=s[0]
longest=s[0]
i=1
for n in range(1,len(s)):
    if s[n] >= s[n-1]:
        curr=curr+s[n]
        if len(curr)>len(longest):
            longest=curr
    else:
        curr=s[n]            
print("Longest substring in alphabetical order is: "+longest)