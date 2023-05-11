# # while() shart operatori  (tarjima: toki)
# son = 1
# while son<=5:
#     print(son, end=' ')
#     son += 1


# savol = "istalgan son kiriting \
# (dasturni to'xtatish uchun 'exit' deb yozing): >>>"

# qiymat = ''

# while qiymat != "exit":
#     qiymat = input(savol)
#     if qiymat != "exit":
#         print(float(qiymat)**2)
# print("dastur tugadi")



# # ishora  [flag] (bir nechta shart tekshirilishi uchun)
# savol = "istalgan son kiriting \
# (dasturni to'xtatish uchun 'exit' deb yozing): >>>"
# ishora = True

# while ishora:
#     qiymat = input(savol)
#     if qiymat == "exit":
#         ishora =False
#     else:
#         print(float(qiymat)**2)
# print("dastur tugadi")


# # break while  =>  tsiklni to'xtatish
# savol = "istalgan son kiriting \
# (dasturni to'xtatish uchun 'exit' deb yozing): >>>"
# qiymat = ''

# while True:  # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == "exit":
#         break  # tsiklni to'xtatish  
#     else:
#         print(float(qiymat)**2)
# print("dastur tugadi")


# # break => for da ham ishlatiladi
# sonlar = list(range(1,11))
# for son in sonlar :
#     if son == 5:
#         break
#     print(f"{son}ning kvadrati: {son**2}")


# # continue => tsiklni boshiga qaytarish
# sonlar = list(range(1,11))
# for son in sonlar :
#     if son == 5:
#        continue  # tsiklni boshiga qaytarish
#     print(son**2)

# # continue while
# son = 0
# print("10 gacha toq sonlarni chiqarish")

# while son<10:
#     son += 1
#     if son%2 == 0:
#         continue
#     else: 
#         print(son)


# # infinite Loop => abadiy tsikl => dastur to'xtamaydi => mantiqiy xato
# son = 0
# while son<10:
#     # son += 1   # qolib ketti
#     if son%2 != 0:
#         continue
#     else: 
#         print(son)
   


# son = 0  # xato => abadiy sikl
# while son<10:
#     if son%2 != 0:
#         continue
#     else: 
#         print(son)
#     son += 1  # bu ifodani whiledan pastki qatorda yozish kerak edi


# son = 0  # xato => abadiy sikl
# while son>0:  # shart xato berildi => son<10 deb berilishi kerak edi
#     son += 1
#     if son%2 != 0:
#         continue
#     else: 
#         print(son)