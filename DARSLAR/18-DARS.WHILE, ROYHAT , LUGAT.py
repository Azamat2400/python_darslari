# print("Do'stlaringiz royhatini tuzamiz!")
# ismlar = []
# n = 1
# while True:
#     ism = input(f"{n}-do'stingiz ismini kiriting! >>> ")
#     ismlar.append(ism)
#     takrorlash = input("yana ism kiritasizmi? ha/yo'q >>> ")
#     n += 1
#     if takrorlash != "ha":
#         break
# print("Do'stlaringiz ro'yhati:")
# for ism in ismlar:
#     print(ism.title())



# print("Do'stlar yoshini saqlaymiz!")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting! >>> ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting! >>> ")
#     dostlar[ism] = int(yosh)

#     javob = input("yana ma'lumot qo'shasizmi? ha/yo'q >>> ")
#     if javob == "ha":
#         ishora = True
#     elif javob == "yo'q":
#         ishora = False
#     else: print("tushunarsiz ma'lumot kiritdingiz")

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")


# # .remove ni bir necha marta takrorlash
# cars = ['lacetti', 'nexia', 'cobalt', 'nexia', 'matiz', 'nexia']

# while 'nexia' in cars:
#     cars.remove('nexia')  # ro'yhatdan har bir 'nexia'ni o'chiradi

# print(cars)


# talabalar = ['olim', 'husan', 'hamid']
# baholangan_talabalar = {}

# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting! >>> ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho)

# for talaba, baho in baholangan_talabalar.items():
#     print(f"{talaba.title()} {baho} oldi.")

