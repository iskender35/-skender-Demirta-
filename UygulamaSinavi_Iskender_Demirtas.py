print("""
İşlem seçimi : 
Çıkmak için : Kırmızı Tuşa Basınız
1 - Bakiye Sorgulama
2 - Para Yatırma
3 - Para Çekme
4 - Hesaplarım arası para aktarımı
5 - Çikis
""")
 
Hesap1_Bakiyeniz = 1000 
Hesap2_Bakiyeniz = 0
while True :
    islem = input('İslem Yapmak İstediğiniz Numara')
    if(islem == "5"):
        print('Bankamızı Tercih Ettiğiniz İçin Teşekkür Ederiz')
        break
    elif (islem == '1'):
        Hesap  = int(input("İşlem Yapmak istediğiniz Hesabı Seçiniz"))
        if (Hesap == 1):
            print("Hesap 1 Bakiyeniz {} Tl dir".format(Hesap1_Bakiyeniz))
        elif (Hesap == 2):
            print("Hesap 2 Bakiyeniz {} Tl dir".format(Hesap2_Bakiyeniz))
        elif (Hesap > 2):
            print("Lütfen Geçerli Bir İşlem Yapınız")
    elif(islem == '2'):
        Hesap  = int(input("İşlem Yapmak istediğiniz Hesabı Seçiniz"))
        if (Hesap == 1):
            yatacak=int(input('Yatırmak İstediğiniz Miktarı Giriniz'))
            Hesap1_Bakiyeniz = Hesap1_Bakiyeniz + yatacak
            print("Hesabınıza {} Tl Yatırdınız".format(yatacak))
            print("Hesap 1 Bakiyeniz {} Tl dir".format(Hesap1_Bakiyeniz))
            print("Hesap 2 Bakiyeniz {} Tl dir".format(Hesap2_Bakiyeniz))
        elif (Hesap == 2):
            yatacak=int(input('Yatırmak İstediğiniz Miktarı Giriniz'))
            Hesap2_Bakiyeniz = Hesap2_Bakiyeniz + yatacak
            print('Hesabınıza {} Tl Yatırdınız'.format(yatacak))
        elif (Hesap > 2):
            print("Lütfen Geçerli Bir İşlem Yapınız")
    elif(islem=='3'):
        Hesap  = int(input("İşlem Yapmak istediğiniz Hesabı Seçiniz"))
        if (Hesap == 1):
            miktar = int(input("Cekmek istediginiz miktarı giriniz"))
            if (Hesap1_Bakiyeniz < miktar):
                print("Yetersiz Bakiye")
                continue
            else:
                Hesap1_Bakiyeniz = Hesap1_Bakiyeniz - miktar
                print("1. Hesabınızdan {} Tl çektiniz".format(miktar))
        if (Hesap == 2):
            miktar = int(input("Çekmek istediginiz miktarı giriniz"))
            if (Hesap2_Bakiyeniz < miktar):
                print("Yetersiz Bakiye")
                continue
            else:
                Hesap2_Bakiyeniz = Hesap2_Bakiyeniz - miktar
                print("2. Hesabınızdan {} Tl çektiniz".format(miktar))
        elif (Hesap > 2):
            print("Isleminiz Gecersiz Lutfen Tekrar Deneyiniz")
    elif(islem=='4'):
        Hesap  = int(input("İşlem Yapmak istediğiniz Hesabı Seçiniz"))
        if (Hesap == 1):
            Havale = int(input("Havale miktarını giriniz"))
            if(Havale > Hesap1_Bakiyeniz):
                print("Yetersiz Bakiye")
                continue
            else:
                Hesap1_Bakiyeniz = Hesap1_Bakiyeniz - Havale
                Hesap2_Bakiyeniz = Hesap2_Bakiyeniz + Havale
                print("1.Hesabınızdan {} Tl 2.Hesabınıza havale yaptınız".format(Havale))
        if (Hesap == 2):
            Havale = int(input("Havale miktarını giriniz"))
            if(Havale > Hesap2_Bakiyeniz):
                print("Yetersiz Bakiye")
                continue
            else:
                Hesap2_Bakiyeniz = Hesap2_Bakiyeniz - Havale
                Hesap1_Bakiyeniz = Hesap1_Bakiyeniz + Havale
                print("2.Hesabınızdan {} Tl 1.Hesabınıza havale yaptınız".format(Havale))
        elif (Hesap > 2):
            print("Isleminiz Gecersiz Lutfen Tekrar Deneyiniz")
    else:
        print('Geçersiz İşlem')