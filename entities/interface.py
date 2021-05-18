

import mysql.connector
from mysql.connector import errorcode as er

class Interface:


    def __init__(self):
        pass
    
    def welcome(self):

        welcome = "# Bienvenue dans OpenFoodFact Comparateur. #"
        nextmenu = "#    Appuyez sur Entrée pour continuer.    #"
        print()
        print()
        for characters in welcome:
            print("#", end = "")
        print()
        print(welcome)
        print(nextmenu)
        for characters in welcome:
            print("#", end = "")
        print()
        print()

    def menuprompt(self):
        menu = {
            1 : 'Chercher un nouveau produit.',         #open new menu with categories
            2 : 'Afficher les favoris.',                #open a array with all the favorites from the database table.
            3 : 'Mettre a jour la base de données.',    #calls the writemanager and all his method in the right order.
            4 : 'Quitter le programme.'                 #asks : "do you want to quit? (y/n)" and return to main menu if no and quit if yes.
        }
        for key, values in menu.items():
            print(key, ":" ,values)

        userinput = input("Entrez votre choix: ")
        try:
            int(userinput)
            it_is = True
        except ValueError:
            it_is = False
            print("Veuillez entrer un choix valide. (1-4)")

        if userinput == 1:
            self.newproduct()
        elif userinput == 2:
            self.favorites()
        elif userinput == 3:
            self.updatedb()
        else:
            self.exitmenu()



    def newproduct(self, category):
        pass
        #takes a parameter of the returned value of categories.
        
    def categories(self):
        pass
        #from categories in database:
            #select 5 random categories.
                #return those categories.
    #categories = categories()
    #create menu 
            
    def favorites(self):
        pass
        #display an array of the surrogate table.
    
    def updatedb(self):
        pass

    def exitmenu(self):
        
        userinput = input("Voulez-vous quitter le programme? (y/n) : ")

        try:
            userinput.lower() == "y" or userinput.lower() == "n"
        except ValueError:
            print("Veuillez entrer une réponse valide. (y/n) ")
        
        if userinput.lower() == "y":
            exit
        else:
            self.menuprompt()