# Tarmoqlanuvchi dastur IF operatori

# # avtolarning nomlarini turli xil chiqarish
# avtolar = ['tesla', 'bmw', 'ferrari', 'cobalt', 'lacetti']

# for avto in avtolar:
#     if avto=='bmw':
#         print("\n",avto.upper())
#     else:
#         print("\n",avto.title())



# # ism kiritish va tekshirish
# ism = input("\nIsmingizni kiriting:")

# if ism.lower() != 'ali':
#     print(f'\nUzur {ism.title()}, biz Alini kutayotgandik!')

# else:
#     print('Salom, Ali')


# # sonlar
# javob = float(input("12x6 nechchiga teng? >>> "))

# if javob!=72:
#     print("Javobingiz xato!")


# #  yoshni tekshirish
# yosh = int(input("\nYoshingizni kiriting: >>>"))

# if yosh >= 18:
#     print("\nXush kelibsiz!")
# else:
#     print("\nSizga mumkin emas!")


# login uzunligini tekshirish
login = input("\nLogin kiriting: >>>")

if len(login)<=5:
    print("\nLogin 5 belgidan ko'proq bo'lishi shart!")


# x va y qiymatlarni taqqoslash
x, y =25, 50

print("x<y") if x<y else print("x>y")