# a = int(input("Sayıyı giriniz"))
# if a%2==0 :
#     print("Sayı Çifttir")
# else:
#     print("Sayı Tektir")
# # a nın 2 ye bölümünden kalan sayı 0 ise çift, değil ise sayı tektir (Alttakide aynı) not 1 and 2 or 3 öncelik sıraları makina ilk onları sırasına göre çalıştırır.

# if not a%2==0 :
#     print("Sayı Tektir")
# else:
#     print("Sayı Çifttir")


# a = int(input("Vize1 Giriniz"))
# b = int(input("Vize2 Giriniz"))
# c = int(input("Final Notu Giriniz"))
# Notu = round((0.3*a) + (0.3*b) + (0.4*c))

# Sonuc = ""


# # Notu = int(input("Notunuzu Giriniz"))
# # Sonuc = ""

# if Notu < 25 and Notu >=0:
#     Sonuc="FF"
# elif Notu < 45 and Notu >=25:
#     Sonuc="FD"
# elif Notu < 55 and Notu >=45:
#     Sonuc="DD"    
# elif Notu < 60 and Notu >=55:
#     Sonuc="DC"
# elif Notu < 69 and Notu >=60:
#     Sonuc="CC"
# elif Notu < 80 and Notu >=70:
#     Sonuc="CB" 
# elif Notu < 85 and Notu >=80:
#     Sonuc="BB" 
# elif Notu < 90 and Notu >=85:
#     Sonuc="BA"
# elif Notu <= 100 or Notu >=90:
#     Sonuc="AA" 
# else:  
#     Sonuc = "Not Hesaplanamadı"
# print("Notunuz {},{} İyi Günler Dileriz".format(Sonuc))
# input()

# if vites==1 :
#     print("1")
# elif vites==2:
#     print("2")
# elif vites==3:
#     print("3")
# elif vites==4:
#     print("4")
# elif vites==5:
#     print("5")
# else:
#     print("N")

# Var1 = "Montumun cebinde yok kuruş"
# if "kuruş" in Var1:
#     print("Zenginsin Kardeşim")

# liste = [1,2,3,4,9999]
# if 9999 in liste:
#     print("Sayı Burda")
    
# import random
# liste = []
# if i in range(1,20):
#     liste.append(random.randint(0,1000))

# tahmin = int(input("Tahmin et"))

# if tahmin in liste:
#     print("Kazandın")
# else:
#     print("Kaybettin")

username = input("Kullanıcı adı")
sifre = input("Şifre")

if username:
    if username == "ali" and sifre == "123456":
        print("Ali Hoşgeldi")
    else:
            print("Kullanıcı Bulunamadı")
else:
    print("Giriş Yapılamadı")






