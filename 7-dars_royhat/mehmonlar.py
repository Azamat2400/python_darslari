# .remove() metodi yordamida kela olmaydigan mehmonlarni royhatdan chiqarish: +

# + ro'yhat o'rtasiga, boshiga va oxiriga ism kiritish

friends = []
ism = "null"

ism = input("\nMehmonga chaqirmoqchi bo'lgan do'stingiz ismini kiririting: ")
friends.append(ism.title())

ism = input("\nMehmonga chaqirmoqchi bo'lgan do'stingiz ismini kiririting: ")
friends.append(ism.title())

ism = input("\nMehmonga chaqirmoqchi bo'lgan do'stingiz ismini kiririting: ")
friends.append(ism.title())

ism = input("\nMehmonga chaqirmoqchi bo'lgan do'stingiz ismini kiririting: ")
friends.append(ism.title())

print("\nRejadagi mehmonga keladigan do'stlar royhati: ",friends)

ism = input("\nUlar orasidan kim kela olmaydi: ")
friends.remove(ism.title())

ism = input("\nYana kim kela olmaydi: ")
friends.remove(ism.title())


print("\nFaqat mehmonga kela oladigan do'stlar: ", friends)


# ro'yhat o'rtasiga, boshiga va oxiriga ism kiritish

ism = input("\nRo'yhat o'rtasiga ism kiriting: ")

friends.insert(1,ism.title())

ism = input("\nRo'yhat boshiga ism kiriting: ")

friends.insert(0, ism.title())


ism = input("\nRo'yhat oxiriga ism kiriting: ")

friends.append(ism.title())

print("\nYangilangan ro'yhat: ",friends)