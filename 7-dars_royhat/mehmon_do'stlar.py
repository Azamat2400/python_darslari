# ro'yhatga indeks orqali qiymat qo'shish + royhatni o'zgartirish

friends = []
mehmonlar = []
indeks = 0
ism = "null"

indeks= int(input("\nRo'yhatdagi tartib nomerini kiriting: "))-1
ism = input("\nDo'stingiz ismini kiriting: ")
friends.insert(indeks, ism.title())

indeks= int(input("\nRo'yhatdagi tartib nomerini kiriting: "))-1
ism = input("\nDo'stingiz ismini kiriting: ")
friends.insert(indeks, ism.title())

indeks= int(input("\nRo'yhatdagi tartib nomerini kiriting: "))-1
ism = input("\nDo'stingiz ismini kiriting: ")
friends.insert(indeks, ism.title())

print("\nRo'yhatdagi do'stlar: ",friends)



indeks = int(input("\nMehmonga kela oladigan do'stingiz tartibini kiriting: "))-1

# kiritilgan indeksdagi ismni [ism]ga o'zlashtiradi
ism = friends.pop(indeks) 

# [ism]ni [mehmonlar] ro'yhatiga qo'shadi
mehmonlar.append(ism)

print("\n",indeks,"-indeksdagi do'stingiz bo'lmish",ism,"mehmonga kela olar ekan.")

print("\nDo'stlar ro'yhati: ",friends)



indeks = int(input("\nMehmonga kela oladigan do'stingiz tartibini kiriting: "))-1

# kiritilgan indeksdagi ismni [ism]ga o'zlashtiradi
ism = friends.pop(indeks) 

# [ism]ni [mehmonlar] ro'yhatiga qo'shadi
mehmonlar.append(ism)

print("\n",indeks,"-indeksdagi do'stingiz bo'lmish",ism,"mehmonga kela olar ekan.")


print("\nMehmonga keladigan do'stlar ro'yhati: ",mehmonlar)

print("\nMehmonga kela olmaydigan do'stlar ro'yhati: ",friends)