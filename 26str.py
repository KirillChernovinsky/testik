N = int(input("Введите число от 1 до 9: "))

# Задаем изображение пингвина
pinguin = ["   _~_   \n",
           "  (o o)  \n",
           " /  <>  \\ \n",
           "/        \\\n",
           "  ^^ ^^   \n"]

# Выводим N пингвинов
for i in range(N):
    for line in pinguin:
        print(line, end=" ")
    print()