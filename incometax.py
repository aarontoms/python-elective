salary = float(input("Enter salary: "))
rate = 0.0

if salary < 300000:
    rate = 0.0
elif salary > 300000 and salary <= 600000:
    rate = 6.0
elif salary > 600000 and salary <= 900000:
    rate = 10.0
elif salary > 900000 and salary <= 1200000:
    rate = 15.0
elif salary > 1200000 and salary <= 1500000:
    rate = 20.0
else:
    rate = 30.0

tax = salary * rate / 100
print("Income tax amount: ", tax)
