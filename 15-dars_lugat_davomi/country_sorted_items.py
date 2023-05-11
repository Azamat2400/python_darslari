country = {
    "o'zbekiston"  : "toshkent", 
    "qozog'iston"  : "anqara", 
    "qirg'iziston" : "bishkek", 
    "tojikiston"   : "dushanbe", 
    "turkmaniston" : "ashxobod", 
    "afg'oniston"  : "tolibon"
}
print("davlatlar nomlari")
for davlat_nomi in sorted(country.keys()):
    print(davlat_nomi)

print("poytaxtlar nomlari")
for poytaxt_nomi in sorted(country.values()):
    print(poytaxt_nomi)