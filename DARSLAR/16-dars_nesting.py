# 14.05.2022y 
# 16-dars. NESTING  (ichma-ich kutubxonalar)

# # Ro'yhat ichida lug'at masalasi
# car0 = {
#     "model"   : "lacetti",
#     "rang"    : "oq",
#     "yili"    : 2018,
#     "narxi"   : 13_000,
#     "km"      : 50_000,
#     "korobka" : "avtomat"
# }
# car1 = {
#     "model"   : "nexia 3",
#     "rang"    : "qora",
#     "yili"    : 2018,
#     "narxi"   : 9_000,
#     "km"      : 89_000,
#     "korobka" : "mexanika"
# }


# cars = [car0, car1] # 2ta lug'atni ro'yhatga joyladik
# for car in cars:
# # Ro'yhatdagi car elementining modeli so'ralmoqda
#     print(f"{car['model']}, " 
#           f"{car['rang']}, "
#           f"{car['yili']}, "
#           f"{car['narxi']} $", '\n')

# # cars royhati 0-elementining model kalit so'zining qiymati
# print(cars[0]['model'])  # 1-jolat

# k = cars[0]   # 2-holat soddalashtirish
# print(k['model']) 




# malibus = []
# for n in range(10):
#     new_car = {
#         'model'   : 'malibu',
#         'rang'    : None,
#         'yili'    : 2022,
#         'narx'    : None,
#         'km'      : 0,
#         'korobka' : 'avtomat'
#     }
#     malibus.append(new_car)


# # for malibu in malibus:
# #     print(malibu)  

# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'

# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'

# for malibu in malibus[6:]:
#     malibu['rang'] = 'oq'
#     malibu['korobka'] = 'mexanika'

# # for malibu in malibus:
# #     print(malibu)

# for malibu in malibus:
#     if malibu['korobka'] == 'avtomat':
#         malibu['narx'] = 40_000
#     else: malibu['narx'] = 35_000

# for malibu in malibus:
#     print(malibu)


# # Lug'at ichidagi ro'yhat masalasi
# dasturchilar = {
#     'ali' : ['python', 'c++'],
#     'vali' : ['html', 'css', 'js'],
#     'hasan' : ['php', 'sql'],
#     'husan'  : ['python', 'php'],
#     'maryam' : ['c++', 'c#']
# }
# #   key , value       ->       .items()  
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism}, quyidagi dasturlash tillarini biladi:", end = ' ')
#     for til in tillar:
# # oxirini yangi qatordan chiqarmasdan, shu qatorga ulab yuborish
#         print(til, end = ' ') 
    
# # Ro'yhat ichida ro'yhat masalasi
hamkasblar = {
    'ali' : { 'familiya' : 'valiyev',
              'tyil' : 1995,
              'malumot' : 'oliy',
              'tillar' : ['python', 'c++']
            },
    'vali' : { 'familiya' : 'aliyev',
              'tyil' : 2001,
              'malumot' : "o'rta-maxsus",
              'tillar' : ['html', 'css', 'js']
              },
    'hasan' : { 'familiya' : 'husanov',
              'tyil' : 1999,
              'malumot' : 'maxsus',
              'tillar' : ['php', 'sql']
              }  
}

for ism, info in hamkasblar.items():
    
    print(f"\n{ism} {info['familiya']},"
          f"{info['tyil']}-yilda tug'ilgan.\n"
          f"Ma'lumoti : {info['malumot']}.\n"
          "Quyidagi dasturlash tillarini biladi:")
# Ro'yhat uchun for ishlatildi    
    for til in info['tillar']:
        print(til, end=' ')