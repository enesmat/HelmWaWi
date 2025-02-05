from User.Model.user import user



def createUser(email, name, password, adresse, tel):

    createdUser = user(email, name, password, adresse, tel)
    createdUser.speichern()
