savol = "yoshingiz nechida? >>> "
ishora = True

while ishora:
    qiymat = input(savol)

    if qiymat == "exit" or qiymat == "quit":
        break
    
    qiymat = int(qiymat)

    if 0 <= qiymat <= 7:
        narx = 2000
    elif qiymat <= 18:
        narx = 3000
    elif qiymat <= 65:
        narx = 10000
    elif qiymat > 65:
        narx = "bepul" 
    print(f"Chipta narxi {narx} so'm")

print("dastur tugadi")