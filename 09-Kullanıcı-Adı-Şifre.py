gercek_kullanici_adi = "ahmet"
gercek_sifre = "1234"

kullanici_adi = input("Kullanıcı adınızı giriniz: ").lower()
sifre = input("Şifrenizi giriniz: ")

if kullanici_adi == gercek_kullanici_adi and sifre == gercek_sifre:
    print("Giriş başarılı.")
else:
    print("Kullanıcı adı veya şifre hatalı.")