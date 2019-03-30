# i nin anlamı indis bütün aralıktakı değerlerde gezer ve aralıktakı sayıları temsil eder.

# liste =[24,34,56,57,67,87,89,49,11,45,32]
# sayac = 0
# for i in range(0,len(liste)):
#     if liste[i]> 50: 
#         sayac += 1
# print(sayac)

# sayac = 0
# for item in liste:
#     if item > 50:
#         sayac+=1
# print(sayac)

# sayac = 0
# metin = "Fıstıkçı Şahap"
# alfabe = "abcdefghijklmnopqrstuvwxyz"
# for kar in metin:
#     if not (kar.lower() in alfabe):
#     sayac += 1
#     if kar.lower() in alfabe:
#         pass
#     else:
#         saya +=1
# print(sayac)
        
# sayac = 0
# metin = "Fıstıkçı Şahap"
# alfabe = "abcdefghijklmnopqrstuvwxyz"
# for kar in metin:
#     sayac += 1
#     if not (kar.lower() in alfabe):
#         print(" {} adımda for durdu".format(sayac))
#         break 
# print(sayac)


import random
sayi = random.randint(0, 100)
print(sayi)
for i in range(1, 7):
   tahmin = int(input("Sayıyı Tahmin Et"))
    if tahmin > sayi:
        print("Aşağı hak {}".format(6 - i))
    elif tahmin < sayi:
        print("Yukarı Kalan hak {} tahminde buldun".format(6 - i))
    elif tahmin == sayi:
        print("Tebrikler {} tahminde buldun".format(i))
        break
    if i == 6:
        print("Hakkınız Bitt")