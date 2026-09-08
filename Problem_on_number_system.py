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
