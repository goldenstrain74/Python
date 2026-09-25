import numpy as np
dizi = np.array([1,2,3,4,5,6])
print("NumPy başarı ile kuruldu")
print("dizi:",dizi)
print("--------------------------------------------")
#-------------------------------------------------------#

pyListe= [1,2,3,4,5,10,10,50,22]
npListe= np.array(pyListe)
print("python listesi: \n",pyListe, "\n Tipi",type(pyListe))
print("numPy listesi: \n",npListe,"\n Tipi:", type(npListe))

print("--------------------------------------------")
#-----------------------------------------------------------#

sayilar= np.array([1,2,3,4,5,10,15,22,30,50,200])
print("dizi: ", sayilar)
print("ilk iki sayı:", sayilar[0:2])
print("son beş sayı: ",sayilar[-5:])
print("bir dört index arası sayılar: ",sayilar[1:4])
print("3. indexten sonraki sayılar: ",sayilar[2:])



