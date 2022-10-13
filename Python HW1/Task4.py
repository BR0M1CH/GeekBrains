
from turtle import end_fill
while(True):
    print('Введите любой символ, чтобы продолжить. Чтобы закончить введите end') 
    a = str(input())
    if a == "end":
        exit()
    print("Введите первое число: ", end="")
    x = float(input())
    print("Введите второе число: ", end="")
    y = float(input())
    print("Введите оператор: ", end="")
    z = str(input())
    if z not in ("/", "+", "-", "*", "pow","mod", "div"):
        print("Неверно введен оператор, список допуступных операторов: '/' '+' '-' '*' 'pow' 'div' 'mod'")    
    if z == "+":
        print(x+y)
    elif z == "-":
        print(x-y)
    elif z == "*":
        print(x*y)
    elif z == "/":
        if y == 0:
            print("Деление на 0!")
        else:
            print(x/y)
    elif z == "mod":
        print(x%y)
    elif z == "div":
        if y == 0:
            print("Деление на 0!")
        else: 
            print (x//y)
    elif z == "pow":
        print(x**y)


    