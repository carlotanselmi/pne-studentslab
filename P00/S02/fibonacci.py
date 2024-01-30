# Session 2 - Exercise 1:
print("Fibonacci sequence:")
n1 = 0
n2 = 1
for i in range(0, 11):
    print(n1, end=" ")
    n3 = n1 + n2
    n1 = n2
    n2 = n3

print()
n1 = 0
n2 = 1
terms = 11
count = 0
while count < terms:
    print(n1, end=" ")
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count += 1