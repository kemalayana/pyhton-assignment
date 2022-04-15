hesaplar = {
    '1'  : {
         'ad' : 'Veli Cam',
         'sifre' : '321',
         'hesap_no' : '1',
         "bakiye" : 3000,
         'ek_hesap' : 2000,
         'max_ek_hesap' : 2000
                  },
    '2'  : {
         'ad' : 'Ali Cam',
         'sifre' : '123',
         'hesap_no' : '2',
         'bakiye' : 2000,
         'ek_hesap' : 1000,
         'max_ek_hesap' : 1000
}}

def para_cek(hesap, miktar):
    if miktar <= hesaplar[hesap]['bakiye']:
        print("Paranızı alabilirsiniz.")
        hesaplar[hesap]['bakiye'] -= miktar
    else:
        toplam = hesaplar[hesap]['bakiye'] + hesaplar[hesap]['ek_hesap']
        if toplam >= miktar:
            ek_hsp = input(f"Bakiyeniz yetersiz ek hesap kullanmak istermisiniz?(e/h)\
Ek hesap dahil çekebileceğiniz max tutar: {toplam}")
            if ek_hsp == "e":
                print("Paranızı alabilirsiniz.")
                kalan_ek = hesaplar[hesap]['ek_hesap'] - (miktar - hesaplar[hesap]['bakiye'])
                hesaplar[hesap]['bakiye'] = 0
                hesaplar[hesap]['ek_hesap']= kalan_ek
            elif ek_hsp == "h":
                print(f"{hesaplar[hesap]['hesapNo']} nolu hesabınızda {hesaplar[hesap]['bakiye']} bakiye bulunmaktadır.")
            else:
                print("Yanlış bir işlem yaptınız.")
        else:
            print("Üzgünüz, bakiyeniz yetersiz. ")
    
    print(f"Güncel Bakiyeniz: {hesaplar[hesap]['bakiye']}, Güncel Ek Hesabınız: {hesaplar[hesap]['ek_hesap']}")
    devam_mi(hesap)
    
def para_yatir(hesap, miktar):
    for i in range(1, len(hesaplar) + 1):
        if hesaplar[str(i)]['hesap_no'] == hesap:
            if hesaplar[str(i)]['ek_hesap'] <= hesaplar[str(i)]['max_ek_hesap']:
                if miktar >= (hesaplar[str(i)]['max_ek_hesap'] - hesaplar[str(i)]['ek_hesap']):
                    ana = miktar - (hesaplar[str(i)]['max_ek_hesap'] - hesaplar[str(i)]['ek_hesap'])
                    hesaplar[str(i)]['bakiye'] += ana
                    hesaplar[str(i)]['ek_hesap'] = hesaplar[str(i)]['max_ek_hesap']
                elif miktar <= (hesaplar[str(i)]['max_ek_hesap'] - hesaplar[str(i)]['ek_hesap']):
                    hesaplar[str(i)]['ek_hesap'] += miktar
                print(f"Güncel bakiyeniz: {hesaplar[hesap]['bakiye']}, Güncel ek Hesabınız: {hesaplar[hesap]['ek_hesap']}")
            elif hesaplar[str(i)]['ek_hesap'] == hesaplar[str(i)]['max_ek_hesap']:
                hesaplar[str(i)]['bakiye'] += miktar
                print(f"Güncel bakiyeniz: {hesaplar[hesap]['bakiye']}, Güncel ek Hesabınız: {hesaplar[hesap]['ek_hesap']}")
    devam_mi(hesap)
    
def hesap_sorgu(hesap):
    for i in range(1, len(hesaplar) + 1):
        if hesaplar[str(i)]['hesap_no'] == hesap:
            print(f"Merhaba {hesaplar[str(i)]['ad']}")
            sifre = input(f"Lütfen şifrenizi giriniz:")
            sifre_sorgu(sifre)
            break
        elif i == len(hesaplar) + 1 : 
            print("Yanlış hesap numarasını girdiniz.")
            break
            
def sifre_sorgu(sifre):
    for i in range(1, len(hesaplar) + 1):
        if hesaplar[str(i)]['sifre'] == sifre:
            musteri = str(i)
            menu(musteri)
            break
        elif i == len(hesaplar) + 1 :
            print("Yanlış şifre girdiniz.")
            break

def menu(musteri):
    secim = (input(f"Para çekmek için 1 i para yatırmak için 2 yi tuşlayın"))
    if secim == "1":
        tutar = int(input("Çekmek istediğiniz tutarı giriniz: "))
        para_cek(musteri, tutar)
        
    elif secim == "2":
        yatir = int(input("Yatırmak istediğiniz tutarı giriniz: "))
        para_yatir(musteri, yatir)
        
    else:
        print("Yanlış seçim yaptınız.")

def devam_mi(sorgu):
    while True:
        x = (input('Devam etmek için Evet giriniz. Çıkmak için herhangi birşey yazınız.')).capitalize()
        if x == 'Evet':
            menu(sorgu)
        else:
            print("Bizi tercih ettiğiniz için teşekkür ederiz. İyi günler dileriz.")
            break
            
sorgu = input("Lütfen hesap numaranızı giriniz: ")
hesap_sorgu(sorgu)1


