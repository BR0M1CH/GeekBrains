n = int(input("Введите число: "))
a = []
prod = 1
for i in range(1,n+1):
    prod *= i
    a.append(prod)
print(a)
