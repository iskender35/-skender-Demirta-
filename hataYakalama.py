# try:
#     a = int(input("1. Sayı"))
#     b = int(input("2. Sayı"))
#     print(a/b)
# except ZeroDivisionError:
#     print("Hata var")
# except ValueError:
#     print("Sadece sayı giriniz")


try:
    a = input("1. Sayı:")
    adim = "a.d.m.-1a"
    if a == "Soner":
        raise Exception
    b = int(input("2. Sayı:"))
    adim = "a.d.m.-1b"
except:
        print("Hata var Hata Mesajı",adim)
else:
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Sıfıra bölünme hatası")
