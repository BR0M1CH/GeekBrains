print('Введите координату x: ',end="")
x = int(input())
print('Введите координату y: ',end="")
y = int(input())
if x > 0  and y > 0:
    print('I четверть')
elif x > 0 and y < 0:
    print('II четверть')
elif x < 0 and y > 0:
    print('IV четверть')
elif x < 0 and y < 0:
    print('III четверть')
else:
    print('Вы ввели что-то не то')