def onluga_cevir(deger, taban):

    rakamlar = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    sonuc = 0

    for karakter in deger:

        basamak = rakamlar.index(karakter)

        if basamak >= taban:
            raise ValueError

        sonuc = sonuc * taban + basamak

    return sonuc


def tabana_cevir(sayi, taban):

    rakamlar = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    if sayi == 0:
        return rakamlar[0]

    sonuc = ""

    while sayi > 0:
        kalan = sayi % taban
        sonuc = rakamlar[kalan] + sonuc
        sayi = sayi // taban

    return sonuc


deger = input("Dönüştürülecek sayıyı giriniz: ")

kaynak_taban = int(input("Kaynak tabanı giriniz (2-58): "))
hedef_taban = int(input("Hedef tabanı giriniz (2-58): "))

try:

    if kaynak_taban < 2 or kaynak_taban > 58:
        raise ValueError

    if hedef_taban < 2 or hedef_taban > 58:
        raise ValueError

    onluk_deger = onluga_cevir(deger, kaynak_taban)

    sonuc = tabana_cevir(onluk_deger, hedef_taban)

    print("10'luk sistemdeki değeri:", onluk_deger)
    print("Sonuç:", sonuc)

except ValueError:
    print("Hatalı sayı veya taban girdiniz.")