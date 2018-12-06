loan = int(input("Input the cost of item in $: "))

import math

if loan <= 1000:
    rate = 1.5/100
else:
    rate = 2/100 
interest_paid = loan * rate
payment = 50
remaining_debt = (loan-payment+interest_paid)
minus = loan - (loan - remaining_debt)
remaining_debt -= minus
if remaining_debt < payment:
    payment = remaining_debt


if remaining_debt <= payment:
    payment = remaining_debt
month = 1


while remaining_debt > 0:
    
    
    month =+ 1
    print("Month: %d" % (month), payment, interest_paid, remaining_debt)