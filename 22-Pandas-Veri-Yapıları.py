import pandas as pd
import numpy as np

etiketliVeri= pd.Series([1,2,3,4,5],["a","b","c","d","e"])
print("Dizi: \n",etiketliVeri)
print("b etiketinin değeri: ",etiketliVeri["b"])
print("\n \n")

sayilar = np.arange(0,20).reshape(4,5)
sutunlar=["a","b","c","d","e"]
satirlar=["AB","EU","GB","JP"]
tablo = pd.DataFrame(sayilar, index=satirlar,columns=sutunlar)
print(tablo)
print("\n")
# sütun Yazdırma
print("a ve d sütunu: \n",tablo[["a","d"]])
print("\n")

# satır seçme (etiket kullanılarak)
print("AB ve JP satırı: \n",tablo.loc[["AB","JP"]])
print("\n")

# satır seçme (index kullanarak)
print("EU ve GB satırı \n",tablo.iloc[[1,2]])
print("\n")

# satır sütun seçimi
print("AB satırı a ve d sütunu: \n",tablo.loc["AB",["a","d"]])
print("\n")

# veri filtreleme
print("4'den büyük ve 12'den küçük sayılar: ",tablo[(tablo<12)&(tablo>4)])
print("\n")

# fonksiyonlar
print("c stünundaki değerlerin toplamı: ",tablo["c"].sum())
print("c stünundaki değerlerin en küçüğü: ",tablo["c"].min())
print("c stünundaki değerlerin en büyüğü: ",tablo["c"].max())
print("c stünundaki değerlerin ortalaması: ",tablo["c"].mean())
print("\n")

#dosya çağırma
import os
print("Çalışma dizini:", os.getcwd())
print(os.listdir(),"\n\n\n")

dosya = pd.read_csv("22-ogrenciler.csv")

print(dosya)