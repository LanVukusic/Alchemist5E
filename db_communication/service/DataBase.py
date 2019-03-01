from service import DbConnection
from objects import Herb


class HerbData(object):
    con = None
    crs = None

    def __init__(self):
        self.con = DbConnection.DbConnection.getConnection()
        crs = self.con.cursor()

    def readAll(self):
        self.crs.execute("SELECT * FROM Herbs")
        return self.crs.fetchall()
        #returns a list of tuplets:
        #(it can be converted to json with (import..) json.dumps(<a list of tuplets>)

class Database:
    con = None;
    crs = None;

    def __init__(self):
        self.con = DbConnection.DbConnection.getConnection()
        self.crs = self.con.cursor()
        #print(self.con)

    def writeToOneLine(self, table, data):
        '''
        This can only be used for tables with only (id, name) thus the property tables:
            Climate, ExpDate, Ingestion, PotionType, Rarity, Season, Symptom
        :param table: to be inserted into
        :param list: a list of names to be inserted
        :return:
        '''

        list = SqlList.getList(SqlList, data)

        sql = "INSERT INTO {s} (name) VALUES (%s)".format(s = table)
        val = [data]
        self.crs.execute(sql, val)
        self.con.commit()
        print(self.crs.rowcount)

    def writeHerbs(self, data): #JUST FOR TEST INSERTING
        sql = "INSERT INTO Herbs (name, climateId, cost, ingestionId, lore) VALUES (%s, %s, %s, %s, %s)"
        val = data
        self.crs.execute(sql, val)
        self.con.commit()
        print(self.crs.rowcount)

class ReadData:
    con = None;
    crs = None;

    def __init__(self):
        self.con = DbConnection.DbConnection.getConnection()
        self.crs = self.con.cursor()
        #print(self.con)

    def readAllHerbs(self):
        listH = self.readAllAny("Herbs")
        herbList = list()
        for herb in listH:
            x = Herb.Herb()
            x.id = int(herb[0])
            x.name = herb[1]

            x.climate = 0
            if(herb[2] is not None):
                x.climate = int(herb[2])

            x.rarity = 0
            if(herb[3] is not None):
                x.rarity = int(herb[3])

            x.ingestion = 0
            if(herb[4] is not None):
                x.ingestion = int(herb[4])

            x.cost = int(herb[5])
            x.effect = herb[6]
            x.visual = herb[7]
            x.lore = herb[8]
            x.world = herb[9]
            x.seasons = self.readConnection("HerbsSeasons", "herbId", x.id, "seasonId")
            x.potions = self.readConnection("HerbsPotions", "herbId", x.id, "potionId")
            herbList.append(x)
        return herbList

    def readConnection(self, connection, purpose, purposeId, property):
        '''
            Used for multipleToMulitple pattern search
        :param connection: table holding the connection
        :param purpose: the filter (for instance herbId)
        :param property: what we need (for instance seasonId)
        :return: a list of poperty id's matched with the purpose id
        '''
        properties = list()
        querry = "SELECT {prop} FROM {conn} WHERE {purp} = {pId}"
        querry = querry.format(prop = property, conn = connection, purp = purpose, pId = purposeId)

        self.crs.execute(querry)

        fetch = [item[0] for item in self.crs.fetchall()]

        return fetch

    def readAllAny(self, table):
        '''
        It reads all rows as whole. (The result can be converted to json with (import..) json.dumps(<a list of tuplets>)
        Care as all table names start with a caps letter, such as: Climate, Herbs, ...
        :param table: from which to read
        :return: a list of tuplets
        '''
        self.crs.execute("SELECT * FROM {s}".format(s = table))
        return self.crs.fetchall()

class SqlList:
    def getList(self, data):
        i = iter(data)
        n = [None for one in data]
        return zip(iter(n), i)
