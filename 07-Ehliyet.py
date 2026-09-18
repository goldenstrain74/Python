while True:
    ehliyet = input("Almak istediğiniz ehliyet türünü giriniz (A1, A2, A, B, C, D1, D): ").upper()
    # verilen cevapları büyük harfe çevirir
    okul = input("İlköğretim mezunu musunuz? (evet/hayır): ").lower() 
    # verilen cevapları küçük harfe çevirir

    if okul == "evet":
        yas = int(input("Yaşınızı giriniz: "))
        if ehliyet == "A1":
            if yas >= 16:
                print("A1 sınıfı ehliyet alabilirsiniz.")
            else:
                print("A1 sınıfı ehliyet alamazsınız. Yaşınız 16'dan büyük olmalı.")

        elif ehliyet == "A2":
            if yas >= 18:
                print("A2 sınıfı ehliyet alabilirsiniz.")
            else:
                print("A2 sınıfı ehliyet alamazsınız. Yaşınız 18'den büyük olmalı.")

        elif ehliyet == "A":
            
            if yas >= 20 :
                tecrube = input("A2 ehliyet tecrübeniz var mı? (var/yok): ").lower()
                if tecrube == "var":
                    print("A sınıfı ehliyet alabilirsiniz.")
                else:
                    print("A sınıfı ehliyet alamazsınız. A2 ehliyet tecrübeniz olması gerekir.")
            else:
                print("A sınıfı ehliyet alamazsınız. Yaşınız 20'den büyük olmalı.")

        elif ehliyet == "B":
            if yas >= 18:
                print("B sınıfı ehliyet alabilirsiniz.")
            else:
                print("B sınıfı ehliyet alamazsınız. Yaşınız 18'den büyük olmalı.")

        elif ehliyet == "C":
            
            if yas >= 21 :
                b_ehliyet = input("B sınıfı ehliyetiniz var mı? (var/yok): ").lower()
                if b_ehliyet == "var":
                    print("C sınıfı ehliyet alabilirsiniz.")

                    ticari = input("Ticari araç kullanacak mısınız? (evet/hayır): ").lower()

                    if ticari == "evet":
                        src34 = input("SRC3 veya SRC4 belgeniz var mı? (var/yok): ").lower()
                        psikoteknik = input("Psikoteknik belgeniz var mı? (var/yok): ").lower()

                        if src34 == "var" and psikoteknik == "var":
                            print("Ticari araç da kullanabilirsiniz.")
                        else:
                            print("Ehliyeti alabilirsiniz fakat ticari araç kullanamazsınız.")
                else:
                    print("C sınıfı ehliyet alamazsınız. B sınıfı ehliyetiniz olması gerekir.")
            else:
                print("C sınıfı ehliyet alamazsınız. Yaşınız 21'den büyük olmalı.")

        elif ehliyet == "D1":
            
            if yas >= 21 :
                b_ehliyet = input("B sınıfı ehliyetiniz var mı? (var/yok): ").lower()
                if b_ehliyet == "var":
                    print("D1 sınıfı ehliyet alabilirsiniz.")

                    ticari = input("Ticari yolcu taşımacılığı yapacak mısınız? (evet/hayır): ").lower()
                    if ticari == "evet":
                        src12 = input("SRC1 veya SRC2 belgeniz var mı? (var/yok): ").lower()
                        psikoteknik = input("Psikoteknik belgeniz var mı? (var/yok): ").lower()

                        if src12 == "var" and psikoteknik == "var":
                            print("Ticari minibüs şoförlüğü yapabilirsiniz.")
                        else:
                            print("Ehliyeti alabilirsiniz fakat ticari minibüs kullanamazsınız.")

                else:
                    print("D1 sınıfı ehliyet alamazsınız. B sınıfı ehliyetiniz olması gerekir.")

                
            else:
                print("D1 sınıfı ehliyet alamazsınız.")

        elif ehliyet == "D":
            

            if yas >= 24:
                b_ehliyet = input("B sınıfı ehliyetiniz var mı? (var/yok): ").lower()
                if b_ehliyet == "var":
                    print("D sınıfı ehliyet alabilirsiniz.")

                    ticari = input("Ticari yolcu taşımacılığı yapacak mısınız? (evet/hayır): ").lower()

                    if ticari == "evet":
                        src12 = input("SRC1 veya SRC2 belgeniz var mı? (var/yok): ").lower()
                        psikoteknik = input("Psikoteknik belgeniz var mı? (var/yok): ").lower()

                        if src12 == "var" and psikoteknik == "var":
                            print("Ticari otobüs şoförlüğü yapabilirsiniz.")
                        else:
                            print("Ehliyeti alabilirsiniz fakat ticari otobüs kullanamazsınız.")
                else:
                    print("D sınıfı ehliyet alamazsınız. B sınıfı ehliyetiniz olması gerekir.")
            else:
                print("D sınıfı ehliyet alamazsınız. Yaşınız 24'ten büyük olmalı.")

        else:
            print("Geçersiz ehliyet türü girdiniz.")

    else:
        print("Ehliyet almak için en az ilköğretim mezunu olmanız gerekir.")
