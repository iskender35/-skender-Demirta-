birler = {"0":"","1": "Bir","2":"İki","3":"Üç"}
onlar = {"0":"","1":"On","2":"Yirmi","3":"Otuz","4":"Kırk","5":"Elli","6":"Altmış","7":"Yetmiş","8":"Seksen"}
basamak = {0:"",1:"Bin",2:"Milyon",3:"Milyar"}
sayi = "3,222.111"
sayi = sayi.replace(",","").replace(".","")
if len(sayi)%3 > 0:
    sayi = sayi.zfill(3-len(sayi)%3+len(sayi))
sonuc = ""
print(sayi)
print(sayi[0:3])
liste = []
for i in range(int(len(sayi)/3)):
    liste.append(sayi[i*3:(i*3)+3])
    liste.reverse()
    okuma = ""
for i in range(len(liste)):
    if liste[i][0] != "1" and liste[i][0] != "0":
        okuma += birler[liste[i][0]] + "yüz"
    elif liste[i][0] == "1":
        okuma += "Yüz"  

okuma += onlar[liste[i][1]]
okuma += birler[liste[i][2]]
sonuc = okuma + " " + basamak[i] + sonuc
okuma = ""
print(sonuc)



    print(basamak[liste.index("003")])
    print(liste)
print(onlar[liste[0][1]] + birler[liste[0][2]])

#    pass
# print(sayi[0:3])
# print(sayi[3:6])
# print(sayi[6:9])
# print(i)
# print(i*3)
