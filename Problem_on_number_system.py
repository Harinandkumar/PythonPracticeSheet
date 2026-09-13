# Q1.Given an integer N, determine whether the given number is even or odd. A number is even if it is completely divisible by 2. Otherwise, it is odd.
def EvenorOdd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
N = int(input("Enter your number:"))
print("number is ",EvenorOdd(N))

#Q2. Check Whether a Number is Positive, Negative, or Zero
def PositiveNegativeZero(n):
    if  n>0:
        return "Positive"
    elif n <0:
        return "Negative"
    else:
        return "Zero"
N = int(input("Enter your number:"))
print(PositiveNegativeZero(N))

#Q3.Find the Greatest of Two Numbers
def  GreatestOfTwo(n1,n2):
    if n1 <n2:
        return n2
    else:
        return n1
n1= int(input("Enter your first number:"))
n2 = int(input("Enter your Second number: "))
print(GreatestOfTwo(n1,n2))
# Q4.Find the Greatest of Three Numbers
def GreatestOfThree(n1,n2,n3):
   if n1 >=n2 and n1 >=n3:
       return n1
   elif n2>=n1 and n2 >=n3:
       return n2
   else:
       return n3
n1 =int(input("Enter your First number:"))
n2 = int(input("Enter your Second number:"))
n3 = int(input("Enter your third number:"))
print(GreatestOfThree(n1,n2,n3))

# Q5. Check Whether a Year is a Leap Year
def CheckLeafYear(y):
    if y % 400 ==0:
        return "Leaf Year"
    elif y%4 and y%2!=0:
        return "Leaf Year"
    else:
        return "Not a Leap Year"
N = int(input("Enter your year to check leaf year or not :"))
print(CheckLeafYear(N))


#6. Find the Sum of First N Natural Numbers
def SumOfNaturalNumber(n):
    i = 1
    sum =0
    while i <=n:
        sum = sum +i
        i = i+1
    return sum
n = int(input("ENter the value of n :"))
print(SumOfNaturalNumber(n))

#Q7. Count the Number of Digits in an Integer
def CountDigit(n):
    count =0
    while n!=0:
        count+=1
        n = n//10
    return count
n = int(input("Enter the number:"))
print(CountDigit(n))
#8. Find the Sum of Digits of a Number
def SumfDigit(n):
    sum =0
    while n!=0:
       LastDigit= n%10
       sum = sum +LastDigit
       n = n//10
    return sum
n = int(input("Enter the number:")) 
print(SumfDigit(n))

#Q9. Reverse the Digits of a Number
def ReverseDigit(n):
    rev =0
    while n !=0:
        LastDigit = n % 10
        rev = (rev*10) +LastDigit
        n = n//10
    return rev
n = int(input("Enter your NUmber:"))
print(ReverseDigit(n))

#Q10.Check Whether a Number is a Palindrome
def CheckPalindrome(n):
    temp =n
    rev =0
    while n!=0:
            LastDigit = n % 10
            rev = (rev*10) +LastDigit
            n = n//10
    if rev == temp:
        return "Palindrome"
    else:
        return "Not Palindrome"
n = int(input("Enter your number:"))
print(CheckPalindrome(n))

#Q11. Find the Maximum and Minimum Digit in a Number
def FindMaxMinDigit(n):
    min = float('inf')
    max =float('-inf')
    while n!=0:
        lastdigit = n % 10
        if lastdigit > max:
            max = lastdigit
        if lastdigit < min:
            min = lastdigit
            
        n = n//10
    return max,min
n = int(input("Enter the number:"))
max,min=FindMaxMinDigit(n)
print("maximum Digit =",max," minimum Digit =",min)

#Q12.Count the Occurrences of a Given Digit
def CountOccurences(n,D):
    d={}
    while n!=0:
        lastdigit =n%10
        d[lastdigit] = d.get(lastdigit,0)+1
        n = n//10
    count = d.get(D)
    return count
n = int(input("Enter the number"))
d = int(input("Enter the digit:"))
print(CountOccurences(n,d))

#Q13. Find the Frequency of Every Digit
def FrequencyOfDigit(n):
    d ={}
    while n!=0:
        lastdigit = n%10
        d[lastdigit] = d.get(lastdigit,0)+1
        n = n//10
    for i in range(0,10):
        print(i,"->",d.get(i,0),end=", ")

FrequencyOfDigit(112233) 
#Q.Given an integer n, find the digit that occurs least frequently in its decimal representation. If multiple digits have the same frequency, choose the smallest digit.

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        d = {}
        
        while n!=0:
            lastdigit =n%10
            d[lastdigit] = d.get(lastdigit,0)+1
            n = n//10
        l=float('inf')
        ans =0
        for i in d:
            if d.get(i) < l or (d.get(i)==l and i <ans ):
                l = d.get(i)
                ans=i
        return ans


#Q14. Replace All 0s with 1s in a Number
def  replaceZeroWithOne(n):
    res =[]
    while n!=0:
        lastdigit = n%10
        if lastdigit ==0:
            res.append(1)
        else:
            res.append(lastdigit)
        n =n//10
    i =len(res)-1    
    while i >=0:
        print(res[i],end="")
        i =i-1 
          
replaceZeroWithOne(102003)

# =========or================
def  replaceZeroWithOne(n):
    number = str(n)
    convertednumber= number.replace("0","1")
    return int(convertednumber)

print(replaceZeroWithOne(102003))

#Q.15. Remove a Given Digit from a Number
def removeGivenDigit(n,d):
    res =''
    output=''
    while n!=0:
        lastdigit = n%10
        if lastdigit !=d:
            res = res+str(lastdigit)
        n = n//10
    i = len(res)-1
    while  i >=0:
        output = output+res[i]
        i = i-1
    return output
print(removeGivenDigit(122342,2))
#Q16. Find the Product of Digits of a Number
def productOfDigit(n):
    product =1
    while n!=0:
        lastdigit = n%10
        product = product * lastdigit
        n =n//10
    return product
print(productOfDigit(234))

        
#17.Repeatedly Add Digits Until a Single Digit Remains
def repeatedlyAddDigit(n):
    while True:
        sum =0
        while n!=0:
            lastdigit = n%10
            sum = sum+lastdigit
            n = n//10
        if 1<=sum<=9:
            
            return sum
        n =sum
print(repeatedlyAddDigit(529))
#Q18.Find the Sum of Squares of Digits
def sumOfSquares(n):
    sum=0
    while n!=0:
        lastdigit = n%10
        sum = sum + (lastdigit**2)
        n = n//10
    return sum
print(sumOfSquares(123))

#19.Check Whether a Number is Prime
def checkPrimeNumber(n):
    count =0
    for i in range(1,n+1):
        if  n%i==0:
            count+=1
    if count ==2:
        return True
    else:
        return False
print(checkPrimeNumber(20))

#20.Print All Prime Numbers in a Given Range
def PrintAllPrime(l,r):
    for i in range(l,r+1):
        count =0
        for j in range(1,i+1):
           if i % j==0:
               count+=1
        if count ==2:
            print(i,end=" ")
PrintAllPrime(10,30)

#Q21.Find the Prime Factors of a Number
def primeFactor(n):

    for i in range(2, n+1):
        while n != 1:
            if n % i == 0:
                print(i)
                n = n // i
            else:
                break

primeFactor(60)

#Q22.Express a Number as the Sum of Two Prime Numbers
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



