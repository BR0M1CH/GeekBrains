import math
from decimal import Decimal as dc

def rounder(a):                            #Функция сама узнает сколько знаков после запятой ввел пользователь, чтобы затем округлить число воизбежание ошибки дробных чисел
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
    a = float(a)
    b = math.trunc(a)
    a = round(a-b,length)
    return(a)
print("Введите массив")
li = list(map(str, input().split()))
li = list(map(rounder, li))
li = list(map(abs, li))
maxF = max(li)
minF = min(li)
print(maxF-minF)


