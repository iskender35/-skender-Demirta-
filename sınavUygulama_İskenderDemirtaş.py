print("""
İşlem seçiniz : 
Çıkmak için : Kırmızı Tuşa Basınız
1 - Para Çekme
2 - Para Yatırma
3 - Bakiye Sorgulama
4 - Çıkış Yapmak İstermisiniz?
""")
 
Bakiyeniz = 1000 
while True :
    islem = input('İslem Yapmak İstediğiniz Numara')
    if(islem == "4"):
        print('Pis Fakir Dahada Gelme')
        break
    elif (islem == '1'):
        miktar = int(input('Miktar Giriniz'))
        if(Bakiyeniz - miktar < 0):
            print('Yetersiz Bakiye')
            continue
        else:
            Bakiyeniz = Bakiyeniz - miktar
            print('Hesabınızdan {} Tl Para Çektiniz'.format(miktar))
    elif(islem == '2'):
        yatacak=int(input('Yatırmak İstediğiniz Miktarı Giriniz'))
        Bakiyeniz = Bakiyeniz + yatacak
        print('Hesabınıza {} Tl Yatırdınız'.format(yatacak))
    elif(islem=='3'):
        print('Bakiyeniz {} Tl dir'.format(Bakiyeniz))
    else:
        print('Geçersiz İşlem')