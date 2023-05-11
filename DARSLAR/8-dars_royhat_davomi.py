# # Tartiblash
# cars = ['bmw', 'merc', 'tesla', 'audi']

# cars.sort()  # alfavit bo'yicha tartiblaydi
# print(cars)

# son = [1, 40, 10, 20, 80, 70]
# son.sort()
# print(son)


# cars = ['Bmw', 'merc', 'Tesla', 'audi']

# cars.sort()
# print(cars)

# # Teskari tartiblash

cars = ['bmw', 'merc', 'tesla', 'audi'] 
# cars.sort(reverse=True)
# print(cars)

# # Qiymatni o'zgartirmasdan royhatni chiqarish
# print(sorted(cars, reverse=True))
# print(cars)

# # Ro'yhatni aylantirish (teskari tartiblash)
# cars.reverse()

# # ro'yhatdagi elementlar soni
# print(len(cars))

# # Range() funksiyasi
# sonlar = list(range(10)) # noldan 9 gacha sonlar
# print(sonlar)

# toq_sonlar = list(range(1,20,2))
# print(toq_sonlar)

# # Ro'yhatni kesish
# sonlar = [00,10,20,30,40,50,60]
# print(sonlar[1:4])

# print(sonlar[:3])  # bosh qiymat berilmasa 0-elementdan boshlaydi
# print(sonlar[2:])  # oxirgi qiymat berilmasa oxirgi elementgacha olinadi

# # Ro'yhatdan nusxa olish (boshidan oxirigacha)
# cars = ["lacetti", "nexia", "matiz", "cobalt"]
# my_cars = cars[:]

# # #Xato# 1ta ro'yhat 2 xil nomda xolos
# my_cars = cars

# List (O'zgaruvchan_ro'yhat) va Tuple (O'zgarmas_ro'yhat) farqi

kursdoshlar = ['Oybek', 'Azamat', 'Ibrohim']  # List
sinfdoshlar = ('Azamat', 'Xislat', 'Yusuf')   # Tuple

print(type(sinfdoshlar))

# (sinfdoshlar) Tuple tipida edi uni [sinfdoshlar] List (ro'yhatga aylantirish)
# sabab o'zgartirish kiritish uchun

sinfdoshlar = list(sinfdoshlar)
print(type(sinfdoshlar))

# kursdoshlar tipini Tuple tipiga aylantirish
kursdoshlar = tuple(kursdoshlar)
print(type(kursdoshlar))
# print(kursdoshlar)