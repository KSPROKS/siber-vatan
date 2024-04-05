#open("yenidosya.txt","w")

# "w" Write -> yazma modu , yoksa oluştutur içeriği silip ek:
# "a" Appent -> ekleme modu 
# "x" Crate -> oluşturma modu , aynısı varsa hata verir 
# "r" Read -> okuma modu 

#file = open("yenidosya.txt","w")
#print (file)
#file.close()
#file_dizin = open("C:/Users/Kutisef/Desktop/masaüstü dosyası.txt","w")
#file_dizin.colse()
#file = open("yenidosya.txt","w",encoding='utf-8')
#file.write("KERİM SEFERCİK")
#file.close()
#file = open("yenidosya.txt","a",encoding='utf-8')
#file.write("\nKERİM SEFERCİK")
#file.close()



'''
try:
    file = input("bir dosya adı girin: ")
    file = open(f"{file}.txt","x",encoding='utf-8')
except FileNotFoundError:
    print("\033[3m"+"Dosya oluşturma hatası"+"\033[0m")
finally:
    print("\033[3m"+"dosya oluşturldu"+"\033[0m")

#içerik = file.read()
#print (içerik)
'''


#file = open("yenidosya.txt","r",encoding='utf-8')
#içerik_karkter = file.read(0)
#içerik_karkter = file.read(13)
#print(içerik_karkter)
#print(file.readline(),end="")
#print(file.readline(),end="")

#liste = file.readlines()
#print(liste[0])
#print(liste[1])
#file.close()
'''
with open("yenidosya.txt","r",encoding='utf-8') as file:
    content = file.read()
    print(content)
    file.seek(10)
    print(file.tell())
    content2 = file.read()
    print(content2)
'''
'''
with open("yenidosya.txt","r+",encoding='utf-8') as file:
    file.seek(22)
    file.write("siber vatan")
'''

#with open("yenidosya.txt","r+",encoding='utf-8') as file:
#    file.write("Karabük > ALL")

'''
citylist =["Karabük","Bayburt","İzmir"]
index = 1
with open("yenidosya.txt","r+",encoding='utf-8') as file:
    for i in citylist:
        if index==len(citylist):
            file.write(i)
        else:
            file.write(i+'\n')
        index += 1
'''
'''
import math as islem

sonuc = islem.sqrt(121)
print(sonuc)

sonuc = islem.factorial(5)
print(sonuc)
'''
'''
from math import *

print(factorial(5))
print(5)
print(factorial(5))
'''

'''
import random

sonuc = random,random()
print(sonuc)
'''
'''
import random

sayilar = [0,1,2,3,4,5,6,7,8]
list=""
i=0

while i!=6:
    list+=str(sayilar[random.randint(0,len(sayilar)-1)])
    i+=1

print(list)
'''
'''
import random

sayilar = [0,1,2,3,4,5,6,7,8]
list=""
i=0

while i!=6:
    list+=str(random.choice(sayilar))
    i+=1

print(list)
'''
'''
import random

sayilar = [0,1,2,3,4,5,6,7,8]
list=[]
i=0

while i!=6:
    list.append(random.choice(sayilar))
    i+=1
print("before shuffle")
print(list)
random.shuffle(list)
print("after shuffle")
print(list)
'''
