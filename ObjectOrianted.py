class Kedi:
    familya = "Felis"
    def __init__(self,adı="",tuy="",goz="",renk=""):
        self.tuy = tuy
        self.goz = goz
        self.adı = adı
        self.renk = renk
    def beslenme(self):
        self.miyavla()
        print(self.adı,"Beslendi")
    def miyavla(self):
        print(self.adı,"Miyavladı")
Duman = Kedi(adı="Duman",tuy="kısa",goz="yaşil",renk="gri")
print(Duman.goz)
Duman.beslenme() 
Duman = Kedi()
Duman.adı ="Duman"
Duman.beslenme()
melek = Kedi()
melek.adı = "Melek"
melek.beslenme()
