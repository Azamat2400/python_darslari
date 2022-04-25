taomlar = ['Osh', 'Manti', 'Lag\'mon', 'Chuchvara', 'Go\'ja']
print("\nTaomlar ro'yhati:",taomlar)

#  nusxa olish
nonushta = taomlar [:]
print("\nNonushta ro'yhati:",nonushta)

# nom = input("\nNonushta ro'yhatidan chiqariladigan taom:")
# nonushta.remove(nom.title())

# nom = input("\nNonushta ro'yhatidan chiqariladigan taom:")
# nonushta.remove(nom.title())

# nom = input("\nNonushta ro'yhatidan chiqariladigan taom:")
# nonushta.remove(nom.title())

# print("\nNonushtaga qolgan taomlar:",nonushta)


nom = input("\nEndi nonushta ro'yhatiga taom qo'shing:")
nonushta.append(nom.title())

nom = input("\nNonushta ro'yhatiga taom qo'shing:")
nonushta.append(nom.title())

print("\nNonushtaning yangi ro'yhati:", nonushta)

print("\nTaomlar:",taomlar)
print("\nNonushta:",nonushta)


nonushta = tuple(nonushta)
print("\nNonushta o'zgarmas ro'yhatga aylandi:",nonushta)

# [insert]ga o'xshash soddalik
taomlar[2]='Makaron'
print(taomlar)






