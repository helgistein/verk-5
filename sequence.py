n = int(input("Enter the length of the sequence: ")) # Do not change this line
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
for x in range(0, n - 3):
    sum = a + b + c
    print(sum)
    a = b
    b = c
    c = sum