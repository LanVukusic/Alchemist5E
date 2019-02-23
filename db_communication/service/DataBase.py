from service import DbConnection

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
    def read(self, seasonId, climateId, rarityId, minCost, maxCost):
        self.crs.execute("")
