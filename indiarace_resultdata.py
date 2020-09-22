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
from app_race.models import *  #Vishnupriya

url = "https://www.indiarace.com/Home/racingCenterEvent?venueId=3&event_date=2020-03-06&race_type=RESULTS"
page = requests.get(url)
page_data = BeautifulSoup(page.content,"html.parser")


total = page_data.find_all("div",class_ = "row winner_row")
total_race = len(total)


with transaction.atomic():
    for i in range(1,total_race+1):
        race_id = 'race-'+str((i))
        datas = []

        items = page_data.find_all("div",id = race_id)

        table = items[0].find_all('table', attrs={'class':'result-table-new1'})
        table_len = len(table)
        for i in range(0,table_len):    
            thead = table[0].find_all('thead')
            tbody = table[0].find_all('tbody')
            rows1 = thead[0].find_all('tr')
            rows2 = tbody[0].find_all('tr')



            for row in rows2:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                datas.append(cols) # Get rid of empty values
                data_len = len(datas)


            for data in datas:
                #race number
                raceno_data = items[0].find('div',class_ ='side_num')
                raceno = raceno_data.find('h1').text
                race_primarykey = raceno_data.find('h5').text

                #race heading datas
                racehead_data = items[0].find('div',class_ ='center_heading')
                main_head = racehead_data.find('h2').text
                main_subhead = racehead_data.find('h3').text

                #race  distance
                racetime_data = items[0].find('div',class_ ='archive_time')  
                race_distance = racetime_data.find('h4').text


                # main_head = main_head.strip()
                # main_head = main_head.replace(" ", "")
                # main_head = " ".join(main_head.split())


                #table Data
                Pl = data[0]
                h_no = data[1]
                horse_pedigree = data[2]
                desc = data[3]
                trainer = data[4]
                jockey = data[5]
                wt = data[6]
                al = data[7]
                dr = data[8]
                sh = data[9]
                won_by = data[10]
                dist_win = data[11]
                rtg = data[12]
                odds = data[13]
                time = data[14]

                result = Result(
                    Pl = Pl,
                    h_no = h_no,
                    horse_pedigree = horse_pedigree,
                    desc = desc,
                    trainer = trainer,
                    jockey = jockey,
                    wt = wt,
                    al = al,
                    dr = dr,
                    sh = sh,
                    won_by = won_by,
                    dist_win = dist_win,
                    rtg = rtg,
                    odds = odds,
                    time = time,
                    raceno = raceno,
                    race_primarykey = race_primarykey,
                    main_head = main_head,
                    main_subhead = main_subhead,
                    race_distance = race_distance,
                    )
                result.full_clean()
                result.save()

    print("sucess")

