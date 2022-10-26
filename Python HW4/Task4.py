def reader():  # Функция ввода с проверкой
    global mas
    try:
        print("Введите квадратное уравнение без знаков умножения:", end="")  # Простая проверка ввода на присутсвие степени в строке
        mas = [i for i in (str(input()))]
        mas.index("^")
    except:
        print("Уравнение не квадратное")
        reader()
    return (mas)


def finder_a():  # Функция поиска коэффициента "а"
    global mas
    if mas[0] == "x":  # Если первый символ списка - "х", то коэф. "а" равен единице
        a = int(1)
        while mas[0] != "+" or mas[0] != "-" or mas[0] != "-":
            mas.pop(0)
            if mas[0] == "+" or mas[0] == "-" or mas[0] == "=":
                break
    else:
        oper = 0
        a = str("")
        try:
            int(mas[0])   # Пробуем преобразовать первый символ строки в инт: если преобразовалось, значит на первом месте - цифра, значит знака минус нет
            oper = 0
        except:  # А если не получилось - значит там знак минус, меняем оператор и удаляем этот минус
            oper = 1
            mas.pop(0)
        for i in range(mas.index("^")-1):   # Считываем все символы до "х", добавляем их в строку Б, затем конвертируем её в целое
            a += mas[i]
        try:
            if oper == 0:
                a = int(a)
            else:
                a = int(0-int(a))
        except: # На случай непредвиденных обстоятельств
            print("Ошибка конвертации а")
        while mas[0] != "+" or mas[0] != "-" or mas[0] != "=":     # Подчищаем наш список вплоть до оператора перед икс или перед целым числом
            mas.pop(0)
            if mas[0] == "+" or mas[0] == "-" or mas[0] == "=":
                break
    return (a)


def finder_b():  # Функция поиска коэффициента "b"
    global mas
    b = str("")
    try:
        # Проверяем есть ли вообще в строке икс, если его нет - значит коэф Б = 0
        mas.index("x")
        if mas[0] == "+":  # Смотрим на знак и меняем оператор в зависимости от знака
            oper = 0
        else:
            oper = 1
            mas.pop(0)
        for i in range(mas.index("x")):  # Дальше все по аналогии с А
            b += mas[i]
        try:
            if oper == 0:
                b = int(b)
            else:
                b = int(0-int(b))
        except:
            print("Ошибка конвертации B")
        while mas[0] != "+" or mas[0] != "-" or mas[0] != "=": # В условие добавился знак равно - на случай, если нулевой степени в строке нет
            mas.pop(0)
            if mas[0] == "+" or mas[0] == "-" or mas[0] == "=":
                break
    except:
        b = 0
    return (b)


def finder_c():  # Функция поиска коэффициента "с"
    global mas
    c = str("")
    try:
        mas[0] != "="   # Если в начале строки стоит знак равно, значит нулевого коэф. нет
        if mas[0] == "+":  # Все по аналогии с а и б
            oper = 0
        else:
            oper = 1
            mas.pop(0)
        for i in range(mas.index("=")):
            c += mas[i]
        try:
            if oper == 0:
                c = int(c)
            else:
                c = int(0-int(c))
        except:
            print("Ошибка конвертации C")
    except:
        c = 0
    return (c)


def Discriminant_Plus(a, b, D):   # Тут все просто, считаем иксы, если дискриминант положительный
    x1 = (int(0-b)+D**0.5)/(2*a)
    x1 = round(x1, 2)
    x2 = (int(0-b)+D**0.5)/(2*a)
    x2 = round(x2, 2)
    if x1 == 0:
        x1 = int(0)
    if x2 == 0:
        x2 = int(0)
    return x1, x2


def Discriminant_Minus(a, b, D):  # Считаем комплексные иксы с отрицательным дискриминантом
    print("В целых числа решения нет, но могу предложить в мнимых:")
    D = complex(D**0.5)
    x1 = complex((int(0-b)+D)/(2*a))
    x1 = complex(round(x1.real, 2), round(x1.imag, 2))
    x2 = complex((int(0-b)-D)/(2*a))
    x2 = complex(round(x2.real, 2), round(x2.imag, 2))
    return x1, x2


def D_Calc(defa, defb, defc):  # На вход принимаем три функции поиска коэффициентов, считаем дискриминант и смотрим какую дальше функцию использовать
    a = defa()
    print(a)
    b = defb()
    print(b)
    c = defc()
    print(c)
    D = (int(b**2) - int(4*a*c))
    try:
        D >= 0
        x1, x2 = Discriminant_Plus(a, b, D)
    except:
        x1, x2 = Discriminant_Minus(a, b, D)
    return (x1, x2)


reader()
x1, x2 = D_Calc(finder_a, finder_b, finder_c)
print(f"x1 = {x1} \nx2 = {x2}")
