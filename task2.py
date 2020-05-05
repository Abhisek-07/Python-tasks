# Program to accept a number and calculate the sum of all numbers between 1 and n including n
n = int(input("enter a number: "))
sum = 0
for num in range(1,n+1,1):
    sum = sum + num
print("The sum is", sum)
