dostlar = {
    "oybek"   : ['ivan vasilevich', 'shurik', 'karib dengiz'],
    'ibrohim' : ['temir xotin', 'maryam', "sevgi iztirobi"],
    'elbek_s'   : ['jumong', 'samuray', 'xitoycha sevgi']
}

for ism, kinolar in dostlar.items():
    
    print(f"\n{ism}ning sevimli filmlari :", end=' ')
    
    for kino in kinolar:
        print(kino, end=', ')
