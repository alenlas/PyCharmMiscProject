numbers = [7, 11, 8, 5, 3, 12, 2, 6, 9, 10, 1, 4]

total = 0
count = 0

for number in numbers:
    if number % 2 == 0:
        count = count + 1
        total =  total + number
average = total / count
print(average)


