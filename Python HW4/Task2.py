import random

mas, a,helper = [random.randint(0,10) for x in range(random.randint(20,25))], 0, []
print(f"Случайно сгенерированный массив выглядит следующим образом: {mas}")
for i in range(len(mas)):
    if mas[i] not in helper:
        helper.append(mas[i])         #Добавил во вспомогательный массив элемент текущий(если он уникальный в рамках вспомогательного массива), в настоящем массиве 
        mas[i] = "a"                  #Этот элемент переприсваиваю, чтобы при дальнейшем поиске он не всплыл(опять же, переприсваивается лишь уникальный элемент)
for i in range(len(helper)):
    while "a" in mas:
        mas.remove("a")               #Подчистил массив от переприсвоенных элементов, чтобы программа не копалась в мусоре
    if helper[i] in mas:
        while helper[i] in mas:       #Если элемент который есть в обоих массивах обнаружен - все его появления удаляются для облегчения поиска,
            mas.remove(helper[i])     #т.к все уникальные элементы переименованы и сохранены в хелпере.
        helper[i] = "b"               #При чем если элемент обнаружен в обоих массивах, то в хелпере он переприсваивается, а затем так же весь хлам удаляется
while "b" in helper:
    helper.remove("b")
print("Список неповторяющихся элементов:", helper)

