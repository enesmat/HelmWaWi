from ShoppingCart.shoppingCart import shoppingCart
import os
path = os.path.join("./../", "user.txt")

class user():
    def __init__(self, email, name, password, adresse, tel):
        self.shoppingCart = shoppingCart()
        self.email = email
        self.name = name
        self.password = password
        self.adresse = adresse
        self.tel = tel

    def speichern(self):
        print(path)
        save = open(path,"+a")
        try:
            save.writelines([f"{self.name}\n",f"{self.email}\n",f"{self.name}\n",f"{self.password}\n",f"{self.adresse}\n",f"{self.tel}\n"] )
            save.close()
        except Exception as error:
            print(error)
            save.close()
