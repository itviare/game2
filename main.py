from random import randint

d = 0
dd = 0
nd = 100
n = randint(1, nd)
pp = 10
name = input("Ismiz nima? : ")
print("Ugadayka oyiniga hush kelibsiz, "+name)
print("Man bir son oyladim, topib korinchi uni!")
while True:
    a = int(input("Nechchi deb oylaysiz: "))
    if pp == -1:
        dd+=1
        print("Imkoniyatlariz tugadi.")
        inp = input("Yana oynash uchun 1-ni tering, chiqish uchun 0-ni: ")
        if inp == "0":
            break
        if inp == "1":
            pp=10
            n = randint(1, nd)
            continue

    if a==n:
        d+=1
        print(f"Toptiz! Malades {name}! Siz {d} marta yuta oldiz va {dd} marta yutqizdiz!")
        inp = input("Yana oynash uchun 1-ni tering, chiqish uchun 0-ni: ")
        if inp == "0":
            break
        elif inp == "1":
            nd+=100
            pp=10
            n = randint(1, nd)
            continue
        else:
            print("Boshidan urunib korin!")
    elif a < n:
        print("Mani sonim kottaroq")
        pp-=1
    elif a > n:
        print("Mani sonim kichikroq")
        pp-=1