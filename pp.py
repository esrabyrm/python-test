import random
import string

def sifre_olustur(uzunluk, sayi_istiyor_mu=True, buyuk_harf_istiyor_mu=True, ozel_karakter_istiyor_mu=True):
    harfler = string.ascii_letters
    sayilar = string.digits
    ozel_karakter = string.punctuation
    if sayi_istiyor_mu:
        harfler += string.digits
    if buyuk_harf_istiyor_mu:
        harfler += string.ascii_uppercase
    if ozel_karakter_istiyor_mu:
        harfler += string.punctuation

    sifre = ''.join(random.choice(harfler)for _ in range(uzunluk))
    return sifre
def kullanici_istekleri():
    uzunluk = int(input("Şifre uzunluğunu girin: "))
    sayi_istiyor_mu = input("Şifrede sayi içermesi gerekiyor mu? (evet/hayir): ").lower
    buyuk_harf_istiyor_mu = input("Şifrede büyük harfler olsun mu? (evet/hayir):").lower
    ozel_karakter_istiyor_mu = input("Özel karakterler olsun mu (evet/hayir):").lower

    if sayi_istiyor_mu == "evet":
        sayi_istiyor_mu = True
    else:
        sayi_istiyor_mu = False

    if buyuk_harf_istiyor_mu == "evet":
        buyuk_harf_istiyor_mu = True
    else:
        buyuk_harf_istiyor_mu = False

    if ozel_karakter_istiyor_mu == "evet":
        ozel_karakter_istiyor_mu = True
    else:
        ozel_karakter_istiyor_mu = False

    sifre = sifre_olustur(uzunluk, sayi_istiyor_mu, buyuk_harf_istiyor_mu, ozel_karakter_istiyor_mu)
    print("Oluşturulan Şifre:", sifre)

kullanici_istekleri()








 


