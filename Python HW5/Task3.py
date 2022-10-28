str =  input("Введите строку: ").split()
for i in range(len(str)):
    if "абв" in str[i]:
        str[i] = None
while None in str:
    str.remove(None)
print(str)
