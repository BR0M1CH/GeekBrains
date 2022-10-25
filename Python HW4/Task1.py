n = int(input("Введите число: "))
mas = []
a = int(2)
for i in range(1,n):
    if not n%i:
        mas.append(i)
def simpler():
    global a, mas, i
    if not mas[i]%a and mas[i]!=a:
        mas[i] = 0
        print(mas)
    else:
        if a<mas[i]:
            a+=1
            simpler()
    a = int(2)
for i in range(len(mas)):
    simpler()
while 0 in mas:
    mas.remove(0)
print(f"Список простых делителей числа {n}: {mas}")