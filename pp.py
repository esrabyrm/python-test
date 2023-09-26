import random
import string


def sifre_olustur(
    uzunluk=6,
    kucuk_unlu_harf_istiyor_mu=True,
    buyuk_unlu_harf_istiyor_mu=True,
    kucuk_unsuz_harf_istiyor_mu=True,
    buyuk_unsuz_harf_istiyor_mu=True,
    sayi_istiyor_mu=True,
    ozel_karakter_istiyor_mu=True,
):
    unlu_harfler = "aeiou"
    unsuz_harfler = "bcdfghjklmnprstvyzxw"
    sayilar = "123456789"
    ozel_karakter = "!^+&?\|_"
    sifre=""
    karakter =""

    if kucuk_unlu_harf_istiyor_mu == True:
        sifre = sifre + random.choice(unlu_harfler)

    if buyuk_unlu_harf_istiyor_mu == True:
        sifre = sifre + random.choice(unlu_harfler.upper())

    if kucuk_unsuz_harf_istiyor_mu == True:
        sifre = sifre + random.choice(unsuz_harfler)

    if buyuk_unsuz_harf_istiyor_mu == True:
        sifre = sifre + random.choice(unsuz_harfler.upper())

    if sayi_istiyor_mu == True:
        sifre = sifre + random.choice(sayilar)

    if ozel_karakter_istiyor_mu == True:
        sifre = sifre + random.choice(ozel_karakter)

    
# eğer şifrenin uzunluğu girilen uzunluktan küçükse eksik olan kısım kadar rastgele bir kararkter girilicek.       
while len(karakterler) < uzunluk:
    rastgele_karakter = random.choice(
         string.ascii_letters + string.digits + ozel_karakter
    )
    if rastgele_karakter not in karakterler:
         karakterler += rastgele_karakter

# yeni oluşturulan doğru uzunluktaki şifrenin karakterlerin yerleri rastgele değiştirilecek.
    sifre = "".join(random.sample(karakterler, len(karakterler)))
    return sifre


def kullanici_istekleri():
    kucuk_unlu_harf_istiyor_mu = (
        input("küçük ünlü harf istiyor musun? (evet/hayir): ").lower() == "evet"
    )
    buyuk_unlu_harf_istiyor_mu = (
        input("Şifrede büyük ünlüharfler olsun mu? (evet/hayir):").lower() == "evet"
    )
    kucuk_unsuz_harf_istiyor_mu = (
        input("küçük ünsüz harfler olsun mu (evet/hayir):").lower() == "evet"
    )
    buyuk_unsuz_harf_istiyor_mu = (
        input("büyük ünsüz harfler olsun mu (evet/hayir):").lower() == "evet"
    )
    sayi_istiyor_mu = input("sayilar olsun mu (evet/hayir):").lower() == "evet"
    ozel_karakter_istiyor_mu = (
        input("özel karakterler olsun mu (evet/hayir):").lower() == "evet"
    )
    # kullanıcın min şifre uzunluğuna bağlı
    if sifre.len < uzunluk:
        
       
        
     uzunluk = int(input("Şifre uzunluğunu girin: "))
    # kullanıcının imputu min'den daha küçükse tekrar uzunluk girmesi istenir
    sifre = sifre_olustur(
        uzunluk,
        kucuk_unlu_harf_istiyor_mu,
        buyuk_unlu_harf_istiyor_mu,
        kucuk_unsuz_harf_istiyor_mu,
        buyuk_unsuz_harf_istiyor_mu,
        sayi_istiyor_mu,
        ozel_karakter_istiyor_mu,
    )

    # kullanıcının min şifre uzunluğuna bağlı
    print("Oluşturulan Şifre:", sifre)


kullanici_istekleri()
