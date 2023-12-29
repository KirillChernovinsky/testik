n = int(input("Школьников: "))
k = int(input("Мандаринов: "))



y = k // n
y1 = k % n

print("На школьника: ",(y))
print("Остаток: ",(y1))
#
# def distribute_mandarins(n, k):
#     # Вычисляем количество мандаринов, которое получит каждый школьник
#     mandarins_per_student = k // n
#
#     # Вычисляем количество оставшихся мандаринов в корзине
#     remaining_mandarins = k % n
#
#     return mandarins_per_student, remaining_mandarins
#
#
# # Получаем входные данные от пользователя
# n = int(input("Введите количество школьников: "))
# k = int(input("Введите количество мандаринов: "))
#
# # Вызываем функцию и сохраняем результаты
# mandarins_per_student, remaining_mandarins = distribute_mandarins(n, k)
#
# # Выводим результаты на экран
# print("Количество мандаринов на каждого школьника:", mandarins_per_student)
# print("Количество оставшихся мандаринов в корзине:", remaining_mandarins)
#
#
#
#
#
#
#
