# str1 = [i for i in input("Введите первое уравнение: ")]
# str2 = [i for i in input("Введите второе уравнение: ")]
str1 = "x^2+3=0"
str2 = "6x^4+3x^2-3x+2=0"
def spliter(list):                                               #Функция просто разбивает строку на отдельные блоки переменных              
    helper,helpstr = [], ""
    for i in range(len(list)):
        if list[i] != "+" and list[i] !="-" and list[i] != "=":
            helpstr+=list[i]
        else:
            helper.append(helpstr)
            helpstr = ""
            helpstr+=list[i]
    while "" in helper:
        helper.remove("")
    return(helper)
def zeroer(array):                                               #Если какого-то "икса" нет, то на месте его коэфиициента ставит 0
    helper = [i for i in array]
    array = []
    a = int(helper[0][-1])
    for i in range(a+1):
        array.append("")
    for k in range(len(helper)):
        if helper[k][-1] != "x" and "x" in helper[k]:
            a = int(helper[k][-1])
            array[-a-1] = helper[k]
        elif helper[k][-1] == "x":
            array[-2] = helper[k]
        if "x" not in helper[-1]:
            array[-1] = helper[-1]
    for i in range(len(array)):
        if array[i] == "":
            array[i] = "0" 
    return(array)
def coef(array):                                                #Переводит все строки в нужные числа
    for i in range(len(array)-2):
        if ("^") in array[i]:
            array[i] = array[i][:-3]
    if ("x") in array[-2]:
        array[-2] = array[-2][:-1]
    for i in range(len(array)):
        if array[i] == "-":
            array[i] = int(-1)
        elif array[i] == "":
            array[i] = int(1)
        else:
            array[i] = int(array[i])
    return(array)
str1 = (coef(zeroer(spliter(str1))))
str2 = (coef(zeroer(spliter(str2))))
for i in range(max(len(str1),len(str2) - min(len(str1),len(str2)))):          #делаем так, чтобы длины массивов были равны
    if len(str1) < len(str2):
        str1.insert(0, int(0))
    elif len(str2) < len(str1):
        str2.insert(0, int(0))
result=""
for i in range(len(str1)):                                                    #Складываем массивы
    str1[i] +=str2[i]
result+=(f"{str1[0]}x^{len(str1)-1}")
for i in range(1,len(str1)):
    if str1[i] > 0 and i <len(str1)-2:
        result += (f"+{str1[i]}x^{len(str1)-1-i}")
    elif str1[i] < 0 and i <len(str1)-2:
       result += (f"{str1[i]}x^{len(str1)-1-i}") 
    elif str1[i] > 0 and i == (len(str1)-2):
        result+=(f"+{str1[-2]}x")
    elif str1[i] < 0 and i == (len(str1)-2):
        result+=(f"{str1[-2]}x")
    elif i == len(str1)-1 and str1[i]>0:
        result+=(f"+{str1[-1]}")
    elif i == len(str1)-1 and str1[i]<0:
        result+=(f"{str1[-1]}")
print(result)





        

   

