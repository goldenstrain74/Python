def Selamla():
    print("Merhaba! Ben bir fonksiyonum.")

# fonksiyonlar çağırılmadığı sürece çalışmazlar.
#  Fonksiyonları çağırmak için fonksiyon adını yazıp parantez açıp kapatmamız gerekir.

Selamla() # fonksiyon çağırma

def Selamla(isim):
    print("Merhaba, " + isim + "!")

Selamla("Ahmet") # fonksiyon çağırma ve parametre gönderme

def Topla(a, b): # parametreli fonksiyon
    return a + b # return ifadesi, fonksiyonun sonucunu döndürür.

toplam = Topla(5, 10) # fonksiyon çağırma ve sonucunu bir değişkene atama
print("Toplam:", toplam) # fonksiyon sonucunu ekrana yazdırma

def Topla(*args): # args, değişken sayıda parametre alabilen bir parametredir.
    toplam = 0
    for sayi in args:
        toplam += sayi
    return toplam

print(Topla(3,5,7,10,2))

# print(Topla("ahmet", "mehmet", "ali")) int değer döndüren fonksiyona 
# string parametre gönderirsek hata alırız. Bu yüzden fonksiyonun parametre tipini
# kontrol etmeliyiz.

def Notlar (**kwargs): # kwargs, key-value (anahtar-değer) çiftlerini temsil eder.
    for ders, not_ in kwargs.items():
        print(ders + ":", not_)

Notlar(Matematik=85, Fizik=90, Kimya=78)
