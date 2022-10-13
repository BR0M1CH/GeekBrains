from operator import truediv
from xmlrpc.client import boolean

def ConverterXYZ(a):
    if a in range(2):
       if a == 1:
           a = True
           return(a)
       else:
           a = False
           return(a)
    else:
        print('Вы ввели не булево значение переменной')
        a = int(input())
        return(ConverterXYZ(a))   

print('Ввведите X')
x = int(input())
x = ConverterXYZ(x)
print('Ввведите Y')
y = int(input())
y = ConverterXYZ(y)
print('Ввведите Z')
z = int(input())
z = ConverterXYZ(z)
print('Таким образом переменные принимают следующие значения: Х = {}, У = {}, Z = {}'.format(x, y, z))
if (not(x or y or z)) == (not(x) and not(y) and not(z)):
    print('Утверждение (¬(X ⋁ Y ⋁ Z)) = (¬X ⋀ ¬Y ⋀ ¬Z) истинно')
else:
    print('Утверждение (¬(X ⋁ Y ⋁ Z)) = (¬X ⋀ ¬Y ⋀ ¬Z) ложно')




    