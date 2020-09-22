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

# url = "https://www.indiarace.com/Home/racingCenterEvent?venueId=3&event_date=2020-03-06&race_type=RACECARD" --> issue
url = "https://www.indiarace.com/Home/racingCenterEvent?venueId=10&event_date=2019-10-26&race_type=RACECARD" 
# url = "https://www.indiarace.com/Home/racingCenterEvent?venueId=8&event_date=2020-03-01&race_type=RACECARD" 
page = requests.get(url)
page_data = BeautifulSoup(page.content,"html.parser")
#print(page_data)

#Race 1 Full Data RACE
items = page_data.find_all("div",id = 'race-1')
from django.db import transaction


######################################################################
total = page_data.find_all("div",class_ = "row winner_row")
total_race = len(total)

with transaction.atomic():
    for i in range(1,total_race+1):
        race_id = 'race-'+str((i))
        datas = []
        items = page_data.find_all("div",id = race_id)
        table = items[0].find('table',class_ ='table table-striped statistics_table race_card_tab')
        table_len = len(table)
        for i in range(0,1):    
            race_card_td = table.find_all('td', class_="race_card_td")
            race_url = race_card_td[0].find('a')
            thead = table.find_all('thead', class_="statistics_table_head")
            tbody = table.find_all('tbody', class_="table_body_static race-card-new table-hover")
            rows2 = tbody[0].find_all('tr', class_="dividend_tr")

            for row in rows2:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                datas.append(cols) # Get rid of empty values


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

            race_url = str(race_url)
            race_url = race_url.split('"')
            race_url = race_url[1]


            horse_pedigree = race_url.split('/')[6]

            racecardss = RaceCard.objects.filter(is_active=True,raceno=raceno)
            if not racecardss.exists():
                racecard = RaceCard(
                    raceno = raceno,
                    race_primarykey = race_primarykey,
                    main_head = main_head,
                    main_subhead = main_subhead,
                    race_distance = race_distance,
                    race_url = race_url,
                    horse_pedigree = horse_pedigree,
                    # created_by = user,
                    # modified_by = user,
                    )
                racecard.full_clean()
                racecard.save()


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

            #table Data
            no = data[0]
            silk = data[1]
            horse_pedigree = data[2]
            desc = data[3]
            owner = data[4]                
            trainer = data[5]
            jockey = data[6]
            wt = data[7]
            al = data[8]
            sh = data[9]
            eq = data[10]
            rtg = data[11]

            racecard_detailsss = RaceCardDetails.objects.filter(is_active=True,raceno=raceno)
            if not racecard_detailsss.exists():
                racecard_details = RaceCardDetails(
                    no = no,
                    silk = silk,
                    horse_pedigree = horse_pedigree,
                    desc = desc,
                    owner = owner,
                    trainer = trainer,
                    jockey = jockey,
                    wt = wt,
                    al = al,
                    sh = sh,
                    eq = eq,
                    rtg = rtg,
                    raceno = raceno,
                    race_primarykey = race_primarykey,
                    main_head = main_head,
                    main_subhead = main_subhead,
                    race_distance = race_distance,
                    # created_by = user,
                    # modified_by = user,
                    )
                racecard_details.full_clean()
                racecard_details.save()


    racecards = RaceCard.objects.filter(is_active=True)
    for racecard in racecards:
        
        url = racecard.race_url
        page = requests.get(url)
        page_data = BeautifulSoup(page.content,"html.parser")

        table = page_data.findAll('table',{"class":"sire table sire-table-new"})
        th = table[0].findAll('th')
        head = [i.text for i in th]

        datas = []
        tbody = table[0].findAll('tbody')
        tr = tbody[0].findAll('tr')
        horse_pedigree = url.split('/')[6]
        for cell in tr:
            td = cell.find_all('td')
            row = [i.text.replace('\n','') for i in td]
            datas.append(row)




            for data in datas:
                slno = data[0]
                data1 = data[1]
                dist = data[2]
                rclass = data[3]
                raceno = data[4]                
                venue = data[5]
                jockey = data[6]
                wt = data[7]
                dist_wi = data[8]
                time = data[9]
                rtg = data[10]

                previous = RacecardPreviousDetails.objects.filter(is_active=True,horse_pedigree=horse_pedigree).count()
                if previous < 6:
                    racecard_previous_details = RacecardPreviousDetails(
                        slno = slno,
                        data = data1,
                        dist = dist,
                        rclass = rclass,
                        raceno = raceno,
                        venue = venue,
                        jockey = jockey,
                        wt = wt,
                        dist_wi = dist_wi,
                        time = time,
                        rtg = rtg,
                        horse_pedigree=horse_pedigree,
                        # created_by = user,
                        # modified_by = user,
                        )
                    racecard_previous_details.full_clean()
                    racecard_previous_details.save()
      
    print("sucess")







   