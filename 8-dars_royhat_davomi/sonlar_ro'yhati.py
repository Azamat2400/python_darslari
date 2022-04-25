# range() 120 dan 150 gacha juft sonlarni chiqarish

juft_sonlar = list(range(120,150,2))
print(juft_sonlar)

# # yig'indini hisoblash
# print(sum(juft_sonlar))

# # eng katta va eng kichik son ayirmasi
# print(max(juft_sonlar)-min(juft_sonlar))

# element soni
olcham = len(juft_sonlar)
print(olcham)

# ro'yhat boshidan 5ta o'rtasidan 5ta oxiridan 5ta son chiqarish
print("\nRo'yhat boshidan 5ta son:",juft_sonlar[:5])
print("\nRo'yhat o'rtasidan 5ta son:",juft_sonlar[int(olcham/2)-2:int(olcham/2)+3])
print("\nRo'yhat oxiridan 5ta son:",juft_sonlar[-5:])
