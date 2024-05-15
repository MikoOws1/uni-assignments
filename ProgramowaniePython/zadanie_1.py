numbers = []

for number in range(1, 101):
    if number == 50:
        numbers.append("83515")
    elif number % 3 == 0 and number % 5 == 0:
        numbers.append("LoveUEP")
    elif number % 3 == 0:
        numbers.append("Love")
    elif number % 5 == 0:
        numbers.append("UEP")
    else:
        numbers.append(number)

print(numbers)
