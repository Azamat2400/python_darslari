# Kursdoshlar ro'yhatini to'ldirish

kursdoshlar = []
ism = input("Kursdoshingiz ismini kiriting: ")
kursdoshlar.append(ism)

ism = input("Kursdoshingiz ismini kiriting: ")
kursdoshlar.append(ism)

ism = input("Kursdoshingiz ismini kiriting: ")
kursdoshlar.append(ism)

print(kursdoshlar)

print('Salom, '+kursdoshlar[0].title().strip()+'!\n')
print(kursdoshlar[1].title().strip()+'jon qalaysiz?\n')
print(kursdoshlar[2].title().strip()+' tuzikmisiz?')
