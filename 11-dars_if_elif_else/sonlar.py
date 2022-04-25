butun_son = int(input("\nBiror butun son kiriting! >>> "))

for n in range(2,11) :
    if not butun_son%(n) :
        print(f'\nSiz {butun_son} sonini kiritdingiz va u {n} ga qoldiqsiz bo\'linadi')