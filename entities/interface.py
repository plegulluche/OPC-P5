from tqdm import tqdm

from entities.readmanager import Readmanager as Readmanager
from entities.databasecreator import Dbmanager as Dbmanager
from entities.writemanager import Writemanager as Writemanager


class Interface:
    """
    Class managing data output in the console,
    organising them in a form of a menu managing inputs.

    Each method correspond to a menu, when the use enter the
    corresponding input a method is called to open the
    menu wich match the input.
    """

    def __init__(self):
        """
        interface class constructor.
        """
        pass

    def welcome(self):
        """
        Display the welcome menu.

        catch any input error.
        """

        welcome = "# Bienvenue dans OpenFoodFact Comparateur. #"
        nextmenu = "#    Appuyez sur Entrée pour continuer.    #"
        print()
        print()
        for characters in welcome:
            print("#", end="")
        print()
        print(welcome)
        print(nextmenu)
        for characters in welcome:
            print("#", end="")
        print()
        print()

        cond = True
        while cond:
            try:
                userinput = input("")
                if userinput == "":
                    cond = False
                    self.menuprompt()
                else:
                    raise ValueError
            except ValueError:
                print("Appuyez sur la touche entrée de votre clavier svp")

    def menuprompt(self):
        """
        Display the main menu.

        catch any input errors.
        """

        menu = {
            1: "Chercher un nouveau produit.",
            2: "Afficher les favoris.",
            3: "Mettre a jour la base de données.",
            4: "Quitter le programme.",
        }
        for key, values in menu.items():
            print(key, ":", values)

        cond = True
        while cond:
            try:
                userinput = int(input("Entrez votre choix (1-4): "))
                if userinput in range(1, 5):
                    cond = False
                else:
                    raise ValueError
            except ValueError:
                print("Veuillez entrer un nombre valide. (1-4)")

        if userinput == 1:
            self.newproduct()
        elif userinput == 2:
            self.favorites()
        elif userinput == 3:
            self.updatedb()
        else:
            self.exitmenu()

    def newproduct(self):
        """
        This method is called when the option #1 is selected
        by the user in the menuprompt method.

        Displays a menu from which the user must select a category
        from 5 random categories fetched in the database.

        Call the chooseproduct method passing it the id from the choosen category
        as int.

        catch any input errors.
        """

        read = Readmanager()
        fivecateids = read.read5randomcate()
        fivecatename = []
        for ids in fivecateids:
            fivecatename.append(read.readcategory(ids))
        menu = {
            1: fivecatename[0],
            2: fivecatename[1],
            3: fivecatename[2],
            4: fivecatename[3],
            5: fivecatename[4],
        }
        for key, values in menu.items():
            print(key, ":", values)
        cond = True
        while cond:
            try:
                userinput = int(input("entrez votre choix (1-5) : "))
                if userinput in range(1, 6):
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

    def chooseproduct(self, idcate):
        """
        This method is called when the user enter the correct input
        in the newproduct method.
        Display a menu with 5 random products choosen from the database
        corresponding to the category the user selected.

        :param : The category id
        :type : int

        Call the algosubstitu method passing it the productid
        as int when the user select a product.
        """

        read = Readmanager()
        checkmorethanfive = read.readproductcatecate(idcate)
        fiveproducts = None
        if len(checkmorethanfive) <= 5:
            fiveproductsdisplay = read.readproductcatecate(idcate)
            idlist = []
            for product in fiveproductsdisplay:
                idlist.append(read.readproductnameorid(product))
            fiveproducts = idlist
            x = 1
            for product in fiveproductsdisplay:
                print(x, ":", product)
                x += 1
        else:
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
                if userinput in range(1, 6):
                    cond = False
                else:
                    raise ValueError
            except ValueError:
                print("Veuillez entrer un choix valide (1-5)")

        if userinput == 1:
            self.algosubstitu(fiveproducts[0])
        elif userinput == 2:
            self.algosubstitu(fiveproducts[1])
        elif userinput == 3:
            self.algosubstitu(fiveproducts[2])
        elif userinput == 4:
            self.algosubstitu(fiveproducts[3])
        else:
            self.algosubstitu(fiveproducts[4])

    def algosubstitu(self, productid):
        """
        Search in the database a product, corresponding
        to the one selected by the use in the chooseproduct
        method, and with a better nutriscore value.
        Display an array of all its datas.
        Also allow the user to register the result in the database.

        :param : id of the selected product
        :type : int

        call the newproduct method or the menuprompt method
        depending of the userinput.
        """

        print("RECHERCHE DE VOTRE SUBSTITUT VEUILLEZ PATIENTER.")
        print(productid)
        read = Readmanager()

        listcateids = read.readproductcatecateid(productid)
        prospectprodid = read.readsamecate(listcateids)

        while productid in prospectprodid:
            del prospectprodid[prospectprodid.index(productid)]

        listofproductwithcategories = []
        for product in tqdm(prospectprodid):
            catesprodname = read.readproductcatecateid(product)
            datas = (product, catesprodname)
            listofproductwithcategories.append(datas)

        finalprospects = []

        for productandcates in tqdm(listofproductwithcategories):
            commons = list(set(productandcates[1]).intersection(listcateids))
            score = len(commons)
            if score == len(listcateids):
                finalprospects.append(productandcates[0])
            elif score == len(listcateids) - 1:
                finalprospects.append(productandcates[0])
            elif score == len(listcateids) - 2:
                finalprospects.append(productandcates[0])

        if finalprospects == []:
            cond = True
            while cond:
                print("Pas de substitut pour ce produit dans la base de donnée")
                try:
                    userinput = input(
                        "Voulez vous chercher un autre produit (P) ou retourner au menu principal (M) ? : "
                    )
                    if userinput.lower() == "p":
                        self.newproduct()
                        cond = False
                    elif userinput.lower() == "m":
                        self.menuprompt()
                        cond = False
                    else:
                        raise TypeError
                except TypeError:
                    print("Veuillez entrer un choix valide svp")

        else:
            scoreref = 0
            scoresubstitute = 0
            substituteid = 0
            nutriscoreref = read.readnutriscore(productid)
            if nutriscoreref == "a":
                scoreref = 1
            elif nutriscoreref == "b":
                scoreref = 2
            elif nutriscoreref == "c":
                scoreref = 3
            elif nutriscoreref == "d":
                scoreref = 4
            else:
                scoreref = 5

            for prodid in finalprospects:
                if read.readnutriscore(prodid) == "a":
                    scoresubstitute = 1
                elif read.readnutriscore(prodid) == "b":
                    scoresubstitute = 2
                elif read.readnutriscore(prodid) == "c":
                    scoresubstitute = 3
                elif read.readnutriscore(prodid) == "d":
                    scoresubstitute = 4
                elif read.readnutriscore(prodid) == "e":
                    scoresubstitute = 5
                else:
                    scoresubstitute = 6

                if scoreref == 1 and scoresubstitute == scoreref:
                    substituteid = prodid
                elif scoresubstitute < scoreref:
                    substituteid = prodid
                    break
                elif scoresubstitute <= scoreref:
                    substituteid = prodid
                    break

            write = Writemanager()
            print(substituteid)
            baseproductinfos = read.selectproductdata(productid)
            surrogateinfos = read.selectproductdata(substituteid)
            surrogateshops = read.readproductshopshop(substituteid)
            if substituteid is None:
                print("Pas de substituts valables trouvés")
            for items in surrogateinfos:
                if items is None:
                    items = "Pas d'infos"
            for items in surrogateshops:
                if items is None:
                    items = "Pas d'infos"

            print(
                "                                                          \n"
                "__________________________________________________________\n"
                f"Produit de base :        | {baseproductinfos[0]}         \n"
                f"Nutriscore :             | {baseproductinfos[1]}         \n"
                f"Substitut :              | {surrogateinfos[0]}           \n"
                f"Nutriscore :             | {surrogateinfos[1]}           \n"
                f"Magasins :               | {surrogateshops}              \n"
                f"URL :                    | {surrogateinfos[2]}           \n"
                "__________________________________________________________\n"
            )

            cond = True
            while cond:
                try:
                    userinput = input("Voulez-vous sauvegarder ce substitut ? (o/n) : ")
                    if userinput.lower() == "o":
                        write.writesurrogate(productid, substituteid)
                        cond = False
                        print("Produit enregistré.")

                    elif userinput.lower() == "n":
                        cond = False
                    else:
                        raise TypeError
                except TypeError:
                    print("Veuillez entrer une réponse valide svp (o/n) ")

            cond = True
            while cond:
                try:
                    userinput = input(
                        "Voulez vous chercher un autre produit (P) ou retourner au menu principal (M) ? : "
                    )
                    if userinput.lower() == "p":
                        self.newproduct()
                        cond = False
                    elif userinput.lower() == "m":
                        self.menuprompt()
                        cond = False
                    else:
                        raise TypeError
                except TypeError:
                    print("Veuillez entrer un choix valide svp")

    def favorites(self):
        """
        Display an array with all the datas of the favorites
        registered in the Surrogate table in the database.
        """

        read = Readmanager()
        surrogates = read.readsurrogate()
        allproduct = []
        allsurrogates = []
        allprodshops = []
        allsurrshops = []
        for couples in surrogates:
            dataproduct = read.selectproductdata(couples[0])
            datasurrogate = read.selectproductdata(couples[1])
            allproduct.append(dataproduct)
            allsurrogates.append(datasurrogate)
        for couples in surrogates:
            shopsproducts = read.readproductshopshop(couples[0])
            shopssurro = read.readproductshopshop(couples[1])
            allprodshops.append(shopsproducts)
            allsurrshops.append(shopssurro)

        def top():
            print(
                "|",
                "_" * 25,
                "Produit de Base",
                "_" * 25,
                "|",
                "_" * 25,
                "Substitut",
                "_" * 25,
                "|",
            )

        def sep():
            print("*" * 135)

        def name(productname, surrname):
            lenght = 66
            if len(productname) > lenght:
                begining = productname[:55]
                ending = productname[55:]
                print(
                    f"Nom: {begining}", " " * (63 - len(begining)), f"|Nom: {surrname}"
                )
                print(" " * 5, f"{ending}")
            else:
                print(
                    f"Nom: {productname}",
                    " " * (63 - len(productname)),
                    f"|Nom: {surrname}",
                )

        def nutri(nutriprod, nutrisurr):
            print(f"Nutriscore: {nutriprod}", " " * 55, f"|Nutriscore: {nutrisurr}")

        def shops(prodshops, surrshops):
            lenght = 60
            lenghtproshop = 0
            prodshopbegining = []
            prodshopend = []
            totallenbeginig = 0
            for shops in prodshops:
                lenghtproshop += len(shops) + 4
            lenghtproshop += 2
            if prodshops == []:
                print(f"Magasins: {prodshops}", " " * 56, f"|Magasins: {surrshops}")
            elif lenghtproshop > lenght:
                prodshopbegining.append(prodshops[:2])
                prodshopend.append(prodshops[2:])
                for shops in prodshopbegining:
                    totallenbeginig += len(shops)
                print(
                    f"Magasins: {prodshopbegining}",
                    " " * (60 - totallenbeginig),
                    f"|Magasins: {surrshops}",
                )
                print(" " * 5, f"{prodshopend}")

            else:
                print(
                    f"Magasins: {prodshops}",
                    " " * (60 - lenghtproshop),
                    f"|Magasins: {surrshops}",
                )

        def link(prodlink, surrlink):
            lenghtprodlink = len(prodlink[:55])
            begining = prodlink[:55]
            ending = prodlink[55:]
            print(f"URL: {begining}", " " * (63 - lenghtprodlink), f"|URL: {surrlink}")
            print(f"{ending}")

        top(), sep(), sep()

        for product, surrogate, shopprod, shopsurr in zip(
            allproduct, allsurrogates, allprodshops, allsurrshops
        ):
            name(product[0], surrogate[0])
            nutri(product[1], surrogate[1])
            shops(shopprod, shopsurr)
            link(product[2], surrogate[2])
            sep()
            sep()
        cond = True
        while cond:
            try:
                userinput = input("Voulez vous  retourner au menu principal (o/n) ? : ")
                if userinput.lower() == "o":
                    self.menuprompt()
                    cond = False
                elif userinput.lower() == "n":
                    self.exitmenu()
                    cond = False
                else:
                    raise TypeError
            except TypeError:
                print("Veuillez entrer un choix valide svp")

    def updatedb(self):
        """
        Call all the methods to recreate the database, call the API
        to fetch new datas and fill the database with those new datas.
        """

        cond = True
        while cond:
            try:
                userinput = input(
                    "Voulez vous mettre a jour la base de données? (y/n) : "
                )
                if userinput.lower() == "y" or userinput.lower() == "n":
                    cond = False
                else:
                    raise ValueError
            except ValueError:
                print("Veuillez entrer une lettre (y ou n )")

        if userinput == "y":
            print(
                "Veuillez patienter pendant la mise a jour de la base de données,"
                + "ceci peut prendre plusieures minutes."
            )
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

        cond = True
        while cond:
            try:
                userinput = input("Voulez vous  retourner au menu principal (o/n) ? : ")
                if userinput.lower() == "o":
                    self.menuprompt()
                    cond = False
                elif userinput.lower() == "n":
                    self.exitmenu()
                    cond = False
                else:
                    raise TypeError
            except TypeError:
                print("Veuillez entrer un choix valide svp")

    def exitmenu(self):
        """
        Display the exit menu.
        """

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
