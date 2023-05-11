python_lugati = {
    'int' : 'butun son toifasi',
    'float' : '10 li son toifasi',
    'string' : 'matn toifasi',
    'if' : 'agar',
    'elif' : 'aksincha agar',
    'else' : 'aksincha',
    'insert' : 'kiritish',
    'append' : 'qo\'shib qo\'yish',
    'del' : 'o\'chirish',
    'print' : 'chiqarish'
}

kalit = input("\nKalit so'z kiriting! >>> ").lower()
tarjima  = python_lugati.get(kalit)

# print(python_lugati.get(kalit, "Bunday so'z mavjud emas"))

if kalit == None:
    print("Bunday so'z mavjud emas")
else :
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")