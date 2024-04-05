def faktoriel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriel(n-1)

#sayi=6
#print (faktoriel(sayi))


x = "golbal değişken"

def function():
    x = "local değişken"
    print(x)

#function()
#print(x)


#Eror codes:


#print(a)   vaule eror

#int(a19)   vaule eror

#print(10/0)    syntx eror

#print("hello"wold)   zero division


''' ???
while True:
    try:
      x = int(input("x giriniz:"))
      y = int(input("y giriniz:"))
      print(x/y)
    except ZeroDivisionError:
      print("sifira bölünme hatasi")

    except SyntaxError:
       

    except NameError:
       

    except Exception as ex:
      print("x ve y için sayisal değer giriniz",ex)

    else:
      break
    finally:
      print("herşey yolunda")


'''
import re
def parola_kontrol(parola):
    if len(parola)<8:
        raise Exception("parola en az 8 karakter olbailir")
    elif not re.search("[A-Z]",parola):
      raise Exception("parola büyük harf içermelidir")
    elif not re.search("[@,*,?,-,_,!,.,:,#,']",parola):
      raise Exception("parolaniz özel karakter içermelidir")
    else:
        print("parolaniz oldukça güçlüdür")

passwold=input("lütfen bir şifre girin: ")
try:
    parola_kontrol(passwold)
except Exception as ex:
    print (ex)


