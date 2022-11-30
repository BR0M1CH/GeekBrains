import random
container = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player = "X"
bot = "O"

def Field(val): 
    print("\n") 
    print("\t     |     |") 
    print(f"\t  {val[0]}  |  {val[1]}  |  {val[2]}") 
    print('\t_____|_____|_____') 

    print("\t     |     |") 
    print(f"\t  {val[3]}  |  {val[4]}  |  {val[5]}") 
    print('\t_____|_____|_____') 

    print("\t     |     |") 

    print(f"\t  {val[6]}  |  {val[7]}  |  {val[8]}") 
    print("\t     |     |") 
    print("\n") 


def Check_win(val):
    a = 0
    if (val[0] == val[1] == val[2]) or (val[3] == val[4] == val[5]) or (val[6] == val[7] == val[8]):
        a = 1
    elif (val[0] == val[3] == val[6]) or (val[1] == val[4] == val[7]) or (val[2] == val[5] == val[8]):
        a = 1
    elif (val[0] == val[4] == val[8]) or (val[2] == val[4] == val[6]):
        a = 1
    elif (1 not in val) and (2 not in val) and (3 not in val) and (4 not in val) and (5 not in val) and (6 not in val) and (7 not in val) and (8 not in val) and (9 not in val):
        a = 2
    return(a)   


def Player_turn(player):
    global container
    Field(container)
    while True:
        try:
            a = int(input(f"Куда ставим {player}? "))
            if a not in container:
                raise Exception
            break
        except:
            print("Ошибка ввода, попробуем еще раз")
            Field(container)
    container[a-1] = player
    print("Вы походили: ")
    Field(container)


def Lot():
    global player, bot
    a = random.randint(0,1)
    if a == 0: 
        player = "X"
        bot = "O"
    else: 
        player = "O"
        bot = "X"


def Bot_turn(bot):
    global container
    while True:
        try:
            a = random.randint(0,8)
            if container[a] == "O" or container[a] == "X":
                raise Exception
            else:
                container[a] = bot
                Field(container)
                print("Бот походил")
                break
        except:
            print()


Lot()
print(f"Вы играете '{player}'")
if player == "X":
    print("Вы начинаете!")
    Player_turn(player)
else:
    print("Начинает бот!")
while True:
    Bot_turn(bot)
    if Check_win(container) == 1:
        print("Выиграл бот!")
        break
    elif Check_win(container) == 2:
        print("Ничья!")
        break
    Player_turn(player)
    if Check_win(container) == 1:
        print("Вы выиграли!")
        break
    elif Check_win(container) == 2:
        print("Ничья!")
        break
