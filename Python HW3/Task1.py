print("Введите массив")
list = list(map(int,input().split()))
sum = 0
for i in range(len(list)):
   sum+=list[i]
   i+=2
print(sum)
