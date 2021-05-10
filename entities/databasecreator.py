import mysql.connector
from mysql.connector import errorcode
import config
import re

#user : "projet5" pwd : "OPC" this combinaison will be used as the user for the program to login into mysql.

class Dbmanager:
    """class that create the DB and tables inside it """

    def __init__(self):
        self.logintomysqlnodb = config.useridnodb
        self.logintomysql = config.userid
        self.filetoconstructdb = config.filefordbcreator 

    def contructdatabase(self):

        try:
            cnx = mysql.connector.connect(**self.logintomysqlnodb)
            

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Something is wrong with your user name or password')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('Database does not exist')
            else:
                print(err)

        
        db_builder_cursor = cnx.cursor()

        db_builder_cursor.execute("DROP DATABASE IF EXISTS food;")
        db_builder_cursor.execute("CREATE DATABASE food;")
        db_builder_cursor.execute("SHOW DATABASES;")

              
        cnx.close()

 
    def builddatabasetables(self):
        
        try:
            cnx = mysql.connector.connect(**self.logintomysql)
            

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Something is wrong with your user name or password')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('Database does not exist')
            else:
                print(err)

        
        db_builder_cursor = cnx.cursor()

        

        def exec_sql_file(cursor=db_builder_cursor, file=self.filetoconstructdb):
            
            statement = ""

            for line in open(file):
                
                if not re.search(r';$', line):
                    statement = statement + line
                else: # when you get a line ending in ';' then exec statement and reset for next statement 
                    statement = statement + line
                    try:
                        db_builder_cursor.execute(statement)
                    except (OperationalError, ProgrammingError) as e:
                        print("[WARN] MySQLError during execute statement \n\tArgs: (%)".format(e))
                    
                    statement = ""
                
        exec_sql_file()

        cnx.close()
