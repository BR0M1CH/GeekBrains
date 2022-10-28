import random
General_stones = int(2021)
Bot_stones = int(0)


def Bot_start_auto(general):
    global Bot_stones
    general -= 28
    Bot_stones+=28
    print(f"Бот забрал 28 камней, в куче осталось {general} камней")
    return (general)


def player_random(general):
    random_stone = random.randrange(1, 29)
    general -= random_stone
    print(
        f"Игрок забрал {random_stone} камней, в куче осталось {general} камней")
    return (general)



def bot_play(general):
    global Bot_stones
    bot_takes = general-28-27
    general -= bot_takes
    Bot_stones+=bot_takes
    print(f"Бот забрал {bot_takes} камней, в куче осталось {general}")
    return (general)


def bot_win(general, n):
    global Bot_stones
    bot_takes = general-n
    general -= bot_takes
    print(f"Бот забрал {bot_takes} камней, в куче осталось {general}")
    Bot_stones+=bot_takes
    return (general)


def player_play(general):
    try:
        player_takes = int(
            input(f"В куче {general} камней, какое количество вы хотите забрать себе? "))
        if player_takes > 28 or player_takes < 1:
            raise NameError
        else:
            general -= player_takes
            print(
                f"Вы забрали {player_takes} камней, в куче осталось {general} камней")
            return (general)
    except NameError:
        print("А кто это у нас тут такой хитрый?")
        return (player_play(general))
    except ValueError:
        print("Вы ввели строку, а нужно число")
        return (player_play(general))


lot = random.randrange(0, 2)
if lot == 1:
    print("Бот начинает")
else:
    print("Игрок ходит первым")
    General_stones = player_random(General_stones)
while General_stones > 88:
    General_stones = Bot_start_auto(General_stones)
    # В этой строке игрок ходит рандомно
    General_stones = player_random(General_stones)
    # General_stones = player_play(General_stones)                            # В этой строке игрок ходит сам, выбрать одну из вариаций
    print(General_stones)
if General_stones == 88:
    General_stones -= 1
else:
    while General_stones > 59:
        General_stones = bot_win(General_stones, 59)                
        General_stones = player_play(General_stones)
General_stones = bot_win(General_stones, 29)
General_stones = player_play(General_stones)
print(f"В куче осталось {General_stones} камней, бот забирает себе всё и выигрывает")
print(f"У бота {Bot_stones} камней")
