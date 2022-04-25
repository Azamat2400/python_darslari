sonlar = []
indekslar = []
juft_sonlar = []
a = 0

k = int(input("\nNechta elementli ro'yhat yaratmoqchisiz? >>> "))

for n in range(k) :
    k = (int(input(f'\n{n+1}-elementni kiriting: >>> ')))
    sonlar.append(k)
    if k%2 == 0:
        indekslar.append(n+1)


for son in sonlar:
    if son%2 == 0 :
        juft_sonlar.append(son)
        a = a + son
print("\nRo'yhatdagi quyidagi indekslar juftdir", indekslar)
print("\nRo'yhatdagi juft sonlar: ", juft_sonlar)
print("\nRo'yhatdagi juft sonlar yig'indisi: >>> ", a, " ga teng!")
