 - set up your data base with herbalism.sql
 - set your username and passwd in __init__.py in services package

 - to get a list of herbs from data base do:

#start

from service import DbConnection

data = DataBase.ReadData()
list_of_herbs = data.readAllHerbs()

#stop

 - see herb object structure at objects.Herb.Herb
