from service import *
from service import DataBase
import json

db = DataBase.Database()

db.writeHerbs(
    [
        "namee",
        1,
        3,
        1,
        "loree"
    ]
)

data = DataBase.ReadData()


data.read

test = data.readAllAny("Climate")
print(test)
