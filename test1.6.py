'''
def palindrome(kelime):
    ters_kelime = kelime[::-1]
    if kelime == ters_kelime:
       print(f"'{kelime}' bir palindrome kelime dir")
    else:
       print("\033[96m"+f"'{kelime}' bir palindrome kelime değildir (palindrome ye örnek olarak: 'neden' kelimesi)"+"\033[0m")
'''
'''
kelime = input("lütfen bir kelime girin: ")
kelime.lower(kelime)
#kelime.upper(kelime)
palindrome(kelime)
'''
'''
def ortk_elemanlar(liste1,liste2):
   ortaklar =  set()
   for i in liste1:
      if i in liste2:
         ortaklar.add(i)
   return ortaklar

liste1 = [1,2,5,7,8]
liste2 = [1,5,7,8,4]

ortaklar = ortk_elemanlar(liste1,liste2)
print(ortaklar)
'''
'''
def sıklık(liste):
   frekanslar = ()
   for eleman in liste:
      if eleman in frekanslar:
         frekanslar[eleman] += 1
      else:
         frekanslar[eleman] = 1
   return frekanslar

liste_örneği = [2,3,4,5,6,7,8,25,53,45,66,4,1,2,5]

sonuc = sıklık(liste_örneği)

for eleman,frekans in sonuc.items():
   print(f"{eleman} elemanı: {frekans} kez geçiyor")
'''
'''
def fibonacci(n):
    fibo = [0,1]

    for _ in range(2,n):
        fibo[-1] + fibo[-2]
        fibo.append(next)
    return fibo
n = 10
fibo = fibonacci(n)
print(f"{fibo}")
'''