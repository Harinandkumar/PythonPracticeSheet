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