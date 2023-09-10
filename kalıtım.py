class Calısan:
    
    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+ "@sirket.com"
    def bilgileri_göster(self):
        return "Ad: {} Soyad:{} Maas:{} Email: {}".format(self.isim,self.soyisim,self.maas,self.email)
    
            
calısan1 = Calısan("ali","ak",4000)
calısan2 = Calısan("merve", "gül", 3999)

class Yazılımcı(Calısan):
    def bilgileri_göster(self):
        return "ben bir yazılımcıyım"


yazılımcı1= Yazılımcı("sude","yıldız",67346)
yazılımcı2= Yazılımcı(" ahmet","güneş",87567)

print(calısan2.bilgileri_göster())
print(yazılımcı1.bilgileri_göster())  