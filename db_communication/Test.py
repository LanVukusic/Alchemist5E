from service import *
from service import DataBase
import json

x = DbConnection.DbConnection.getConnection()

print(x)

y = DbConnection.DbConnection.getConnection()

print(y)

z = DataBase.HerbData()

for i in z.readAll():
    print(i)

print(json.dumps(z.readAll()))
