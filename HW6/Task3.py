import re

def Enter():
    global match_list, buffer_dict, main_dict
    n = int(input("Введите количество завершенных матчей: "))
    for i in range(1, n+1): 
        match_list.append(str(input(f"Введите результат {i} матча: ")))

match_list, main_dict = [], {}

def Splitter(match_list):
    for i in range(len(match_list)):
        match_list[i]=re.split(';+', match_list[i])
    return(match_list)

Enter()
match_list = Splitter(match_list)

for i in range(len(match_list)):
    if match_list[i][0] not in main_dict:
        main_dict[match_list[i][0]] = list(map(int,[0, 0, 0, 0, 0]))
    if match_list[i][2] not in main_dict:
        main_dict[match_list[i][2]] = list(map(int,[0, 0, 0, 0, 0]))
    main_dict[match_list[i][0]][0]+=1
    main_dict[match_list[i][2]][0]+=1
    if match_list[i][1] > match_list[i][3]:
        main_dict[match_list[i][0]][1] +=1
        main_dict[match_list[i][0]][4] +=3
        main_dict[match_list[i][2]][3] +=1
        main_dict[match_list[i][2]][4] -=1
    elif match_list[i][3] > match_list[i][1]:
        main_dict[match_list[i][2]][1] +=1
        main_dict[match_list[i][2]][4] +=3
        main_dict[match_list[i][0]][3] +=1
        main_dict[match_list[i][0]][4] -=1
    elif match_list[i][3] == match_list[i][1]:
        main_dict[match_list[i][2]][2] +=1
        main_dict[match_list[i][0]][2] +=1
        main_dict[match_list[i][2]][4] +=1
        main_dict[match_list[i][0]][4] +=1

for i in main_dict.keys():
    main_dict[i] = list(map(str, main_dict[i])) 
    buffer = " ".join(main_dict[i])
    print(f'{i}: {buffer}')
    buffer = ""
