import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_race.settings')

import django
django.setup()

import re
import pandas 
from django.contrib.auth.models import User
from django.db import transaction
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from app_race.models import *  #Vishnupriya
from bs4 import BeautifulSoup
import pandas 


url = "https://www.indiarace.com/Home/horseStatistics/58328/ECO%20FRIENDLY"  #dynamic url of each player previous link
page = requests.get(url)
page_data = BeautifulSoup(page.content,"html.parser")

table = page_data.findAll('table',{"class":"sire table sire-table-new"})
th = table[0].findAll('th')
head = [i.text for i in th]

with transaction.atomic():
    datas = []
    tbody = table[0].findAll('tbody')
    tr = tbody[0].findAll('tr')
    for cell in tr:
        td = cell.find_all('td')
        row = [i.text.replace('\n','') for i in td]
        datas.append(row)

        for data in datas:
            slno = data[0]
            data = data[1]
            dist = data[2]
            rclass = data[3]
            raceno = data[4]                
            venue = data[5]
            jockey = data[6]
            wt = data[7]
            dist_wi = data[8]
            time = data[9]
            rtg = data[10]

            racecard_previous_details = RacecardPreviousDetails(
                slno = slno,
                data = data,
                dist = dist,
                rclass = rclass,
                raceno = raceno,
                venue = venue,
                jockey = jockey,
                wt = wt,
                dist_wi = dist_wi,
                time = time,
                rtg = rtg,
                # created_by = user,
                # modified_by = user,
                )
            racecard_previous_details.full_clean()
            racecard_previous_details.save()