v = int(input("Введите скорость: "))
t = int(input("Введите кол-во часов: "))

plus = 0
minus = 0

if v >0:
    plus = v * t

elif v < 0:
    minus = v * t


if plus > 109:
    print("Вася проехал")


if plus < 109:
    print(plus)


if minus < -109:
     print("Вася проехал")

if minus > -109:
    print(minus)

