str1 = input("Введите строку: ")
str2 = input("Введите субстроку: ")
a = []
b = []
for i in str1:
    a.append(i)
for i in str2:
    b.append(i) #[a, a, b, c, c, a, b, c, a, b, a, b] [a, b, c]
print(a,b)
print(len(b))
counter = 0
counter2 = 0
j = 0
i = 0
while j < len(a):
    if b[i] == a[j]:
        counter +=1
        if counter == len(b):
            counter2 +=1
            counter = 0
            i = 0
            j+=1
        else:
            i+=1
            j+=1
    else:
        if counter != 0:
            j = j - counter + 1
            counter = 0
            i = 0
        else:
            j+=1
print(counter2)

            
