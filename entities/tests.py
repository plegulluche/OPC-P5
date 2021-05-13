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

    Write = Writemanager()
    print("PIERR DEBUG: shoplist:",Write.data.shoplist)
    Write.writecategories()
    Write.writeshops()
    Write.writeproduct()

execute()