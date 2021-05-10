import json
# # from dbcreator import Dbmanager
from apimanager import Apimanager
from datacleaner import Datacleaner

# # from writemanager import Writemanager

# import mysql.connector
# import config


Data = Datacleaner()

Data.createcategoryobject()
Data.createproductobject()
Data.createshopobjects()