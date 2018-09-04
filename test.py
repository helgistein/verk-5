import math
loan = int(input("Input the cost of item in $: "))

while loan <= 1000:
    rate = 1.5/100
payment = 50
interest_paid = loan * rate
remaining_debt = loan - payment + interest_paid
interest_paid = remaining_debt * rate 
minus = loan - (loan - remaining_debt)
remaining_debt -= minus

if remaining_debt < payment:
    payment = remaining_debt
month = 1
    
    
print("Month: %d" % (month), payment, interest_paid, remaining_debt)
month += 1