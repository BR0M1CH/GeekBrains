from codecs import unicode_escape_encode
import random, unicodedata

n = int(input("Введите количество степеней: "))
a = []


def Coder():                                            # Функция, а не простые команды, чтобы свернуть функцию и не засорять вид программы
    global a
    a.append("")
    a.append(u"\u00b2")
    a.append(u"\u00b3")
    a.append(u"\u2074")
    a.append(u"\u2075")
    a.append(u"\u2076")
    a.append(u"\u2077")
    a.append(u"\u2078")
    a.append(u"\u2079")


Coder()


def main(n,a):

    b = str("")
    for i in range(n, -1, -1):
        c = random.randint(0, 100)
        if c != 0:                                      # Если коэф. отличен от нуля - пишем Коэф,Х,+ в случае, если это не нулевая степень икс, в другом просто завершаем коэф, =0
            if i == 0:
                b += (str(f"{c}=0"))
            else:
                b += (str(f"{c}x{a[i-1]}+"))
        else:                                           # Если коэф. равен нулю и это нулевая степень - удаляем последний плюс и пишем =0, если ненулевая степень - не пишем ничего, пропускаем шаг
            if i == 0:
                b[:-1]
                b += str("=0")
    return(b)


def file_work(main, n):
    with open("Romanenko_Task3.txt", "w", encoding="utf-8") as file:
        try:    
            file.write(str(f"Вы выбрали степень {n}, степенное уравнение выглядит так: \n {main}"))
        except:
            print("Ошибочка вышла...")



file_work(main(n,a), n)
