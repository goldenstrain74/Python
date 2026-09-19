# en basitinden kullandığımız print bile bir fonksiyondur. 
# Fonksiyonlar, belirli bir görevi yerine getiren kod bloklarıdır. 
# Python'da birçok yerleşik fonksiyon vardır ve kullanıcılar kendi fonksiyonlarını da oluşturabilirler.

print("Merhaba, dünya!") # print() fonksiyonu ekrana yazı yazdırır.

help(print) # help() fonksiyonu, bir fonksiyon hakkında bilgi verir.

# fonksiyonların aynı zamanda parametreleri de vardır. Parametreler, fonksiyonlara veri iletmek için kullanılır.
print("Merhaba", "dünya!", sep="-") # sep parametresi, yazdırılan değerler arasına konulacak ayırıcıyı belirler.
print("Merhaba", "dünya!", end="!!!\n") # end parametresi, yazdırılan değerlerin sonuna konulacak karakteri belirler.
print("Merhaba", "dünya!", sep="-", end="!!!\n") # sep ve end parametrelerini aynı anda kullanabiliriz.