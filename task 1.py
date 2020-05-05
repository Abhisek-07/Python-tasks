# Program to accept two integer numbers from a user and return their product and if the product is greater than 1000, then return their sum
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
product = num1*num2
if(product <= 1000):
 print("The result is", product)
else:
 print("The result is",  product,  "\nTheir sum is",  (num1+num2))
