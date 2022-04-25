yosh = int(input("\nYoshinigzni kiriting! >>> "))

if yosh <= 4:
    narx = 0
elif yosh <= 18:
    narx = 10000
elif yosh >= 18:
    narx = 20000
print(f'\nSiz uchun chipta narxi {narx} so\'m')