
import mysql.connector

class DbConnection(object):
    mydb = None

    host= None
    user = None
    passwd = None
    database = None

    @staticmethod
    def getConnection():
        # makes sure the connection doesn't create multiple connections,
        # but instead it feeds the same one to everyone.
        if(DbConnection.mydb is None):
            DbConnection.mydb = mysql.connector.connect(
                host = DbConnection.host,
                user = DbConnection.user,
                passwd = DbConnection.passwd,
                database = DbConnection.database
            )
        #print(DbConnection.mydb)

        return DbConnection.mydb
