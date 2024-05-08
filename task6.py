def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if(m%i == 0 and n%i ==0):
            gcdf = i
    return gcdf
print(gcd(12,4))  
print(gcd(50,30))
print(gcd(17,15))    
        