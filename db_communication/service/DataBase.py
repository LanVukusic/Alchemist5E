from service import DbConnection
from objects import Herb
from objects import Potion

class Data(object):
    con = None
    crs = None

    def __init__(self):
        self.con = DbConnection.DbConnection.getConnection()
        self.crs = self.con.cursor()

    def readAll(self):
        self.crs.execute("SELECT * FROM Herbs")
        return self.crs.fetchall()
        #returns a list of tuplets:
        #(it can be converted to json with (import..) json.dumps(<a list of tuplets>)

class WriteData:
    con = None
    crs = None

    def __init__(self):
        self.con = DbConnection.DbConnection.getConnection()
        self.crs = self.con.cursor()
        #print(self.con)

    def writeHerb(
            self,
            name: str,
            cost: int,
            climate = None,
            rarity = None,
            ingestion = None,
            effect = None,
            visual = None,
            lore = None,
            world = None,
            seasons = list(),
            potions = list()
    ): #JUST FOR TEST INSERTING
        pr = ReadData() # property reader

        if climate is not int:
            if climate is not None:
                climate = pr.readPropId("Climate", climate)
        if rarity is not int:
            if rarity is not None:
                rarity = pr.readPropId("Rarity", rarity)
        if ingestion is not int:
            if ingestion is not None:
                ingestion = pr.readPropId("Ingestion", ingestion)

        sql = "INSERT INTO Herbs (name, climateId, rarityId, ingestionId, cost, effect, visual, lore, world) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        print([name, climate, rarity, ingestion, cost, effect, visual, lore, world])
        val = (name, climate, rarity, ingestion, cost, effect, visual, lore, world)
        self.crs.execute(sql, val)
        self.con.commit()
        herbId = self.crs.lastrowid
            # these should always come in ids, if potion does not yet exists, user should (if he wants) create one and set it's herb properties
            # aka user should not even have an option to write a non existant potion name, thus should only be able to select potions
        self.writeConnection("HerbsSeasons", herbId, seasons)
        self.writeConnection("HerbsPotions", herbId, potions)

    def writeConnection(self, table, firstId, secId):
        sql = "INSERT INTO {table} VALUES (%s, %s, %s)".format(table = table, fId = firstId, sId = secId)
        val = [(None,firstId, x) for x in secId]
        self.crs.executemany(sql, val)
        self.con.commit();

    def writeProp(self, table: str, property: str):
        sql = "INSERT INTO {table} VALUES (default, %s)".format(table = table)
        val = [property]
        self.crs.execute(sql, val)
        self.con.commit()
        return self.crs.lastrowid

class ReadData:
    con = None;
    crs = None;
    write = WriteData()

    def __init__(self):
        self.con = DbConnection.DbConnection.getConnection()
        self.crs = self.con.cursor()
        #print(self.con)

    def readPropId(self, table, componentName):
        #comparison is case INSENSITIVE (so if a user writes an already existant season but different case it actually handles it as existant)
        querry = "SELECT id FROM {t} WHERE name = '{n}'".format(t = table, n = componentName)
        self.crs.execute(querry)
        fetch = [item[0] for item in self.crs.fetchall()]
        if len(fetch) is not 0: #this should always be either 1 or 0 (if it is higher there are duplicates in the database(this bad))
            return fetch[0]
        else:
            return self.write.writeProp(table, componentName)

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

    def readAllPotions(self):
        listP = self.readAllAny("Potions")
        potionList = list()

        for potion in listP:
            x = Potion.Potion()
            x.id = int(potion[0])
            x.name = potion[1]
            x.cost = potion[2]

            x.rarity = 0
            if(potion[3] is not None):
                x.rarity = int(potion[3])

            x.expDate = 0
            if(potion[4] is not None):
                x.expDate = int(potion[4])

            x.type = 0
            if(potion[5] is not None):
                x.type = int(potion[5])

            x.ingestion = 0
            if(potion[6] is not None):
                x.ingestion = int(potion[6])

            x.brewing = potion[7]
            x.storing = potion[8]
            x.effect = potion[9]
            x.visual = potion[10]
            x.lore = potion[11]
            x.world = potion[12]

            x.symptom = None
            if potion[13] is not None:
                x.symptom = potion[13]
            x.herbs = self.readConnection("HerbsPotions", "potionId", x.id, "herbId")
            potionList.append(x)
        return potionList

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
