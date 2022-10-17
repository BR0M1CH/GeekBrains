import random
import time

t0 = time.time()
for i in range(100):
    n = random.randint(5,25) #Количество предикатов
    print(f"Система рандомно сгененрировала следующее количество предикат: {n}","\n")
    Pred1 = []
    Sum1 = 0
    Sum2 = 1
    for i in range(n):
        Pred1.append(1)
        Pred1[i] = (bool(random.getrandbits(1)))
        Sum1 += Pred1[i]
    print(Pred1,"\n")
    if Sum1 != 0:
        Sum1 = True
    else:
        Sum1 =  False
    Sum1 = not(Sum1)
    print(Sum1,"\n")
    Pred2 = Pred1.copy()
    for i in range(n):
        Pred2[i] = not(Pred2[i])
        Sum2 *= Pred2[i]
    print(Pred2,"\n")
    if Sum2 == 0:
        Sum2 = False
    else:
        Sum2 = True
    print(Sum2,"\n")
    if Sum1 == Sum2:
        print("Высказывание истинно, что и требовалось ожидать")
    else:
        print("Высказывание ложно, где-то ошибка")
    print(u'\u2500' * 200)
t1 = time.time()
print(t1 - t0)

