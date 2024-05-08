n = [34,55,88,2,4,77,66,1]
for i in range(len(n)):
    for j in range(0,len(n)-i-1):
        if(n[j] > n[j+1]):
            n[j],n[j+1] = n[j+1],n[j]
print(n)            