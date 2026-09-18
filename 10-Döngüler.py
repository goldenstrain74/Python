# çarpım tablosu oluşturur

sayi = int(input("Bir sayı giriniz: "))

for i in range(1, 11):
    print(sayi, "x", i, "=", sayi * i)

# doğru şifre girene kadar kullanıcıdan şifre isteyen program

sifre = ""

while sifre != "1234":
    sifre = input("Şifreyi giriniz: ")

print("Giriş başarılı.")