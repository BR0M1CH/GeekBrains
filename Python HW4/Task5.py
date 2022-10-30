import json


Garage = {"Mazda": {"Rx7": {"Engine": "Stock", "Gearbox": "Stock",
                            "Tires": "Stock", "Nitro": "No", "Turbo": "No"}}}
Helper = {"Stock": int(1), "Sport": int(2), "Pro": int(3), "Elite": int(
    4), "No": int(0), "Yes": int(1), "TwinTurbo": int(2), "BiTurbo": int(1)}
Info = {"/spec": "Показывает х-ки конкретного авто", "/tune": "Прокачка одного параметра авто", "/add": "Добавить машину",
        "/remove": "Удалить машину", "/exit": "Завершить работу программы", "/dino":"Прогоняем машину на диностенде", "/load":"Загружаем данные из файла", "/save":"Загружаем данные в файл"}


def get_key(d: dict, value):    #Возвращает ключ от значения 
    for k, v in d.items():
        if v == value:
            return str(k)


def saver():
    global Garage
    with open ("Cars.json", "w", encoding="utf-8") as car:
        car.write(json.dumps(Garage, ensure_ascii=False))
    print("Гараж сохранён!")

   
def loader():
    global Garage
    with open("Cars.json", "r", encoding="utf-8") as car:
        Garage = json.load(car)
    print("Гараж обновлен!")


def Mark():        #Проверка ввода существующей марки
    global Garage
    helpmas = get_mark()
    while True:
        try:
            n = input(f"Марки, которые есть у вас в гараже: {helpmas}\nКакую марку смотрим?: ")
            if n not in Garage:
                raise Exception
        except:
            print("Такой марки в гараже нет, попробуем еще раз")
        else:
            return (n)


def get_model():     #Геттер -  на выходе выдает массив со всеми моделями в рамках конкретной марки
    global Garage
    helpmas = []
    for item in Garage[n].values():
        helpmas.append(get_key(Garage[n], item))
    return (helpmas)


def get_mark():      #Геттер - на выходе выдает массив со всеми марками в гараже
    global Garage
    helpmas = []
    for item in Garage.values():
        helpmas.append(get_key(Garage, item))
    return (helpmas)


def Model():         #Проверка ввода существуей модели
    global Garage, n
    helpmas = get_model()
    while True:
        try:
            m = input(
                f"Модели марки {n}, которые есть у вас в гараже: {helpmas}\nКакую модель смотрим?: ")
            if m not in Garage[n]:
                raise Exception
        except:
            print("Такой модели у такой марки нет, попробуем еще раз")
        else:
            return (m)


def spec():          #На выходе массив с характеристиками конкретной модели
    global n, m, Garage
    helpmas = []
    if Garage == {}:
        print("Ваш гараж пустой")
    else:
        n = Mark()
        m = Model()
        for k, v in Garage[n][m].items():
            helpmas.append(f"{k} - {v}")
    return (helpmas)


def spec_change_input_key():   #Проверка ввода характеристики авто
    global Garage, n, m
    while True:
        try:
            l = input("Какой параметр меняем? ")
            if l not in Garage[n][m]:
                raise Exception
        except:
            print(f"Такой характеристики у {n}{m} нет, попробуем еще раз")
        else:
            return (l)


def spec_change():    #Функция для смены конкретной характеристики авто        
    global Garage, n, m, l
    while True:
        try:
            if l == "Engine" or l == "Gearbox" or l == "Tires":          #Проверка ввода для группы с множестовом "уровней"
                print("Вы можете поставить 4 разных уровня: Stock, Sport, Pro и Elite")
                s = input("Какой уровень ставим? ")
                if s != "Stock" and s != "Sport" and s != "Pro" and s != "Elite":
                    raise ValueError
                else:
                    Garage[n][m][l] = s
            elif l == "Nitro":                                                    #Проверка ввода для нитро, где либо да, либо нет
                print(
                    "Вы можете либо поставить, либо убрать нитро, впишите либо Yes либо No")
                s = input("Какой уровень ставим? ")
                if s != "Yes" and s != "No":
                    raise ValueError
                else:
                    Garage[n][m][l] = s
            elif l == "Turbo":       #Проверка ввода для турбины, где три варианта
                print(
                    "Вы можете поставить TwinTurbo или BiTurbo, так же вы можете убрать турбину, для этого напишите No")
                s = input("Какой уровень ставим? ")
                if s != "No" and s != "TwinTurbo" and s != "BiTurbo":
                    raise ValueError
                else:
                    Garage[n][m][l] = s
        except ValueError:               
            print(
                f"Такая характеристика не свойственна для параметра {l}, попробуем еще раз")
        else:
            print(f"Теперь у машины такие параметры:")
            for k, v in Garage[n][m].items():
                print(f"{k} - {v}")
            break


def adder():          #Функция добавления марки или модели в гараж
    global Garage, n, m
    helpmas = []
    while True:
        n = input("Хотите добавить авто в существующую марку? ")
        try:
            if n == "Yes":
                n = Mark()
                while True:
                    try:
                        m = input("Введите название модели: ")
                        if m in Garage[n]:
                            raise ValueError
                        break
                    except:
                        print("Такая модель уже есть, попробуем еще раз") 
                Garage[n][m] = {"Engine": "Stock", "Gearbox": "Stock",            #В случае успешного ввода создаем новую машину со стоковыми х-ками
                                "Tires": "Stock", "Nitro": "No", "Turbo": "No"}
                break
            elif n == "No":
                while True:
                    try:
                        n = input("Введите название новой марки: ")
                        if n in Garage:
                            raise ValueError
                        break
                    except:
                        print("Такая марка уже есть, попробуем еще раз")
                Garage[n] = {}
                while True:
                    try:
                        m = input("Введите название модели: ")
                        if m in Garage[n]:
                            raise ValueError
                        break
                    except:
                        print("Такая модель уже есть, попробуем еще раз")
                Garage[n][m] = {"Engine": "Stock", "Gearbox": "Stock",              #В случае успешного ввода создаем новую машину со стоковыми х-ками
                                "Tires": "Stock", "Nitro": "No", "Turbo": "No"}
                break
            else:
                raise ValueError
        except ValueError:
            print("Не понял команды, попробуем еще раз")
    for k, v in Garage[n][m].items():
        helpmas.append(f"{k} - {v}")
    return (helpmas)


def remover():        #Удаление марки или модели из гаража
    global Garage, n, m
    helpmas = get_mark()
    while True:
        try:
            n = input(
                "Вы хотите продать все модели бренда или только модель? Напишите All или Model")
            if n == "All":
                n = Mark()
                del Garage[n]
                break
            elif n == "Model":
                n = Mark()
                m = Model()
                del Garage[n][m]
                break
            else:
                raise Exception
        except:
            print("Не разобрал команды, попробуем еще раз")


def Dino():           #Калькулятор лошадиных сил и разгона 0-100 у машины в зависимости от ее характеристик
    global Garage, n, m, Helper
    n = Mark()
    m = Model()
    HP = int(100*(Helper[Garage[n][m]["Engine"]]) +
             50*(Helper[Garage[n][m]["Turbo"]]))
    Acceleraion = int(int(20)-(HP // int(100))-2 *
                      (Helper[Garage[n][m]["Tires"]])-(Helper[Garage[n][m]["Gearbox"]]))
    print(f"У {n} {m} {HP} лошадиных сил, разгон до 100 км/ч = {Acceleraion}с")
    return

print("Привет, я твой гид по гаражу, прокачивай тачки и попадешь в гоночную элиту Сан-Андреаса!\nВведи /help, чтобы узнать мои функции")
while True:
    command = input("Введите команду: ")

    if command == "/spec":
        helpmas = spec()
        for i in helpmas:
            print(i)

    elif command == "/tune":
        for i in spec():
            print(i)
        l = spec_change_input_key()
        spec_change()

    elif command == "/exit":
        print("Залетай к нам в гараж ещё!")
        break

    elif command == "/add":
        helpmas = adder()
        for i in helpmas:
            print(i)

    elif command == "/info":
        for k, v in Info.items():
            print(f"{k} - {v}")
        print("Ответы на вопросы бота писать с большой буквы, я забыл про уменьшение шрифта")

    elif command == "/remove":
        remover()

    elif command == "/dino":
        Dino()


    elif command == "/load":
        loader()

    elif command == "/save":
        saver()

    else:
        print("Прочитайте инструкцию с помощью команды: /info")
