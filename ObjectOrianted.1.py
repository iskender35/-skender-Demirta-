class KayıtIslem:
    dosyaFormat = "csv"
    def __init__(self,*args,dosyaYolu):
        self.dosyaYolu = dosyaYolu




def dosyaAc(self):
    import os
    dosya = None
    if os.path.exists(self.dosyaYolu):
        dosya = open(self.dosyaYolu,"r+")

