# scrapper for medical data - symptoms. that we are illegaly stealing from webMD
from bs4 import BeautifulSoup
import requests
import re
import json
from tqdm import tqdm
from time import time
import random


jsonHolder = {}

r = requests.get('https://symptomchecker.webmd.com/symptoms-a-z#')
soup = BeautifulSoup(r.text, 'html.parser')
regex = re.compile(r'list_.')
mydivs = soup.findAll("div", {"id": regex})


def getSubcategoryList(link, numOfCategories = 5):
  subsymptoms = []

  r = requests.get("https://symptomchecker.webmd.com/"+link)
  soup2 = BeautifulSoup(r.text, 'html.parser')
  mydivs = soup2.findAll("td", {"class": "bg"})

  if (len(mydivs) > numOfCategories):
    for k in random.sample(range(1, len(mydivs)), numOfCategories):
      subsymptoms.append(mydivs[k].text)
  else:
    for i in mydivs:
      subsymptoms.append(i.text)

  return subsymptoms


for i in tqdm(mydivs):
  for j in i.findAll("li", {"class":"bg"}):
    jsonHolder[j.text] = getSubcategoryList(j.find("a")["href"])
    

jsn = json.dumps(jsonHolder)
with open('data.json', 'w') as outfile:
    json.dump(jsn, outfile)