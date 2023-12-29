
N = int(input("Введите число: "))

if N % 2 == 0:
    next_even = N + 2
else:
    next_even = N + 1

print("Следующее четное число:", next_even)