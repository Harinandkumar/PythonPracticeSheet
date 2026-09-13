def sumOfTwoNumber(n):
    for i in range(2,n):
        count=0
        for j in range(1,i+1):
            if i %j==0:
                count+=1
            count1=0
        for j in range(1,n-i+1):
            if (n-i) % j==0:
                count1+=1
        if count1==2 and count==2:
         return True
        
    return False
print(sumOfTwoNumber(11))

