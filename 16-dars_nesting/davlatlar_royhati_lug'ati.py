davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':34_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }

kirit = input("Biror davlat kiriting! >>> ").lower()

if kirit in davlatlar:
    print(f"{kirit} haqidagi malumotlar")
    
    davlat_nomi = davlatlar[kirit]
    
    print("poytaxti:",davlat_nomi['poytaxt'])
    print("maydoni:",davlat_nomi['maydon'])

else: print("Bizda bu haqida ma'lumot yo'q")