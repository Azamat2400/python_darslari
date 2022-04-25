from cmath import sqrt


son = float(input("\nBiror son kiriting: >>> "))

if son > 0 :
    print(f'\nSiz kiritgan {son} > 0 ')
    print(f'{son} ning ildizi = ', son**(1/2))

elif son < 0 :
    print(f'\nSiz kiritgan {son} < 0 \nMusbat son kiriting!')

else  :
    print(f'\nSiz kiritgan {son} = 0 ')