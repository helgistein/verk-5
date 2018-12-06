initial_value = int(input("Initial value: "))
step = int(input("Step :"))
next_num = 0
summa = 0
first = initial_value
print(first)
next_num = 1
while summa <= 100:
    next_num += step
    print(next_num, end=" ")
    
    summa += next_num
    if summa >= 100:
        break 
print("Sum of seires is: ", summa)