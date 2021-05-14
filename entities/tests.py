import json

import mysql.connector

from databasecreator import Dbmanager
from apimanager import Apimanager
from datacleaner import Datacleaner
from writemanager import Writemanager
import config


def execute():

    
    Db = Dbmanager()
    Db.contructdatabase()
    Db.builddatabasetables()

    Write = Writemanager()
    Write.writecategories()
    Write.writeshops()
    Write.writeproduct()
    Write.writeproductcategory()
    Write.writeproductinshop()

execute()

