dosya = open(r"D:\Deneme.png","r+")
# print(dosya.read())
dosya.read()
print(dosya.tell())
dosya.seek(0)
