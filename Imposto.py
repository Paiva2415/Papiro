income = float(input("Enter the annual income: "))

if income < 85528:
    income = income *.18 - 556.2
else:
    income = ((income - 85528) * .32) + 14839.2

if income < 0:
    income = 0.0
    
tax = income

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

print ("")
