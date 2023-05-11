menu ={
    "osh"       : 20_000,
    "manti"     : 4_000,
    "xonim"     : 3_000,
    "sho'rva"   : 15_000,
    "lag'mon"   : 16_000,
    "moshgo'ja" : 15_000,
    "bishteks"  : 12_000,
    "shashlik"  : 13_000,
    "somsa"     : 6_000,
    "gumma"     : 2_000
}
buyurtmalar = []

print("3ta ovqat buyurtma qiling! ")
for n in range(3):
    buyurtmalar.append(input(f'{n+1}-ovqat >>> ').lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma} {menu[buyurtma]} so'm")
    else:
        print(f"bizda {buyurtma} taomi yo'q")