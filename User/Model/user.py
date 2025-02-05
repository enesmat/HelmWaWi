from ShoppingCart.shoppingCart import shoppingCart #Import der Klasse shoppingCart aus dem Modul shoppingCart.py welche sich im Ordner ShoppingCart befindet.
import os #Import des os Moduls
path = os.path.join("./../", "user.txt") #Erstellt einen Pfad für user.txt im übergeordneten Verzeichnis.

class user(): #Definition einer neuen Klasse user.
    def __init__(self, email, name, password, adresse, tel): # ??? s. shoppingCart.py
        self.shoppingCart = shoppingCart()
        self.email = email
        self.name = name
        self.password = password
        self.adresse = adresse
        self.tel = tel

    def speichern(self): #Definition der Methode speichern.
        print(path) #Ausgabe des Wertes von path
        save = open(path,"+a") #Öffnet die Datei aus dem path. +a append und Lese- und Schreibmodus
        try:
            save.writelines([f"{self.name}\n",f"{self.email}\n",f"{self.name}\n",f"{self.password}\n",f"{self.adresse}\n",f"{self.tel}\n"] ) #Eine Liste von Strings in eine Datei, \n ist der Zeilenumbruch
            save.close() #Datei wird nach dem Schreiben gespeichert und geschlossen
        except Exception as error: #Hier werden Fehler erkannt und abgefangen und in der Variable error gespeichert.
            print(error) #Fehler wird in der Konsole ausgegeben.
            save.close() #Sicherstellung dass die Datei auch wenn es einen Fehler gibt geschlossen wird.
