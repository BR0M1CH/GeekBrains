import random

def start():                                                     #0 Проверяем четность m*n
    global m, n                                                  #0
    m = int(input("Введите количество строк: "))                 #0
    n = int(input("Введите количество столбцов: "))              #0
    try:                                                         #0
        2/((m*n)%2-1)                                            #0
    except:                                                      #0
        print("Количество элементов массива нечетно, еще раз")   #0
        start()                                                  #0
start()                                                          #0
mas = []
buf = 0
j = int(0)
i = int(0)
x=int(0)
y=int(0)
for i in range(m):
    mas.append([])
for i in range (m):
    for j in range(n):
        mas[i].append(random.randint(1, 100))
for i in range(m):
    print(mas[i])
helper = []                                            #1 Создаем список в котором хранятся все номера элементов массива начиная с "1"
for i in range(1,m*n+1):                               #1
    helper.append(i)                                   #1
for k in range (int(m*n/2)):                           #2 Обозначаем рамки количества итераций
    a = random.choice(helper)                          #3 Рандомно выбираем элемент из таблицы номеров
    j = a                                              #4 Из коэффициента выражаем сначала переменную, отвечающую за столбцы
    while j > n:                                       #4
        j-=n                                           #4
    j-=1                                               #4
    i = int((a-j-1)/n)                                 #5 Затем из коэффициента и переменной за столбцы выражаем переменную, отвечающую за строку
    helper.remove(a)                                   #6 Не забываем удалить использованый элементик, чтобы не было повторов
    a = random.choice(helper)                          #3 Повторение предыдуших шагов
    y = a                                              #4
    while y > n:                                       #4
        y-=n                                           #4
    y-=1                                               #4
    x = int((a-y-1)/n)                                 #5
    helper.remove(a)                                   #6      
    buf = mas[i][j]                                    #7Повторение предыдущих шагов закончилось, теперь идет просто свап элементов
    mas[i][j] = mas[x][y]                              #7
    mas[x][y] = buf                                    #7
print()
for i in range(m):
    print(mas[i])

