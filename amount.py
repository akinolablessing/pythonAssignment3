amount = float(input("Enter the principle amount:"))
interest = float(input("Enter the annual interest rate:"))
years = float(input("Enter the duration in years:"))
interestRate = (interest/100)/12
duration = years * 12
payment = amount * interest * ((1 + interest ) ** duration )/(((1+ interest )** duration) -1)
print(f"Your monthly payment is $ {payment}")
