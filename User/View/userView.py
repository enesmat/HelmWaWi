from User.Controller.userController import createUser

def getUserData():
    email = input("Deine Email: ")
    name = input("Dein Name: ")
    password = input("Dein Passwort: ")
    adresse = input("Deine Adresse: ")
    tel = input("Deine Telefonnummer: ")

    createUser(email, name, password, adresse, tel)

