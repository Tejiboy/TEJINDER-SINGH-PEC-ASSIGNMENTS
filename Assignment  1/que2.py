rate=0.2
detuction= 10000
depadd= 3000

gross_income = int(input("Enter your gross income"))
no_of_dep = int(input("Enter your no_of_dep"))

taxable_income= gross_income- detuction- (depadd*no_of_dep)

print(taxable_income)