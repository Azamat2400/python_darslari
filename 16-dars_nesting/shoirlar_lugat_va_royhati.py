muhammad = {
    "ism"      : "muhammad",
    "tahallus" : "yusuf",
    "asarlar" : ["o'zbekistonim",
                  "palaxmon", 
                  "qizg'aldoq"]
}
tora = {
    "ism"      : "to'ra",
    "tahallus" : "sulaymon",
    "asarlar" : ["do'stim",
                  "sevgi", 
                  "qizg'onaman"]
}
ahad = {
    "ism"      : "ahad",
    "tahallus" : "qayum",
    "asarlar" : ["muhabbat",
                  "ayriliq", 
                  "azob"]
}

shoirlar = [muhammad, tora, ahad]

# for shoir in shoirlar:
#     print(f"{shoir['ism']} {shoir['tahallus']} ")

for shoir in shoirlar:
    
    ism = f"{shoir['ism']} {shoir['tahallus']}"
    asarlar = shoir['asarlar']
    
    print(f"\n{ism}ning mashxur asarlari:", end=' ')
    
    for asar in asarlar:
        print(f"{asar}, ", end=' ')

