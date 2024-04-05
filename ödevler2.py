#Bir fonksiyon oluşturun. Emeklilik yaşını 65 olarak belirleyin. Kullanıcıdan yaşını alıp 65 yaş altındakilere 
#emekliliğine kaç yıl kaldığını 65 yaş üstüne zaten emekli olduğunu ekrana yazdırın

def e_yashesap (e_yas):
    if (e_yas >= 65):
        print("65 yas ve üzeri zaten emeklidir")
    elif (e_yas < 65):
        g_yas = 65 - e_yas
        print("emekli olmniza daha ",g_yas,"yil daha var")

#e_yas=int(input("lütfen yaşinizi girin: "))

#e_yashesap(e_yas)


#Bir fonksiyon oluşturun.Fonksiyon kullanıcıdan iki sayı alıp bu iki sayı arasındaki asal sayıları ekrana bastırın

def fonksiyon(sayi1, sayi2):
    asal_sayilar = []
    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1:
            for İ in range(2, sayi):
                if (sayi % İ) == 0:
                    break
            else:
                asal_sayilar.append(sayi)
    return asal_sayilar

#sayi1 = int(input("1.sayiyi girin: "))
#sayi2 = int(input("2.sayiyi girin: "))

#print(sayi1, " ile " ,sayi2," arasindaki asal sayilar:",fonksiyon(sayi1, sayi2))


#İki fonksiyon oluşturun. İki fonksiyon içinde de listeler olsun ilk fonksiyon içindeki 
#listenin en büyük sayısını ikinci fonksiyon içindeki listenin en küçük sayısını toplayıp ekrana bastırın

def en_buyuk_sayi(liste):
    if not liste:
        return None
    return max(liste)

def en_kucuk_sayi(liste):
    if not liste:
        return None
    return min(liste)

liste1 = [12, 34, 2, 4, 65]
liste2 = [3, 1, 67, 5, 23]

en_buyuk_liste1 = en_buyuk_sayi(liste1)
en_kucuk_liste2 = en_kucuk_sayi(liste2)

#if en_buyuk_liste1 is not None and en_kucuk_liste2 is not None:
#    toplam = en_buyuk_liste1 + en_kucuk_liste2
#    print("iki listenin en büyük ve en küçük sayilarinin toplami: ", toplam)
#else:
#    print("en az bir liste boş...")


#Bir fonksiyon oluşturun. Fonksiyon içinde bir tane liste olsun ve bu listenin ilk ve son sayısı eşitse ekrana 
#true değilse false yazdırsın

def ilk_ve_son_sayi(liste):
    if len(liste) < 1:
        return False
    return liste[0] == liste[-1]

#liste1 = [1, 2, 3, 4, 1]
#liste2 = [5, 6, 7, 8, 9]

#print("liste1 için ilk ve son sayilar eşit mi?", ilk_ve_son_sayi(liste1))
#print("liste2 için ilk ve son sayilar eşit mi?", ilk_ve_son_sayi(liste2))


#Bir sayının palindrom sayı olup olmadığını kontrol eden fonksiyonu yazın

def palindrom(sayi):
    sayi_str = str(sayi)
    ters_sayi_str = sayi_str[::-1]
    return sayi_str == ters_sayi_str

sayi1 = 12321
sayi2 = 12345

#print(sayi1, "palindrom sayi mi?", palindrom(sayi1))
#print(sayi2, "palindrom sayi mi?", palindrom(sayi2))


#Bir fonksiyon oluşturun. Fonksiyon içinde iki liste olsun ilk listenin çift sayılarını 
#ikinci listenin tek sayılarını alıp yeni bir listeye ekleyin ve ekrana yazdır

def birlestir(liste1, liste2):
    liste = []
    for sayi in liste1:
        if sayi % 2 == 0:
            liste.append(sayi)
    for sayi in liste2:
        if sayi % 2 != 0:
            liste.append(sayi)
    print("Yeni liste:", liste)

#liste1 = [1, 2, 3, 4, 5, 6]
#liste2 = [7, 8, 9, 10, 11, 12]
#birlestir(liste1, liste2)


#Rus ruleti oyunu yazın. Random kütüphanesi kullanarak 1-6 arasında bir sayı seçilsin ve 
#kullanıcıdan bir sayı alsın eşit olduğunda oyun biter.

import random

def rus_ruleti():
    print("Rus Ruleti oyununa hoş geldiniz!")
    print("1 ile 6 arasinda bir sayi seçin ve şansinizi deneyin.")
    rus_sayisi = random.randint(1, 6)
    
    while True:
        try:
            tahmin = int(input("Tahmininizi girin (1 ile 6 arasinda bir sayi): "))
            if tahmin < 1 or tahmin > 6:
                print("Geçersiz giriş! Lütfen 1 ile 6 arasinda bir sayi girin.")
                continue
            else:
                break
        except ValueError:
            print("Geçersiz giriş! Lütfen sadece bir sayi girin.")
            continue
    
    if tahmin == rus_sayisi:
        print("Tebrikler! Doğru tahmin ettiniz. Rus Ruleti oyununu kazandiniz!")
    else:
        print("Üzgünüm, doğru tahmin edemediniz. Rus Ruleti sayi ", rus_sayisi, "idi.")
        print(" ______                    ___")
        print("/  ____|           }=>    /_ _\ ")
        print("|-|-]    *--PEW--*       |  -  |   ___GAME OVER___YOU_CANT_RETY_TRY___")
        print("|_|                       \___/")

rus_ruleti()