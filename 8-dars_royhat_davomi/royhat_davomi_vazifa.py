# davlatlar royhatini saralash tartiblash

country = ["O'zbekiston", "Qozog'iston", "Qirg'iziston", 
"Tojikiston", "Turkmaniston", "Afg'oniston"]

# uzunlik = len(country)

# print("\nRo'yhatdagi davlatlar soni:", uzunlik)

# # sorted (tartiblash)
# print("\nTartiblangan:",sorted(country))

# # sorted(reverse) (teskari tartiblash)
# print("\nTartiblanmagan:", sorted(country, reverse=True))
# print("\nAsl holat:", country)

# # Reverse() orqali teskari chiqarish
# country.reverse()
# print("\nReverse() orqali teskari chiqarish:",country)

# sort() bilan tartiblash va teskari tartiblash
country.sort()
print("\nSort bilan tartiblash", country)

# sort bilan teskari tartiblash
country.sort(reverse=True)
print("\nSort(reverse) bilan teskari tartiblash:", country)