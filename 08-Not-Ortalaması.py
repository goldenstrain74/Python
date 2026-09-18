okul_turu = input("Okul türünü giriniz (ilkokul/lise/universite): ").lower()

if okul_turu == "ilkokul":
    not1 = float(input("1. notu giriniz: "))
    not2 = float(input("2. notu giriniz: "))

    ortalama = (not1 + not2) / 2

    print("Ortalamanız:", ortalama)

    if ortalama >= 85:
        print("Pekiyi")
    elif ortalama >= 70:
        print("İyi")
    elif ortalama >= 50:
        print("Orta")
    else:
        print("Kötü")

elif okul_turu == "lise":
    not1 = float(input("1. notu giriniz: "))
    not2 = float(input("2. notu giriniz: "))

    ortalama = (not1 + not2) / 2

    print("Ortalamanız:", ortalama)

    if ortalama >= 50:
        print("Geçtiniz")
    else:
        print("Kaldınız")

elif okul_turu == "universite" or okul_turu == "üniversite":
    vize = float(input("Vize notunu giriniz: "))
    final = float(input("Final notunu giriniz: "))

    ortalama = (vize * 0.4) + (final * 0.6)

    print("Ortalamanız:", ortalama)

    if final < 50:
        print("Final notunuz 50'nin altında olduğu için FF ile kaldınız.")
    elif ortalama >= 90:
        print("Harf Notu: AA")
    elif ortalama >= 85:
        print("Harf Notu: BA")
    elif ortalama >= 80:
        print("Harf Notu: BB")
    elif ortalama >= 75:
        print("Harf Notu: CB")
    elif ortalama >= 70:
        print("Harf Notu: CC")
    elif ortalama >= 60:
        print("Harf Notu: DC")
   