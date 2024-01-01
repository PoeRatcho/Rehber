sözlük = {}
while True:
    print("""
[1]: Yeni Kişi Ekleme
[2]: Kişi Sorgulama
[3]: Kişiyi Silme
[Q]: Çıkış
    """)
    
    veri = input("Yapmak İstediğiniz İşlemi Tuşlayınız: ")
    if veri == "1":
        isim = input("Kişinin Adını Giriniz: ")
        numara = input("Numarayı Yazınız: ")
        sözlük.setdefault(isim,numara)
    elif veri == "2":
        sor = input("Sorgulamak İstediğiniz İsimi Giriniz: ")
        if sor in sözlük.keys():
            print(sözlük.get(sor))
        else:
            print("Aranan Kişi Rehberde Bulunamadı...")
    elif veri == "3":
        silme = input("Kimi Silmek İstiyorsunuz?: ")
        varmı = silme in sözlük.keys()
        if varmı:
            sözlük.pop(silme)
        else:
            print("Silmek İstediğiniz {} Kişisi Bulunamadı" .format(silme))
    elif veri == "q" or veri == "Q":
        break
    else:
        print("Hatalı Tuşlama Yaptınız Tekrardan Deneyiniz....")