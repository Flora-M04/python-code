income = int(input("Enter your income: "))
tax = 0
if(income>100000):
    tax = (income*0.3)
elif(income>50000):
    tax = (income*0.2)
elif(income>20000):
    tax = (income*0.1)
else:
    tax = 0
print("Your tax is:", tax)