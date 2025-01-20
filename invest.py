intial_amount = float(input("Enter the initial amount: "))
rate = float(input("Enter the interest rate: "))
years = int(input("Enter the number of years: "))

init = intial_amount
final = intial_amount
rate = rate / 100

print("Year  \tIntial_Amount  \tInterest  \tfinal")    
for i in range(1, years+1):
    final += round(rate*intial_amount, 2)
   
    print(i, "\t", intial_amount, "\t", rate, "\t\t", final)
    intial_amount = final
print()
print("The final amount after", years, "years is", final)
print("The interest earned after", years, "years is", round(final-init,2))