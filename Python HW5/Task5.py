# array=[int(i) for i in input("Введите последовательность")]
array = [int(i) for i in "15234178151"]
print(array)
res = []
min1 = min(array)
max1 = min(array)
n1 = min(array)
while len(array) > 0:
    min1 = min(array)
    max1 = min(array)
    n1 = min(array)
    for i in range(len(array)):
        if (n1+1) in array:
            max1 +=1
            n1+=1
    res.append(f"{max1}-{min1}")
    for i in range(max1-min1+1):
        while min1 in array and min1 <= max1:
            array.remove(min1)
            print(array)
        min1+=1
for i in range(len(res)):
    res[i] = res[i].split("-")
maxdif = int(res[0][0])-int(res[0][1])
k = 0
for i in range(len(res)):
    if int(res[i][0])-int(res[i][1]) > maxdif:
        maxdif = int(res[i][0])-int(res[i][1])
        k = i
print(f"Наибольшую последовательность образуют числа от {res[k][1]} до {res[k][0]}")   
