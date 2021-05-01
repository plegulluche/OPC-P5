import mysql.connector
from mysql.connector import errorcode
import config
import re

#user : "projet5" pwd : "OPC" this combinaison will be used as the user for the program to login into mysql.

class Dbmanager:
    """class that create the DB and tables inside it """

    def __init__(self):
        self.filetoconstructdb = config.filefordbcreator
        
    def contructdatabase(self,login=config.useridnodb):
        """Method of the dbmanager class to construct the database"""
        
        
        print("Connecting to MySQL database...")
        cnx = mysql.connector.Connect(**login)
        if cnx.is_connected():
            print("Connected to MySQL.")
        else:
            print("Connection failed.")          
        cnxcursor = cnx.cursor()
        cnxcursor.execute("DROP DATABASE IF EXISTS food")
        print("droping db.")
        cnxcursor.execute("CREATE DATABASE food")
        print("creating db")
        cnxcursor.execute("SHOW DATABASES")
        print("showing db")

        
           
        cnx.close()
        print("Connection closed.")

    def inserttables(self,login=config.userid):

        """method of the dbcreator class to connect to the database and contruct the tables from the file contained in the config file"""
        
        cnx = mysql.connector.connect(**login)
        cnxcursor = cnx.cursor()       

        with open("/home/ouranos/Documents/Projets python/OPC/Projet 5/entities/planbdd.sql", 'r') as sqlfile:
            query = sqlfile.read()
            result_iterator = cnxcursor.execute(query, multi=True)
        # for line in open(self.filetoconstructdb):
        #     cnxcursor.execute(line, multi = True)
            for res in result_iterator:
                print("Running query: ", res)
                if res.with_rows:
                        fetch_result = res.fetchall()
                        print(json.dumps(fetch_result, indent=4))
                elif res.rowcount > 0:
                        print(f"Affected {res.rowcount} rows" )
            cnx.commit()   
            cnx.close()