'''
toplam = 5
liste = []
for i in range(toplam):
    değer = int(input("yeni bir değer giriniz: "))
    if değer % 3 == 0:
        liste.insert(0,değer)
    else:
        liste.append(değer)
print("listenin son hali",liste)
'''
'''
class Kişi:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}{self.age}"

k1 = Kişi(name="Kerim",age=15)
print(k1)
'''
class Soru:
    def __init__(self,soru,cevap):
        self.soru = soru
        self.cevap = cevap
    def doğru_mu(self,tahmin):
        return self.cevap == tahmin
soru1 = Soru("başkent neresidir : ","ankara")
soru2 = Soru("en kalabalık şehir hangi şehrimizdir : ","istanbul")
soru3 = Soru("en güzel şehrimizneresidir : ","bursa")
doğru_cevaplar = 0
sorular = [soru1,soru2,soru3]
for i in sorular:
    cevap = input(i.soru)
    if i.doğru_mu(cevap):
        doğru_cevaplar += 1
print(f"doğru cevap sayısı {doğru_cevaplar}")