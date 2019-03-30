# def fonksiyon():
#     print("merhaba")
# fonksiyon()

# def carp(sayi=1):
#     print(sayi*sayi)
# carp()
# carp(5)


# def topla(a=0,b=0):
#     print("{} + {} = {}".format(a,b,a+b))
# topla(852265478,8785465213)


liste = [20.10,40,30,0]

def ortalama(*args,katsayı=0):
    toplam = 0
    for item in args:
        toplam += item
    return toplam/len(args)*katsayı
print(ortalama(20,50,40,30,50,katsayi=54)[0]*5)




