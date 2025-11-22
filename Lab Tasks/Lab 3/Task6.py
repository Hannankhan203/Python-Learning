import random

numbers = [random.randint(1, 100) for i in range(10)]

odd = []
even = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("All numbers:", numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)