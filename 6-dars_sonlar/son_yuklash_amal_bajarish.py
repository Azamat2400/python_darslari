# son yuklash + amal bajarish + sonni o'zgartirish
sonlar = []
raqam = 1

son = float(input("\n"+str(raqam)+"-sonni kiriting: "))
sonlar.append(son)

raqam = raqam + 1

son = float(input("\n"+str(raqam)+"-sonni kiriting: "))
sonlar.append(son)

print("\n",sonlar)

# + amal bajarish
print("\n"+f'{sonlar[0]}+{sonlar[1]}=',sonlar[0]+sonlar[1])

# sonni o'zgartirish
ajr_son = 0
indeks = 0
raqam = 0

indeks = int(input("\n"+"O'zgartiriladigan son indeksini kiriting: "))
raqam= float(input("\n"+"alishtiriladigan sonni kiriting: "))

ajr_son = sonlar.pop(indeks)
sonlar.insert(indeks, raqam)

print("\n"+"Ro'yhatdagi sonlar: ",sonlar)
print("\n"+"ajratilgan son: ",ajr_son)
