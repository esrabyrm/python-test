class calisan:
    personel_sayısı=0
    def __init__(self,isim,maas):
        self.isim=isim
        self.maas= maas
        calisan.personel_sayısı +=1
        

calisan1 = calisan("ali",388)
print(calisan.personel_sayısı)
calisan1 = calisan("ahmet",78989)
print(calisan.personel_sayısı)

class Ogrenci:
    ogrenci_sayisi=0
    def __init__(self,isim):
        self.isim = isim
        Ogrenci.ogrenci_sayisi +=1
        
    @classmethod
    def ogrenci_sayisi_getir(cls):
        return cls.ogrenci_sayisi    

ogrenci1 = Ogrenci("esra")
ogrenci2= Ogrenci("kerem")
print(Ogrenci.ogrenci_sayisi_getir())





   
    
   



                




 

