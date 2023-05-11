# cars_0 = {'model':'ferrari', 'rang':'qizil'}
# print(cars_0['model'])
# print(cars_0['rang'])


en_uz = {'apple':'olma', 'apricot':"o'rik"}
# print(en_uz['apple'])

# mevalar = {'olma':'6000', 'tarvuz':'8000', 'qovun':'7000'}
# print(f"Olma narxi {mevalar['olma']} so'm")


# talaba_0 = {'ismi':'Murod', 'yoshi':'22', 'yili':'2000'}
# print(f"\n{talaba_0['ismi'].title()},\
# {talaba_0['yili']}-yilda tug'ilgan,\
# {talaba_0['yoshi']} yoshda ")

# # yangi kalit qo'shish
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'


# # kalitni o'chirish
# del talaba_0['yoshi']

# print("\n",talaba_0)


telefonlar = {
    'ali' : 'iphone x',
    'vali' : 'galaxy s9',
    'olim' : 'mi 10 pro',
    'orif' : 'nokia 3310',
    'anvar' :'3xl'
}

# .get() metodi
# meva = en_uz.get('pineapple','Bunday meva mavjud emas')
# print(meva)

telefon = telefonlar.get('hasan','Bunday ism mavjud emas')
# telefonlar.get('hasan')
