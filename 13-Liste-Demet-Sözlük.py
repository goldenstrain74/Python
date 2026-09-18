# Liste
karakter_liste = ["Ahmet", 100, "Savaşçı"]

# Demet
karakter_demet = ("Ahmet", 100, "Savaşçı")

# Sözlük
karakter_sozluk = {
    "isim": "Ahmet",
    "can": 100,
    "sinif": "Savaşçı"
}

print("Liste:")
print("İsim:", karakter_liste[0])
print("Can:", karakter_liste[1])
print("Sınıf:", karakter_liste[2])

print("\nDemet:")
print("İsim:", karakter_demet[0])
print("Can:", karakter_demet[1])
print("Sınıf:", karakter_demet[2])

print("\nSözlük:")
print("İsim:", karakter_sozluk["isim"])
print("Can:", karakter_sozluk["can"])
print("Sınıf:", karakter_sozluk["sinif"])

# Liste değiştirilebilir
karakter_liste[1] -= 20

# Sözlük değiştirilebilir
karakter_sozluk["can"] = 80

print("\nHasar Aldıktan Sonra")

print("Liste:", karakter_liste)
print("Sözlük:", karakter_sozluk)

# Bu satır hata verir:
# karakter_demet[1] = 80