import math



mas = []
def inttwo(a):
    global mas
    while a != 0:
        b=a%2
        mas.append(b)
        a = a//2
        inttwo(a)
        return(mas)
    mas.reverse()

def GetLength(a):                             #Функция узнает сколько знаков после запятой ввел пользователь
    helper = []
    for i in a:
        helper.append(i)
    i = 0
    if helper[0] == "-":
        helper.pop(0)
    for i in range(helper.index(".")):
        helper.pop(i)
    helper.pop(0)
    length = len(helper)
    return(length)

def doubletwo(f,g,a,coun):                     #Слишком поздно узнал только про целые положительные числа
    global mas
    a = str(a)
    length = g(a)
    a = float(a)
    b = round(a, length)
    b = math.trunc(a)
    f(b)
    mas.append(".")
    c = round(a,length)
    c = math.trunc((c - b)*1000)               #Шажок для избежания проблем с дробями + снимает обязательства каждый раз округлять переменную
    for i in range(coun):
        c = round(c*2, length)
        if c >= 1000:
            mas.append(1)
            c-=1000
        else:
            mas.append(0)
    return(mas)

a = float(input("Введите число: "))
b = math.trunc(a)
c = a-b
if c == 0:
    a = int(a)
    inttwo(a)
else:
    b = int(input("Введите количество знаков после запятой, которое хотите видеть при переводе в двоичную систему: "))
    doubletwo(inttwo, GetLength, a, b)
print("".join(map(str,mas)))





