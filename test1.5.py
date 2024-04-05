import os
geçerli_dizin = os.getcwd()
print(geçerli_dizin)

for i in os.listdir(geçerli_dizin):
    print(1)

new_dictinoary = os.path.join(geçerli_dizin,"yeni_dizin")
os.mkdir(new_dictinoary)
print(f"{new_dictinoary} oluştu")

os.chdir(new_dictinoary)
print(f"{new_dictinoary} dizisine gidildi.")

dosya_yolu = os.path.join(new_dictinoary),"example.txt"
with open(dosya_yolu,"w",encoding='utf-8') as file:
    file.write("Hello Wold")

os.remove("exapmle.txt")
print("dosya silindi")
os.chdir(geçerli_dizin)
print("dosya desklopa gidildi")
os.rmdir("yeni_dizim")
print("açtığın dizim silindi")