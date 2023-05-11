# yosh = int(input("\nYoshingiz nechida? >>> "))

# if yosh <= 4:
#     narx = 0
# elif yosh <= 12:
#     narx = 5000
# elif yosh <= 18:
#     narx = 8000
# else :
#     narx = 10000

# print(f"\nSizga kirish {narx} so'm")


# # kunni aniqlash
# kun = input("\nBugun nima kun? >>> ")
# harorat = float(input("\nHaroratni kiriting! >>> "))

# if (kun.lower() == "shanba" or kun.lower() == "yakshanba") and harorat >= 30:
#     print("\nBugun dam olish kuni va cho'milsak bo'ladi")
# elif (kun.lower() == "shanba" or kun.lower() == "yakshanba") and harorat < 30:
#     print("\nBugun dam olish kuni, lekin cho'milib bolmaydi!")
# else:
#     print("\nBugun ish kuni")

# # boolean
# narx = 20000
# choy = True
# salat = False

# if choy and salat:
#     narx = narx + 10000
# elif choy or salat:
#     narx = narx +5000
# else :
#     narx

# print(narx)


# # boolean murakkabrog'i

# narx = 20000
# choy = True
# salat = False
# non = 1
# kompot = 1
# assorti = 0

# if choy:
#     print("\nChoy oldi.")
#     narx = narx + 3000
# if salat:
#     print("\nSalat oldi.")
#     narx = narx + 2000

# if non:
#     print("\nNon oldi.")
#     narx = narx + 5000

# if kompot:
#     print("\nKompot oldi.")
#     narx = narx + 5000

# if assorti:
#     print("\nAssorti oldi.")
#     narx = narx + 15000

# print("\nJami narx: >>> ", narx)


# # in  
# # not in
# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']

# ovqat = input("\nSiz nima ovqat yeysiz? >>> ")

# if ovqat.lower() in menu:
#     print("\nBuyurtma qabul qilindi.")

# else :
#     print("\nAfsuski, bizda bunday ovqat mavjud emas.")

# # buyurtmani tekshirish
# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']
# if buyurtmalar:
#     for taom in buyurtmalar:
#          if taom in menu:
#              print(f'\nMenuda {taom} bor.')
#          else :
#              print(f'\nAfsuski menuda {taom} yo\'q.')
# else :
#     print("\nSavatchangiz bo'sh")