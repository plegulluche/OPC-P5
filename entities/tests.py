from dbcreator import Dbmanager
from apimanager import Apimanager
from writemanager import Writemanager


import mysql.connector
import config

# data = { "count" : 12354, "tags" : [
#             {"products" : 18522,
#             "name" : "viandes",
#             "id" : "xxx",
#             "url" : "XXX.com",
#             "known" : 1},
#             {"products" : 7852,
#             "name" : "poissons",
#             "id" : "xxx",
#             "url" : "XXX.com",
#             "known" : 1}
# ]}
# def getvalue(dico):
#     value = dico["products"]
#     print(value)
    

# getvalue(data["tags"])

# for allcategories in data["tags"]:
#     category = allcategories["name"]
#     category_names.append(category)

# print(category_names)
# dbconstruct = Dbmanager()
# dbconstruct.contructdatabase()
# dbconstruct.inserttables
db = Dbmanager()
db.contructdatabase()
db.inserttables()

# testwrite = Writemanager()
# testwrite.writecategories()

# listcate = test.createcategoryobject(test.getsixcategories())
# listobjets = test.createproductobject()

# print(listcate)
# print(listobjets)





#list_test = ['viandes', 'poisson', 'legumes', 'fruits']
# dicotest = {"viandes" : [{
#                           "name" : "steack Hé",
#                           "url"  : "url1",
#                           "nutri" : "c"      
#                         },
#                         {
#                           "name" : "test",
#                           "url"  : "none",
#                           "nutri" : "no data"  

#                         }],
#             "poisson" : [{
#                           "name" : "bar",
#                           "url"  : "url1",
#                           "nutri" : "a"      
#                         },
#                         {
#                           "name" : "poisson pané",
#                           "url"  : "none",
#                           "nutri" : "e"  

#                         }],
#             "legumes" : [{
#                           "name" : "carottes",
#                           "url"  : "urlc",
#                           "nutri" : "a"      
#                         },
#                         {
#                           "name" : "tomates",
#                           "url"  : "urlt",
#                           "nutri" : "no data"  
#                           "interm" : { "categories" : ["xxx","www"]}
                         
#                         }],
#             "fruits" : [{
#                           "name" : "banane",
#                           "url"  : "urlb",
#                           "nutri" : "b"      
#                         },
#                         {
#                           "name" : "kiwi",
#                           "url"  : "none",
#                           "nutri" : "no data" 
#                           "interm" : { "categories" : ["xxx","www"]}
#                         } 

#                         }],
#             }

            
# for index in range(len(list_test)):
#     categories = list_test[index]
#     for products in dicotest["{}".format(categories)]:
#         keys = ["name", "url", "nutri"]
#         listvalues = dict(name = products.get("name"), url = products.get("url"), nutri = products.get("nutri"))
#         print(listvalues)


# write = Writemanager()
# write.connecttodb()




