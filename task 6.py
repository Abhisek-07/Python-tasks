# Program to print fibonacci series
n = int(input("Enter the number of terms of fibonacci series to be printed: "))
a = 0
b = 1
if(n<0):
    print("Enter a positive integer")
elif(n==1):
    print(a)
else:
    for i in range(0,n):
        print(a)
        sum = a + b
        a = b
        b = sum
# Program to check if a number is fibonacci or not
import math
def checkperfectsquare(n):
    sqr = int(math.sqrt(n))
    if pow(sqr,2) == n:
        return True
    else:
        return False
def isfibonaccinumber(n):
    res1 = 5*n*n + 4
    res2 = 5*n*n - 4
    if checkperfectsquare(res1) or checkperfectsquare(res2):
        return True
    else:
        return False
num = int(input("Enter an integer: "))
if isfibonaccinumber(num):
    print("Yes", num, "is a fibonacci number")
else:
    print("No", num, "is not a fibonacci number")



