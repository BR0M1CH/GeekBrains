n=int(input("Введите количество строк массива:"))
m=int(input("Введите количество столбцов массива:"))
def massgen():
    print("Введите элементы массива, невведенные элементы считаются равными 0")
    try:
        A = [list(map(int, input().split(maxsplit = (m-1)))) for i in range(n)]
    except ValueError:
        print('Ошибка ввода данных, попробуйте еще раз...')
        return(massgen())
    else:
        return(A)
A = massgen()
print(A)
print()
for i in range(n):
    for j in range(m):
        for x in range(n):
            for y in range(m):
                try:
                    if A[i][j] < A[x][y]:
                        buf = A[x][y]
                        A[x][y] = A[i][j]
                        A[i][j] = buf
                except IndexError:
                    A[x].append(0)                
print("Отсортированный массив выглядит так:")
for i in range(n):
    print(A[i])
























