print('Введите день недели')
a = (int(input()))
if a in range (6, 7):
    print('Это выходной день')
elif a in range (1, 5):
    print('Это будний день')
else:
    print('Это не день недели')