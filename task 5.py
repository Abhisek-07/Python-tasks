# Program to print all the prime numbers in a given interval
start = int(input("Enter lower range:"))
end = int(input("Enter upper range:"))
for num in range(start, end+1):
    if num > 1:
        for i in range(2, num//2 + 2):
            if(num%i == 0):
                break
            else:
                if i == num//2 + 1:
                    print(num)

# Program to check if a given input number is prime or not
n = int(input("Enter a number:"))
c = 0
for f in range(1,n+1):
    if n%f == 0:
        c = c+1
if n == 1:
    print(n, "is neither prime nor composite")
else:
    if c == 2:
        print(n, "is prime")
    else:
        print(n, "is composite")
