suhbatdoshlar = []

k = int(input(("\nBugun nechta odam bilan suhbatlashdingiz: >>> ")))


for n in range(k):
    suhbatdoshlar.append(input(f'\n{n+1}-suhbatdoshingiz ismini kiriting: ').title())


print("\nSuhbatdoshlaringiz ro'yhati:",suhbatdoshlar)