'''def sayicontrol (sayi):
    rakam_str = str(sayi)
    if len(set(rakam_str)) == 1:
        return 1
    else:
        return 0

A=[233,45,777,999999,30,90,11,61]
for sayi in A:
    if sayicontrol(sayi):
        print((sayi)"basamak aynı")
    else:
        print((sayi)"basamak farklı")
???
'''

'''
liste = [10,20,30]
print(type(liste))
'''
'''
class Person:
    def __init__(self,name,lname,adres,doğumyıl):
        self.name = name
        self.lname = lname
        self.adres = adres
        self.doğumyıl = doğumyıl
    def intro(self):
        print("merhaba ben "+self.name)
        print("soyadım "+self.lname)
        print("adres bilgim "+self.adres)
        print("doğum yılım "+self.doğumyıl)
    def bilgi(self):
        return ???

p1 = Person("Kerim","Sefercik","Safranbolu","2009")
#print(p1)
#print("benim adım",p1.name,", soyadım",p1.lname, ", adresim",p1.adres)

#p1.intro()bilgi


p1.bilgi()
???
'''
'''
class Daire:
    pi = 3.14
    def __init__(self,yarıçap):
        self.yarıçap = yarıçap
    def çevre_hesaplama(self):
        return 2* self.pi * self.yarıçap

daire1 = Daire(9)
daire2 = Daire(14)

print(daire1.çevre_hesaplama())
print(daire2.çevre_hesaplama())
'''
'''
class Sqcuare:
    def __inint__ (self,kenar):
        self.kenar = kenar
    def alanhesaplama(self):
        return self.kenar * self.kenar

kenar = Sqcuare(9)
print(kenar.alanhesaplama())

???
'''