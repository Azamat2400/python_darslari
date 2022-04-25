# # Tartiblash
# cars = ['bmw', 'merc', 'tesla', 'audi']

# cars.sort()
# print(cars)

# # katta kichik harfda tartiblash
# cars = ['Bmw', 'merc', 'Tesla', 'audi']

# cars.sort()
# print(cars)

# Teskari tartiblash
# import re


# cars = ['bmw', 'merc', 'tesla', 'audi'] 
# # cars.sort(reverse=True)
# # print(cars)

# # Qiymatni o'zgartirmasdan royhatni chiqarish
# print(sorted(cars, reverse=True))
# print(cars)

# # ro'yhat uzunligi
# print(len(cars))

# # Range() funksiyasi
# sonlar = list(range(0,10))
# print(sonlar)

# toq_sonlar = list(range(1,20,2))
# print(toq_sonlar)

# # Ro'yhatni kesish
# sonlar = [00,10,20,30,40,50,60]
# print(sonlar[1:4])

# # bosh qiymat berilmasa 0-elementdan boshlaydi 
# print(sonlar[:3])

# # oxirgi qiymat berilmasa oxirgi element olinadi
# print(sonlar[2:])

# # Ro'yhatdan nusxa olish (boshidan oxirigacha)
# cars = ["lacetti", "nexia", "matiz", "cobalt"]
# my_cars = cars[:]

# # #Xato# 1ta ro'yhat 2 xil nomda xolos
# my_cars = cars

# List (O'zgaruvchan_ro'yhat) va Tuple (O'zgarmas_ro'yhat) farqi

kursdoshlar = ['Oybek', 'Azamat', 'Ibrohim']
sinfdoshlar = ('Azamat', 'Xislat', 'Yusuf')

print(type(sinfdoshlar))

# (sinfdoshlar) Tuple tipida edi uni [sinfdoshlar] List (ro'yhatga aylantirish)
# sabab o'zgartirish kiritish uchun

sinfdoshlar = list(sinfdoshlar)
print(type(sinfdoshlar))

# endi uni yana Tuple tipiga aylantirish
sinfdoshlar = tuple(sinfdoshlar)
print(type(sinfdoshlar))
# print(sinfdoshlar)