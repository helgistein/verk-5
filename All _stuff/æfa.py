age = int(input("Input age: ")) # Do not change this line
price = 0.0
if age < 65 and age > 5:
    price = 30.0
elif age >= 65:
    price = 15.0
print(price)