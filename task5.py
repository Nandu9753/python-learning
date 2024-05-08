str = "abacdba"
start = 0
end = len(str)
lss = 0
cSet = set()
for s in range(len(str)):
    for i in range(s,end):
        print(str[s:],str[i:s:-1])
        if(str[s:i] == str[i:s:-1]):
            cSet.add(str[s:i])
                
        end += 1
    start += 1
    # if str[s] not in cSet:
    #     while 
    #     cSet.add(str[s])
    #     lss = max(lss,len(cSet))
                
print(cSet)
