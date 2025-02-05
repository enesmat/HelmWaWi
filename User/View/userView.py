from User.Controller.userController import createUser #Die Funktion createUser aus dem Modul userController wird importiert.

def getUserData(): #Defintion einer Funktion
    email = input("Deine Email: ") #Eingabeaufforderung
    name = input("Dein Name: ")
    password = input("Dein Passwort: ")
    adresse = input("Deine Adresse: ")
    tel = input("Deine Telefonnummer: ")

    createUser(email, name, password, adresse, tel) #Nachdem alle Benutzerdaten eingegeben wurden, werden diese an createUser übergeben?

