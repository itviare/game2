from random import randint

d = 0
dd = 0
nd = 100
n = randint(1, nd)
pp = 9
name = input("Никнейм : ")
print("Найдите задуманное число "+name)

while True:
    a = int(input("Сколько вы думаете: "))
    if pp == -1:
        dd+=1
        print("Game over")
        inp = input("Чтобы ещё раз поиграть нажмите 1,а если сдались то 0 ")
        if inp == "0":
            break
        if inp == "1":
            pp=9
            n = randint(1, nd)
            continue

    if a==n:
        d+=1
        print(f"Нашли! Не впечатляет {name}! Вы выиграли {d} раз ,и проиграли  {dd} ")
        inp = input("Попробуйте 1  ")
        if inp == "0":
            break
        elif inp == "1":
            nd+=200
            pp=9
            n = randint(1, nd)
            continue
        else:
            print("Попробуйте ещё раз!")
    elif a < n:
        print("Моё число больше")
        pp-=1
    elif a > n:
        print("Моё число меньше")
        pp-=1