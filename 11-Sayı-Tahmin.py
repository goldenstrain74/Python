import random

gizli_sayi = random.randint(1, 100)
can = 5

print("1 ile 100 arasında bir sayı tahmin edin.")
print("Toplam 5 canınız var.")

while can > 0:
    tahmin = int(input("Tahmininiz: "))

    if tahmin == gizli_sayi:
        print("Tebrikler! Sayıyı doğru bildiniz.")
        break

    elif tahmin < gizli_sayi:
        can -= 1
        print("Daha büyük bir sayı girin.")
        print("Kalan can:", can)

    else:
        can -= 1
        print("Daha küçük bir sayı girin.")
        print("Kalan can:", can)

if can == 0:
    print("Canınız bitti, doğru sayıyı bulamadınız.")
    print("Doğru sayı:", gizli_sayi)