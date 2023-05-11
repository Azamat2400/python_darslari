davlatlar = {
    "o'zbekiston"  : "toshkent", 
    "turkiya"      : "anqara", 
    "qirg'iziston" : "bishkek", 
    "tojikiston"   : "dushanbe", 
    "turkmaniston" : "ashxobod", 
    "afg'oniston"  : "tolibon"
}
country = input("Birorta davlat kiriting! ").lower()
capital = davlatlar.get(country)

if capital == None:
    print("bu haqida ma'lumot yo'q")
else:
    print(f"{country.title()}ning poytaxti : {capital.title()}")  