import numpy as np

print(np.arange(10)) # 10'a kadar olan sayılar
print(np.arange(10,20)) # 10 ile 20 arasındaki sayılar
print(np.arange(20,40,2)) # 20 ile 40 arası çift sayılar

print("--------------------------------------------")
#------------------------------------------------------#
 
print(np.zeros(5))
print(np.ones(5))
print(np.ones(10)*5)

print("--------------------------------------------")
#------------------------------------------------------#
dizi = np.arange(16)
print(dizi)
matris = dizi.reshape(4,4)
print("diziyi biçimlendir \n",matris)

print("--------------------------------------------")
#------------------------------------------------------#

notlarDizisi = np.array([13,24,35,46,88,45,77,100,100,90,78,75,39,100,100])
print(notlarDizisi)
print("veriler toplamı: ", notlarDizisi.sum())
print("verilerin standart sapması: ", notlarDizisi.std())
print("en yüksek not: ",notlarDizisi.max())
print("en yüksek notun indexi: ",notlarDizisi.argmax())
print("en düşük not: ",notlarDizisi.min())
print("en düşük notun indexi: ",notlarDizisi.argmin())
print("\n")
print("50 ve üstü notlar: ", notlarDizisi[notlarDizisi>=50])
print("85 ve altında olan notlar: ", notlarDizisi[notlarDizisi<=85])
#print("50 ve 85 arası olan notlar: ", notlarDizisi[85>=notlarDizisi>=50]) bu kullanım yanlıştur
print("85 ve 100 arası notlar: ", notlarDizisi[(notlarDizisi>=85)&(notlarDizisi<=100)])
print("------------------------------------------------------------")
#-----------------------------------------------------------------------#
import numpy as np

dizi = np.array([1, 3, 2, 3, 4, 3, 5, 2, 3, 1])
print("yeni dizi: ", dizi)

# Benzersiz elemanları ve tekrar sayılarını elde edelim
degerler, tekrar_sayilari = np.unique(dizi, return_counts=True)

# 1. Önce en az ve en çok tekrar edenlerin SIRA (İNDEKS) numaralarını buluyoruz
min_indeks = np.argmin(tekrar_sayilari)
max_indeks = np.argmax(tekrar_sayilari)

# 2. Bu indeksleri kullanarak hem değerleri hem de gerçek tekrar sayılarını çekiyoruz
minTekrar = degerler[min_indeks]
minTekrarSayısı = tekrar_sayilari[min_indeks]

maxTekrar = degerler[max_indeks]
maxTekrarSayısı = tekrar_sayilari[max_indeks]

# Sonuçları yazdıralım
print("En çok tekrar eden veri: ", maxTekrar)
print(maxTekrarSayısı, " kere")
print("En az tekrar eden veri: ", minTekrar)
print(minTekrarSayısı, " kere")

