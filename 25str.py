
num = int(input("Введите число: "))
num_str = str(num)  # Преобразуем число в строку
sum = 0

for digit in num_str:
    sum += int(digit)

print("Сумма цифр числа:", sum)