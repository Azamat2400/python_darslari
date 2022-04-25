mahsulotlar = ['Piyoz', 'Kartoshka', 'Sabzi', 'Bodring', 'Pamidor',
'Olma', 'Uzum', 'Nok', 'Anor', 'Behi']
savat = []


print("\n5 ta mahsulot kiriting! ")


for n in range(5):
    savat.append(input(f'\n{n+1}-mahsulotni kiriting! >>> ').title())

bor_mahsulotlar = []
mavjud_emas = []

for taom in  savat:
    if taom in mahsulotlar:
        print(f'\n{taom} mahsuloti do\'konimizda bor')
        bor_mahsulotlar.append(taom.title())
    else:
        print(f'\n{taom} mahsuloti do\'konimizda yo\'q')
        mavjud_emas.append(taom.title())


print("\nQuyidagi mahsulotlar do'konimizda bor: >>> ", bor_mahsulotlar)

if mavjud_emas:
    print("\nQuyidagi mahsulotlar do'konimizda yo'q: >>>",mavjud_emas)
else :
    print("\nSiz so'ragan barcha mahsulotlar do'konimizda bor!")


