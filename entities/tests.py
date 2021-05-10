import json

import mysql.connector

from databasecreator import Dbmanager
# from dbcreator import Dbmanager
from apimanager import Apimanager
from datacleaner import Datacleaner
from writemanager import Writemanager
import config


def execute():

    #TODO : test avec le db builder jusqu au niveau du write manager, voir la classe entre databasecreator et dbcreator qui marches et suppr l 'autre.
    Db = Dbmanager()
    Db.contructdatabase()
    Db.builddatabasetables()

    Data = Datacleaner()

    Data.createcategoryobject()   #TODO: a tester en connection. 
    Data.createproductobject()
    Data.createshopobjects()


    Write = Writemanager()
    Write.writecategories()
    Write.writeproduct()
    Write.writeshops()

execute()