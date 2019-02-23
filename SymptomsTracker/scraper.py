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

numOfCategories = 5  # the maximal ammount of symptom subtypes that can be gathered 

jsonHolder = {}  #temp storage for the data export

r = requests.get('https://symptomchecker.webmd.com/symptoms-a-z#', verify = False)  #requests the base website. verify = false to prevent ssl errors
soup = BeautifulSoup(r.text, 'html.parser')
regex = re.compile(r'list_.')  # searching with regex. list_A list_B list_C ...so on
mydivs = soup.findAll("div", {"id": regex})  #filtering all tables


def getSubcategoryList(link, numOfCategories = 5):  # procces the subsymptoms
  subsymptoms = []
  try:
    r = requests.get("https://symptomchecker.webmd.com/"+link, verify = False)  
  except:
    return 
  soup2 = BeautifulSoup(r.text, 'html.parser')
  mydivs = soup2.findAll("td", {"class": "bg"})

  if (len(mydivs) > numOfCategories):
    for k in random.sample(range(1, len(mydivs)), numOfCategories):  # selects numOfCategories rangom samples from the given page
      subsymptoms.append(mydivs[k].text)
  else:
    for i in mydivs:  # if there is not enough samples, just pick all of them
      subsymptoms.append(i.text)

  return subsymptoms

def startProccess():
    # function that starts scrapping data from downloaded site. Index is the range tha it works on.
  
  for i in mydivs:
    for j in i.findAll("li", {"class":"bg"}):
      jsonHolder[j.text] = getSubcategoryList(j.find("a")["href"])  # append the main symptom and querry for it's subsymptoms

  saveJSON()  # saves the file when done

def saveJSON(name="data"):
  jsn = json.dumps(jsonHolder)  # dumps dict to json 
  with open(name+".json", 'w') as outfile:
    outfile.write(jsn)  # saves json


if __name__ == '__main__':
  startProccess()
 
