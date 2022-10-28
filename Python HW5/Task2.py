try:
    with open("Reader.txt", "r", encoding="utf-8") as rf:
        reader = rf.readline()
except:
    print("Файл не найден")
print(reader)
reader = [i for i in reader]
def Coder(reader):
    writer, result, helpstr = [], [], ""
    letter = reader[0]
    while reader != []:
        if reader[0]==letter:
            writer.append(reader[0])
            reader.pop(0)
        else:
            writer.append(" ")
            writer.append(reader[0])
            letter = reader[0]
            reader.pop(0)
    for i in range(len(writer)):
        if writer[i] != " ":
            helpstr = (f"{helpstr}{writer[i]}")
        else:
            result.append(helpstr)
            helpstr=""
    result.append(helpstr)
    for i in range(len(result)):
        result[i] = (f"{result[i][0]}*{len(result[i])}")
    writer = ""
    for i in range(len(result)):
        writer += (f"{result[i]} ")
    return(writer)
def Decoder(reader):
    reader = reader.split()
    print(reader)
    writer,result = [], ""
    for i in range(len(reader)):
        writer.append("") 
        for j in range(int(reader[i][2])):
            writer[i]+=(f"{reader[i][0]}")
    for i in range(len(writer)):
        result+=(f"{writer[i]}")
    return(result)
result = Coder(reader)
print(result)         
try:
    with open("Result.txt", "w", encoding ="utf-8") as rs: 
        rs.write(result) 
except:
    print("Какая то ошибочка")






