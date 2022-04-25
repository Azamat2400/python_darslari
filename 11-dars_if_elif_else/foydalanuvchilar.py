users = ['ali', 'vali', 'gani', 'bobur', 'bunyod']
login = input("\nYangi login kiriting! >>> ")

if login.lower() in users:
    print("\nLogin band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz, {login.title()}!")