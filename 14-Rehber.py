while True :
    rehber = {
        "Ahmet": "5551112233",
        "Mehmet": "5554445566"
    }

    print("1- Kişi Ekle")
    print("2- Kişi Güncelle")
    print("3- Kişi Sil")
    print("4- Numara Sorgula")

    secim = input("Seçiminizi giriniz: ")

    if secim == "1":
        isim = input("İsim giriniz: ").lower()
        numara = input("Numara giriniz: ")

        rehber[isim] = numara

        print("Kişi eklendi.")
        print(rehber)

    elif secim == "2":
        isim = input("Güncellenecek kişinin adı: ").lower()

        if isim in rehber:
            yeni_numara = input("Yeni numara: ")
            rehber[isim] = yeni_numara

            print("Numara güncellendi.")
            print(rehber)
        else:
            print("Kişi bulunamadı.")

    elif secim == "3":
        isim = input("Silinecek kişinin adı: ").lower()

        if isim in rehber:
            del rehber[isim]

            print("Kişi silindi.")
            print(rehber)
        else:
            print("Kişi bulunamadı.")

    elif secim == "4":
        isim = input("Aranacak kişinin adı: ").lower()

        if isim in rehber:
            print("Numarası:", rehber[isim])
        else:
            print("Kişi bulunamadı.")

    else:
        print("Geçersiz seçim.")

    