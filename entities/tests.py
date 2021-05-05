import json
# from dbcreator import Dbmanager
from apimanager import Apimanager
from datacleaner import Datacleaner

# from writemanager import Writemanager

import mysql.connector
import config

api = Apimanager()
print(api.geteightcategories())
# data = Datacleaner()

# print(data.createcategoryobject())