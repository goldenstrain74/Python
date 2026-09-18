sepet = []

while True:

    urun = input("Ürün giriniz (Çıkmak için q): ")

    if urun.lower() == "q":
        break

    sepet.append(urun)

print("\nSepetiniz:")

for urun in sepet:
    print("-", urun)

print("Toplam ürün sayısı:", len(sepet))