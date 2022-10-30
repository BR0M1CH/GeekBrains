import random, json
Garage = {"Mazda": {"Rx7":{"Двигатель":"Сток","Коробка передач":"Сток","Шины":"Сток", "Нитро":"Нет", "Турбонаддув":"Нет"}}}
Helper = {"Сток":int(1), "Спорт":int(2), "Про":int(3), "Элита":int(4), "Нет":int(0), "Да":int(1), "TwinTurbo":int(2), "BiTurbo":int(1)}
def get_key(d:dict, value):
    for k, v in d.items():
        if v == value:
            return str(k)

def Mark():
    global helpmas, Garage
    while True:
        try:
            n = input(f"Марки, которые есть у вас в гараже: {helpmas}\nКакую марку смотрим?: ")
            if n not in Garage:
                raise Exception
        except:
            print("Такой марки в гараже нет, попробуем еще раз")
        else:
            return(n)


def Model():
    global helpmas, Garage, n
    while True:
        try:
            m = input(f"Модели марки {n}, которые есть у вас в гараже: {helpmas}\nКакую модель смотрим?: ")
            if m not in Garage[n]:
                raise Exception
        except:
            print("Такой модели у такой марки нет, попробуем еще раз")
        else:
            return(m)


def spec():
    global helpmas, n, m, Garage

    for item in Garage.values():
        helpmas.append(get_key(Garage, item))
        n = Mark()
        helpmas.clear()
        for item in Garage[n].values():
            helpmas.append(get_key(Garage[n],item))
        m = Model()
        helpmas.clear()
        for k, v in Garage[n][m].items(): 
            helpmas.append(f"{k} - {v}")
        return(helpmas)


def spec_change_input_key():
    global helpmas, Garage, n, m
    while True:
        try:
            l = input("Какой параметр меняем? \n")
            if l not in Garage[n][m]:
                raise Exception
        except:
            print(f"Такой характеристики у {n}{m} нет, попробуем еще раз")
        else:
            return(l)


def spec_change():
    global Garage, n, m, l
    while True:
        try:
            s = input("Какой уровень ставим? \n")
            if l == "Двигатель" or l == "Коробка передач" or l == "Шины":
                if s != "Сток" and s != "Спорт" and s != "Про" and s !="Элита":
                    raise Exception
                else: Garage[n][m][l] = s
            elif l == "Нитро":
                if s != "Да" and s!="Нет":
                    raise Exception
                else: Garage[n][m][l] = s
            elif l == "Турбонаддув":
                if s != "Нет" and s != "TwinTurbo" and s != "BiTurbo":
                    raise Exception
                else: Garage[n][m][l] = s
        except:
            print(f"Такая характеристика не свойственна для параметра {l}, попробуем еще раз")
        else: 
            for k, v in Garage[n][m].items(): 
                print(f"Теперь у машины такие параметры:")
                print(f"{k} - {v}")
             

helpmas = []
while True:
    command = input("Введите команду: ")
    if command == "/specifications":
        spec()
        for i in helpmas: print(i)
        helpmas.clear()
    if command == "/tune":
        spec()
        for i in helpmas: print(i)
        l = spec_change_input_key()
        spec_change()

        


        
            
            

        

        
    