# Program to count the total no of digits in a number
n = int(input("enter a number: "))
count = 0
while (n>0):
    count = count + 1
    n = n//10
print("The no of digits is ", count)