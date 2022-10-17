import math


n = int(input("Введите количество 'измерений': "))
x = []
y = []
sum = 0
for i in range(n):
    x.append(float(input(f"Введите кординату ПЕРВОЙ ТОЧКИ в {i+1} измерении: ")))
for i in range(n):
    y.append(float(input(f"Введите кординату ВТОРОЙ ТОЧКИ в {i+1} измерении: ")))
print(x, y)
for i in range(n):
    sum += ((x[i]-y[i])**2)
print(math.sqrt(sum))

