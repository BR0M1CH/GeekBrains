import math
from decimal import Decimal as dc


n = dc(input("Введите число: "))
a = int(math.trunc(n))
b = dc(n - a)
sum = 0
while a != 0:
    sum += a%10
    a //= 10
while b != 0:
    b = dc(b*10)
    sum += math.trunc(b)
    b = dc(b - math.trunc(b))
print (sum)











    




