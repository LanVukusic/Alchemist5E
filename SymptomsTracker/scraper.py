# scrapper for medical data - symptoms. that we are illegaly stealing from webMD
from bs4 import BeautifulSoup
import requests
import re
import json
from tqdm import tqdm
from time import time
import random

# number of asynchronous threads for downloading. It is 7 because it is a devider of 28
# - number of letters of alphabetical order, that we are parsing
WORKERS_NUM  = 1

jsonHolder = {}

r = requests.get('https://symptomchecker.webmd.com/symptoms-a-z#', verify = False)
soup = BeautifulSoup(r.text, 'html.parser')
regex = re.compile(r'list_.')
mydivs = soup.findAll("div", {"id": regex})


def getSubcategoryList(link, numOfCategories = 5):
  subsymptoms = []
  try:
    r = requests.get("https://symptomchecker.webmd.com/"+link, verify = False)
  except:
    return 
  soup2 = BeautifulSoup(r.text, 'html.parser')
  mydivs = soup2.findAll("td", {"class": "bg"})

  if (len(mydivs) > numOfCategories):
    for k in random.sample(range(1, len(mydivs)), numOfCategories):
      subsymptoms.append(mydivs[k].text)
  else:
    for i in mydivs:
      subsymptoms.append(i.text)

  return subsymptoms

def startProccess(indexMn, indexMx):
    # function that starts scrapping data from downloaded site. Index is the range tha it works on.
  for i in mydivs[indexMn:indexMx]:
    for j in i.findAll("li", {"class":"bg"}):
      jsonHolder[j.text] = getSubcategoryList(j.find("a")["href"])

  saveJSON()

def saveJSON(name="data"):
  jsn = json.dumps(jsonHolder)
  with open(name+".json", 'w') as outfile:
    outfile.write(jsn)


if __name__ == '__main__':
  # Setup a list of processes that we want to run
  """ lastInedx = 0
  workers = []
  for i in range(WORKERS_NUM):  # code breakes if division is not perfect. if WORKERS_NUM does not devide mydivs.len entries will get skipped.
    minInd = lastInedx
    maxInd = (len(mydivs) // WORKERS_NUM)+lastInedx
    workers.append(mp.Process(target=startProccess, args=(minInd, maxInd)))
    lastInedx = maxInd

    # Run processes
  for p in workers:
      print("worker started")
      p.start()

  # Exit the completed processes
  for p in workers:
      print("worker finished")
      p.join()
  
  print(jsonHolder) """

  startProccess(0,3)
  # saveJSON("data")
