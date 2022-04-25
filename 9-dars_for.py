# mehmonlar = ["Ali", "Vali", "Sobir", "Hamid"]
# for mehmon in mehmonlar:
#     print("salom,", mehmon)

dostlar = []
print("5ta do'stingiz ismini kiriting")

for n in range(5):
    dostlar.append(input(f"{n+1}-do\'stingiz ismini kiriting:").title())

print(dostlar)