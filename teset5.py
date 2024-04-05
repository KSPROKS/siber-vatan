#a,b,c,d=50,40,70,100
#sonuc=(a>b)
#rint(sonuc)
#onuc=(a<c)
#rint(sonuc)
#sonuc=(a==d)
#print(sonuc)
#sonuc=(c<d)
#print(sonuc)


#name1="Kerim"
#name2="Ahmet"
#name3="Enes"
#username=str(input("lütfen isminizi girin: "))
#if username == (name1 or name2 or name3):
#    print("Hoşgeldin ",username)
#else:
#    print ("Giriş kabul edilmedi")


#name1="Kerim"
#name2="Ahmet"
#name3="Enes"
#username=str(input("lütfen isminizi girin: "))                    #####
#sonuc1 = (username == name1)
#sonuc2 = (username == name2)
#sonuc3 = (username == name3)
#print ("Hoşgedin",((sonuc1 = True))


#kullanıcıdan alınan e mail ve şifrenin önceden tanımlnmış sözlük içerisinde bulunup bulunmadığını bulan ve yazdırın
#users={
#    "ks@gmail.com":123456,
#    "1234@gmail.com":123
#}
#print("-""-""-""Welcome""-""-""-")
#print("lütfen bilgileriniz girin")
#input_mail=input("Mail giriniz: ")
#input_şifre=input("Şifrenizi giriniz: ")
#sonuc_mail=(input_mail in users.keys())
#sonuc_şifre=(input_şifre in users.values())
#sonuc_final=(sonuc_mail==sonuc_şifre)
#print("Eşleşme sağlandi")


#friuts ={"elma","muz","portakal","kiwi"}
#("kiraz" in friuts)


#x = y = [10,20,30]
#z = [10,20,30]
#print(x is y)
#print(x is y)
#print(x == y)


#sayi = int(input("lütfen bir sayi girin: "))
#sayi > -1
#modu = sayi % 2
#sonuc =(modu == 0)
#print (sonuc)

#sayi = int(input("lütfen bir sayi girin: "))
#result = (sayi > 0) and (sayi % 2 == 0)
#print ("sonuc...: " +str(result))


#x = 98
#y = 62
#if (x>y):
#    print("En büyük sayi: ",x)
#    "eğer koşul doğru (True)ise çslişacak kodlar"
#elif(x==y):
#    print("sayilar eşittir")
#else:
#    print("en küçük sayi: ",y)
#    "eğer koşul yanliş (False)ise çalişcak kodlar"



#takim=input("sevdiğiniz takimin adni girniz: ")
#if(takim == "galatasaray"):
#    print("senin sevdiğin renk:kirmizi,sari")
#elif(takim == "beşiktaş"):
#    print("senin sevdiği renk:beyaz,siyah")
#elif(takim == "fenerbahçe"):
#    print("senin sevdiğin renk:lacivert,sari")
#elif(takim == "karabük kardemir spor"):
#    print ("senin sevdiğin renk: bordo,lacivert")


print("-----HESAPMAKİNESİNE-HOŞGELDİNİZ-----\n \n"
      "Toplama için-1  \n"
      "Çikarma için-2  \n"
      "Çarpma için-3  \n"
      "Bölme için-4  \n")
işlem = int(input("Hangi işlemi tercih edersiniz?"))
a =int(input("1. sayiyi girin:"))
b =int(input("2. sayiyi girin:"))

if (işlem == 1):
    print(a+b)
elif (işlem == 2):
    print(a-b)
elif (işlem == 3):
    print(a*b)
elif (işlem == 4):
    print(a/b)
else:
    print("geçerli bir işlem giriniz")