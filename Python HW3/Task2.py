print("Введите массив")
list = list(map(int, input().split()))
for i in range(int(len(list)/2)):
    list[i]*=list[-1]
    list.pop()
print(list)