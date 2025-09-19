import math
num = int(input("Enter a number: "))

print("The number is prime" if num >1 and all(num%i !=0 for i in range(2, int(math.sqrt(num))+1)) else "The number is not prime")
print("The number is not prime" if num <=1 else "")
