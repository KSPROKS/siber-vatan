ad="Kerim"
soyad="Sefercik"
yas=15
a=ad+" "+soyad+" "+str(yas)
#print (a)

#print ("benim Adim:",(ad),",","Soyadim:",(soyad),",","Yasim:",str(yas))


#print(len(a))
#print(a[:12])
#print(a[8:])
#print(a[5:8])
#print(len(a[2:6]))
#print(a[::-1])


karsilamalower=a.lower
#print(karsilamalower)

karşilamaspilt=a.split()
#print(karşilamaspilt)

#print(karşilamaspilt[::-1])

karsilamajoin="-".join(a)
#print(karsilamajoin)

karsilamaswith=a.startswith("8")
#print(karsilamaswith)

karsilamareplace=a.replace("Kerim","Sefercik")
#print(karsilamareplace)