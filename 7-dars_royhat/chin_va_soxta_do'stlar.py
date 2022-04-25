# ro'yhatga indeks orqali qiymat qo'shish + royhatni o'zgartirish

dostlar = []
yaramas_dostlar = []
indeks = 0
ism = "null"

indeks= int(input("\nindeksni kiriting: "))
ism = input("ismni kiriting: ")
dostlar.insert(indeks, ism.title())

indeks= int(input("\nindeksni kiriting: "))
ism = input("ismni kiriting: ")
dostlar.insert(indeks, ism.title())

indeks= int(input("\nindeksni kiriting: "))
ism = input("ismni kiriting: ")
dostlar.insert(indeks, ism.title())

print("Ro'yhatdagi do'stlar: ",dostlar)

indeks = int(input("\nshubhali ism indeksini kiriting: "))

# kiritilgan indeksdagi ismni [ism]ga o'zlashtiradi
ism = dostlar.pop(indeks) 

# [ism]ni [yaramas_dostlar] ro'yhatiga qo'shadi
yaramas_dostlar.append(ism.title())

print("\n",indeks,"-indeksdagi do'stingiz bo'lmish ",ism.title(),
"shubhali ekan,demak ismini almashtiring!")

# [indeks] joyiga alishtiriladigan nomni kiritish
ism =  input("\nalishtiriladigan nomni kiriting: ")

dostlar.insert(indeks,ism.title())



indeks = int(input("\nshubhali ism indeksini kiriting: "))

# kiritilgan indeksdagi ismni [ism]ga o'zlashtiradi
ism = dostlar.pop(indeks) 

# [ism]ni [yaramas_dostlar] ro'yhatiga qo'shadi
yaramas_dostlar.append(ism.title())

print("\n",indeks,"-indeksdagi do'stingiz bo'lmish ",ism.title(),
"shubhali ekan,demak ismini almashtiring!")

# [indeks] joyiga alishtiriladigan nomni kiritish
ism =  input("\nalishtiriladigan nomni kiriting: ")

dostlar.insert(indeks,ism.title())


print("Chin do'stlar: ",dostlar)

print("Soxta do'stlar: ",yaramas_dostlar)