from User.Model.user import user #user.model.user ist der Pfad zum Modul und import user importiert die user.py datei 



def createUser(email, name, password, adresse, tel): #Eine Funktion zum erstellen eines Benutzers, welche die Parameter aus der Klammer vom Nutzer erwartet.

    createdUser = user(email, name, password, adresse, tel) #Erstellen eines Objektes user und Zuweisung auf die Variable an createdUser mit den Werten in der Klammer.
    createdUser.speichern() #Aufruf der Methode speichern() zum speichern der Benutzerdaten in eine Datei.
