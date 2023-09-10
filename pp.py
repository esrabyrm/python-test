import random 
import string 

karakter = string.ascii_letters + string.digits 
vowels = "aeiouAEIOU" 
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" 

def sifre_olustur(length=6): 
    password =''.join(random.choice(karakter) for _ in range(6)) 
    return password 
if __name__ == "__main__": 
     password = sifre_olustur() 
print("Olusturulan sifre:", password) 
print('bu bir değişikliktir')