import random
# buyukliste = []
# for i in range(0,8):
#     liste = []
#     for j in range(0,6):
#         liste.append(random.randint(1,50))
#     buyukliste.append(liste)
# print(*buyukliste,sep="\n")

# buyukliste = [[random.randint(1,50) for j in range(0,6)] for i in range(0,8)]
# print(*buyukliste,sep="\n")


alfabe = "abcdefghiıjklmnoöprsşqtuvwyz"
secim = alfabe[random.randint(0,len(alfabe))]
tahmin =""
while tahmin!=secim:
    tahmin = input("Hangi karakter")
    secim = alfabe[random.randint(0,len(alfabe))]