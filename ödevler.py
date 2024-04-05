#cümle al,boşluk sil,tüm harfleri küçült 
cumle = input("lütfen bir cümle giriniz: ")
yeni_cumle = cumle.replace(" ", "")
kucukcumle = yeni_cumle.strip().lower()
print(kucukcumle)

#Bir dictk oluşturun, dicte yeni bir anahtar-değer çifti ekleyin, ardından bir anahtarı silin
dict = {"anahtar1": "değer1", "anahtar2": "değer2", "anahtar3": "değer3"}
print("oluşturulan dictionary (ekleme öncesi):", dict)
yeni_anahtar = "anahtar4"
yeni_deger = "değer4"
dict[yeni_anahtar] = yeni_deger
print("oluşturulan Dictionary (ekleme sonrasi):", dict)
silinecek_anahtar = "anahtar2"
del dict[silinecek_anahtar]
print("oluşturulan dictionary (silme sonrasi):", dict)

#İki string'i birleştirin ve ardından bir substring arayın ve konumunu bul
str1=str("Merhabalar nasilsiniz ")
str2=str("Ben iyiyim")
bilesik = str1 + str2
substring=input("lütfen bulunacak substring i girniz: ")
index = (bilesik,substring).find_substring
if index != -1:
    print(f"'{substring}' substring i birlestirilmis string icinde {index} indekste bulunuyor")
    def find_substring(main_string, substring):
        index = main_string.find(substring)
        return index
    print(bilesik[substring:])
else:
    print(f"'{substring}' substring i birlestirilmis string icinde bulunamadi")

#Kullanıcıdan bir cümle alın ve cümlenin içindeki kelimeleri alfabetik sıraya göre sıralayın
cumle = input("lütfn bir cümle girin: ")
kelimeler = cumle.split()
sirali_kelimeler = sorted(kelimeler)
print("Cümlenin içindeki kelimeler alfabetik siraya göre:")
for kelime in sirali_kelimeler:
    print(kelime)

#Kullanıcıdan bir cümle alın ve cümlenin içindeki kelimeleri alfabetik sıraya göre sıralayın
cumle = input("lütfn bir cümle girin: ")
kelimeler = cumle.split()
sirali_kelimeler = sorted(kelimeler)
print("Cümlenin içindeki kelimeler alfabetik siraya göre:")
for kelime in sirali_kelimeler:
    print(kelime)

#Kullanıcıdan bir kelime alın ve kelimenin içindeki tüm 'a' harflerini '@' ile değiştirin
kelime = input("lütfen bir kelime girin: ")
düzenlenmiş_kelime = kelime.replace("a", "@")
print("düzenlenmiş kelimeniz: ", düzenlenmiş_kelime)

#Kullanıcıdan iki string alın, bu stringleri birleştirin ve tüm karakterleri küçük harfe çevir
str1 = input("lütfen birinci stringi girin: ")
str2 = input("lütfen ikinci stringi girin: ")
birlesik= str1 + str2
kucuk_harf = birlesik.lower()
print("birleştirilmis ve küçük harfe çevrilmis string:", kucuk_harf)

#liste oluşturun ve listenin ortasındaki elemanı bulun
liste_str = input("lütfen bir liste girin (ör: 1, 2, 3): ")
liste = [int(eleman) for eleman in liste_str.split(",")]
def orta_elemani_bul(liste):
    uzunluk = len(liste)
    orta_indis = uzunluk // 2
    print ("Listenin ortasindaki eleman:", liste[orta_indis])

#Bir liste oluşturun ve listenin ortasındaki elemanı bir tuplee ekleyin
yeni_liste = [1, 2, 3, 4, 5]
tuple = (8, 9)
print ("listenizin şu an: ", yeni_liste)
yeni_liste.insert(3, tuple)
print ("yeni listeniz: ", yeni_liste)


#list = [1, 2, 3, 4, 5]
#tuple_ekle = (6, 7)
#ortasina_tuple_ekle(list, tuple_ekle)
#def ortasina_tuple_ekle(liste, tuple_ekle):
#    uzunluk = len(liste)
#    orta_index = uzunluk // 2
#    liste.insert(orta_index, tuple_ekle)

#Bir liste oluşturun ve listenin ortasındaki elemanı bir tuplee ekleyin

#Bir set oluşturun, set içine bir sayı ekleyin, ardından bu sayıyı setden çıkarın
set ={1,2,3,4,5}
print("set (ekleme öncesi):", set)
yeni_sayi = 6
set.add(yeni_sayi)
print("oluşan set (ekleme sonrasi):", set)
kaldirilacak_sayi = 6
set.remove(kaldirilacak_sayi)
print("oluşturulan set (çikarma sonrasi):", set)

#Bir tuple oluşturun, tuplein 2. ve 4. elemanlarını yeni bir tuple olarak alın
original_tuple = (1, 2, 3, 4, 5)
yeni_tuple = (original_tuple[1], original_tuple[3])
print("orijinal Tuple:", original_tuple)
print("yeni Tuple:", yeni_tuple)


#Bir dictk oluşturun, dicte yeni bir anahtar-değer çifti ekleyin, ardından bir anahtarı silin
dict = {"anahtar1": "değer1", "anahtar2": "değer2", "anahtar3": "değer3"}
print("oluşturulan dictionary (ekleme öncesi):", dict)
yeni_anahtar = "anahtar4"
yeni_deger = "değer4"
dict[yeni_anahtar] = yeni_deger
print("oluşturulan Dictionary (ekleme sonrasi):", dict)
silinecek_anahtar = "anahtar2"
del dict[silinecek_anahtar]
print("oluşturulan dictionary (silme sonrasi):", dict)

#İki string'i birleştirin ve ardından bir substring arayın ve konumunu bul
str1=str("Merhabalar nasilsiniz")
str2=str("Ben sahsen iyiyim")
bilesik = str1 + str2
substring=input("lütfen bulunacak substring i girniz: ")
index = find_substring(bilesik,substring)
if index != -1:
    print(f"'{substring}' substring i birlestirilmis string icinde {index} indekste bulunuyor")
    def find_substring(main_string, substring):
        index = main_string.find(substring)
        return index
    print(bilesik[substring:])
else:
    print(f"{substring} substringi {str1+str2} stringlerinde bulunmamaktadır")

#
hedef_string = "Merhaba dünya!"
hedef_karakter = "a"
def karakter_sayisi(hedef_string, hedef_karakter):
    sayac = 0
    for karakter in hedef_string:
        if karakter == hedef_karakter:
            sayac += 1
            if sayac > 0:
                return sayac
            else:
                print (f"{hedef_karakter} karakteri {hedef_string} içinde {sayac} kez geçiyor.")


#Bir dict oluşturun ve dictin içindeki string türündeki değerlerin karakter sayılarının toplamını bulun
dict = {
    "anahtar1": "merhaba",
    "anahtar2": "dünya",
    "anahtar3": "python",
    "anahtar4": "geliştirici"}
def karakter_sayisi_toplami(dic):
    toplam = 0
    for value in dic.values():
        if isinstance(value, str):
            toplam += len(value)
    return toplam
toplam_karakter_sayisi = karakter_sayisi_toplami(dict)
print("sözlük:", dict)
print("dtring değerlerin toplam karakter sayisi:", toplam_karakter_sayisi)


#Bir set oluşturun ve setin elemanlarını içeren bir liste oluşturun, ardından bu liste elemanlarının toplamını hesaplayın
set = {1, 2, 3, 4, 5}
liste = list(set)
toplam = sum(liste)
print("set:", set)
print("liste:", liste)
print("liste elemanlarinin toplami:", toplam)


#Bir string içinde belirli bir alt dizeyi (substring) arayın ve yerine başka bir alt dize ekleyin
str = input("lütfen bir string girin: ")
aranan_substring = input("lütfen aranacak alt dizeyi girin: ")
eklenecek_substring = input("lütfen yerine eklenecek alt dizeyi girin: ")
sonuc_str = str.replace(aranan_substring, eklenecek_substring)
print("sonuç:", sonuc_str)

