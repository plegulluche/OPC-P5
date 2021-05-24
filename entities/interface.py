import mysql.connector
from mysql.connector import errorcode as er

import config
from readmanager import Readmanager
from databasecreator import Dbmanager
from writemanager import Writemanager

class Interface:


    def __init__(self):
        pass
    
    def welcome(self):                             #OK

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

        userinput = input()
        cond = True

        while cond:
            if userinput == "":
                cond = False
            
        self.menuprompt()
                
            

    def menuprompt(self):                  #OK

        menu = {
            1 : 'Chercher un nouveau produit.',         
            2 : 'Afficher les favoris.',                
            3 : 'Mettre a jour la base de données.',   
            4 : 'Quitter le programme.'                
        }
        for key, values in menu.items():
            print(key, ":" ,values)

        cond = True
        while cond:
            try:
                userinput = int(input("Entrez votre choix (1-4): "))
                if userinput in range(1,5): 
                    cond = False
                else:
                    print("Veuillez entrer un nombre valide. (1-4)")
            except:
                print("Veuillez entrer un nombre valide. (1-4)")
            
        if userinput == 1:
            self.newproduct()
        elif userinput == 2:
            self.favorites()
        elif userinput == 3:
            self.updatedb()
        else:
            self.exitmenu()

    def newproduct(self):                #OK
        
        read = Readmanager()

        #choix de la cate parmis 5 au hasard
        fivecateids = read.read5randomcate()
        fivecatename = []
        for ids in fivecateids:
            fivecatename.append(read.readcategory(ids))
        menu = {
            1 : fivecatename[0],         
            2 : fivecatename[1],                
            3 : fivecatename[2],   
            4 : fivecatename[3],
            5 : fivecatename[4]                
        }
        for key, values in menu.items():
            print(key, ":", values)
        cond = True
        while cond:
            try:
                userinput = int(input("entrez votre choix (1-5) : "))
                if userinput in range(1,6):
                    cond = False
                else:
                    raise ValueError
            except ValueError:
                print("Veuillez rentrer un nombre entre 1 et 5.")

        if userinput == 1:
            id = read.readcategory(fivecatename[0])
            self.chooseproduct(id)
        elif userinput == 2:
            id = read.readcategory(fivecatename[1])
            self.chooseproduct(id)
        elif userinput == 3:
            id = read.readcategory(fivecatename[2])
            self.chooseproduct(id)
        elif userinput == 4:
            id = read.readcategory(fivecatename[3])
            self.chooseproduct(id)
        else:
            id = read.readcategory(fivecatename[4])
            self.chooseproduct(id)
        
        
    def chooseproduct(self,idcate):
        
        read = Readmanager()
        fiveproducts = read.read5randomproduct(idcate)
        listprod = []
        for prodid in fiveproducts:
            prodname = read.readproductnameorid(prodid)
            listprod.append(prodname)
        x = 1
        for prodname in listprod:
            print(x, ":", prodname)
            x += 1
        

        cond = True
        while cond:
            try:
                userinput = int(input("Veuillez selectionner un produit (1-5) : "))
                if userinput in range(1,6):
                    cond = False
                else:
                    raise ValueError
            except ValueError:
                print("Veuillez entrer un choix valide (1-5)")

        if userinput == 1:
            print("algo avec l'idprod1")
        elif userinput == 2:
            print("algo prodid 2")
        elif userinput == 3:
            print("algo proid 3")
        elif userinput == 4:
            print("algo proid 4")
        else:
            print("algo prodid 5")
        
        #algo de substitution en fonction du produit choisi
        #surrogate(mettre l'id du produit choisi)
    def surrogate(self,value):
           #a partir du produit trouver le produit qui a le plus de categories en commun et un meilleur nutriscore.
           #si produit trouvé l'afficher sinon afficher pas d'alternative.
        pass

        #voulez vous enregistrer le produit?
        
        # cond = True
        # while cond:
        #     try:
        #         userinput = input("Voulez vous enregistrer le resultat de la recherche ? (O/N")
        #         if len(userinput) == 1 and isinstance(userinput, str):
        #             cond = False
        #         else:
        #             raise ValueError
        #     except ValueError:
        #         print("Veuillez entrer une reponse valide (O/N) ")

        # if userinput.lower() == "y":
        #     #methode pour enregistrer le produit dans la table surrogate.
    
        # #checher un nouveau produit ou retour au menu ?
        # sousmenu = {
        #             1 : "chercher un nouveau produit",
        #             2 : "Retour au menu"
        # }
        # for key, values in sousmenu.items():
        #     print(key, ":" , values)

        # cond = True
        # while cond:
        #     try:
        #         userinput = int(input("Veuillez entrer votre choix : (1-2) "))
        #         if len(userinput) == 1 and isinstance(userinput, int):
        #             cond = False
        #         else:
        #             raise ValueError
        #     except ValueError:
        #         print("Veuillez entrer un choix valide (1-2")

        # if userinput == 1:
        #     newproduct()
        # else:
        #     menuprompt()
            
            
    def favorites(self):
        print("your are inside favorites menu")
        #display an array of the surrogate table.
    
    def updatedb(self):      #revoir la mise en cache et l emplacement de la verif de condition dans les methodes de remplissage de la bd.
        
        cond = True
        while cond:
            try:
                userinput = input("Voulez vous mettre a jour la base de données? (y/n) : ")
                if userinput.lower() == "y" or userinput.lower() == "n":
                    cond = False
                else:
                    raise ValueError
            except ValueError:
                print("Veuillez entrer une lettre (y ou n )")

        if userinput == "y":
            print("Veuillez patienter pendant la mise a jour de la base de données, ceci peut prendre plusieures minutes.")
            data = Dbmanager()
            data.contructdatabase()
            data.builddatabasetables()
            write = Writemanager()
            write.writecategories()
            write.writeproduct()
            write.writeshops()
            write.cleantables()
            write.writeproductinshop()
            write.writeproductcategory()

        else:
            self.menuprompt()


    def exitmenu(self):              #OK
        
        cond = True
        while cond:
            try:
                userinput = input("Voulez vous quitter le programme ? (Y/N) : ")
                if userinput.lower() == "y" or userinput.lower() == "n":
                   cond = False
                else:
                    raise TypeError    
            except TypeError:
                print("Veuillez entrer une lettre (y ou n)")

        if userinput.lower() == "y":
            exit
        else:
            self.menuprompt()
