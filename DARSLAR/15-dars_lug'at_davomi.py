# .items() metodi (elementlar degani)
# telefonlar = {
#     'ali'   : 'iphone x',
#     'vali'  : 'galaxy s9',
#     'olim'  : 'mi 10 pro',
#     'orif'  : 'nokia 3310',
#     'anvar' :'3xl'
# }

# print(telefonlar.items())  # kalit + qiymat ko'rinishida chiqaradi

# for key, value in telefonlar.items():
#     print(f"Kalit: {key}")
#     print(f"Qiymat: {value} \n")


# for key, value in telefonlar.items():
#     print(f"{key.title()}ning telefoni {value}")

# # .keys metodi
# # faqat kalitlar chiqadi
# mahsulotlar = {
#     "olma"  : 10000,
#     "anor"  : 20000,
#     "uzum"  : 15000,
#     "anjir" : 30000
# }
# print(mahsulotlar.keys())

# print("Do'kondagi mahsulotlar: ") # 1-holat
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot)

# for mahsulot in mahsulotlar: # 2-holat ## 2ta holatda ham bir xil qiymat
#     print(mahsulot)

# # .values() metodi

# telefonlar = {
#     'ali'   : 'iphone x',
#     'vali'  : 'galaxy s9',
#     'olim'  : 'mi 10 pro',
#     'orif'  : 'nokia 3310',
#     'anvar' :'3xl'
# }

# print("Foydalanuvchilar quyidagi telefonlarni ishlatadilar: ")
# for tel in telefonlar.values():
#     print(tel)

# mahsulotlar = {
#     "olma"  : 10000,
#     "anor"  : 20000,
#     "uzum"  : 15000,
#     "anjir" : 30000
# }

# bozorlik = ["anor", "uzum", "non", "baliq"]
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot} {mahsulotlar[mahsulot]} so'm")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"iltimos, do'koningizga {buyum} ham olib keling")

# # Lug'at elementlarini tartib bilan chiqarish
# mahsulotlar = {
#     "olma"  : 10000,
#     "anor"  : 20000,
#     "uzum"  : 15000,
#     "anjir" : 30000
# }
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# # set funksiyasi (bir xil nomlarni bittasini oladi)
# # set ichidagi elementlarga indeks orqali murojat qilib bo'lmaydi.

# telefonlar = {
#     'ali'    : 'iphone x',
#     'vali'   : 'galaxy s9',
#     'olim'   : 'mi 10 pro',
#     'hamida' : 'galaxy s9',
#     'maryam' : 'huawei p30',
#     'tohir'  : 'iphone x',
#     'umar'   : 'iphone x',
# }

# print("Foydalanuvchilar quyidagi telefonlarni ishlatadilar: ")
# for tel in set(telefonlar.values()):
#     print(tel)
# # set ham ma'lumot turi (lekin takrorlanmas qilib chiqaradi)
toys = {"ball", "car", "lamp", "ball", "bear", "car"}
print(type(toys))

print(toys) 
