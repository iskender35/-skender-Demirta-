# demet = (2,2)
# demet = demet + "selin"
# print(demet)

# sozluk = {"book":"kitap","apple":"elma"}
# # book ıs key, kıtap is value sonrasında virgul ile diğer veriye geçiyoruz
# print(sozluk["book"])
# print(sozluk["book"],["apple"])
alfabe = "abcdefghiıjklmnoöprsşqtuvwyz"
cevrim = {i : alfabe.index(i)for i in alfabe}
# print(cevrim)
cevrim.update({"â":28})
cevrim.update({"ASDDSADS":28})
print(cevrim)
isimlistesi = ["ahmet","ışıl","berkecan","ışınsu","orcun","omer"]
sozluk = {}
sozluk = cevrim.fromkeys(isimlistesi)
sozluk.clear()
print(sozluk)
print(cevrim.values())
print(cevrim.items())



# print(cevrim.get("o"))


# isimlistesi = ["ahmet","ışıl","berkecan","ışınsu","orcun","omer"]
# isimlistesi.sort()
# print(isimlistesi)


# print(sorted(isimlistesi,key = lambda x :cevrim.get(x[0])))
# listedeki her bir elemanın ilk karakterini al sonra çevrimde git ve bu karakterleri isimlerin ilk karakterlerine göre öncelikli sırala