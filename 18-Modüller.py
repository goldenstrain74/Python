import math
print("sinüs 45:", math.sin(45))
print("cosinüs 45:", math.cos(45))
print("5 faktöriyel:", math.factorial(5))
print("8 üzeri 3:", math.pow(8, 3))
print("Karekök 16:", math.sqrt(16))
print("Pi sayısı:", math.pi)

import random
rastgele_sayi = random.randint(1, 100)
print("1 ile 100 arasında rastgele sayı:", rastgele_sayi)

import datetime
bugun = datetime.date.today()
print("Bugün:", bugun)

simdi = datetime.datetime.now()
print("Şimdi:", simdi)

su_an = datetime.datetime.now().time()
print("Saat: [Saat:Dakika:Saniye]", su_an)