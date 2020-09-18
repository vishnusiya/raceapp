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


def create_player_details(data):
    try:
        admin = User.objects.filter(is_active=True)[0]
        url = data.get('page_url')
        page = requests.get(url)
        page_data = BeautifulSoup(page.content,"html.parser")

        #Players Details
        items = page_data.find_all("div",class_ = "form-runner-details-main")
        player_name = [item.find(class_="horseName bold").get_text() for item in items]
        player_idex_num = [item.find(class_="number bold").get_text() for item in items]
        player_num = [item.find(class_="horseNumber").get_text() for item in items]  
        player_weight = [item.find(class_="horseWeight").get_text() for item in items]
        player_rating = [item.find(class_="RTG").get_text() for item in items]
        #previous Datas   
        #all form Rows HTML content


        table = page_data.find_all("table",class_ = "runsTable margin-top-10")
        table_len = len(table)
        table_type = type(table)
        table_index = type(table[1])
        table_num_tr = len(table[1].find_all('tr'))


        rng = len(player_name)
        with transaction.atomic():
            for i in range(0,rng):
                player = Player(
                    player_name = player_name[i],
                    player_idex_num = player_idex_num[i],
                    player_num = player_num[i],
                    player_weight = player_weight[i],
                    player_rating = player_rating[i],
                    created_by = admin,
                    modified_by = admin,
                    )
                player.full_clean()
                player.save()

            for j in range(0,table_len):
                results = table[j].find_all('tr', attrs={'class':'form-row'})

                for result in results: 
                    race_position = result.find('td', attrs={'class':'previousRunsLeftTableCell'}).text # result not results
                    description = result.find('td', attrs={'class':'align-top'}).text # result not results

                    ##race_date
                    match = re.search(r'\d{2}/\d{2}/\d{4}', description)
                    race_date = datetime.strptime(match.group(), '%d/%m/%Y').date()                 

                    ##race_rating
                    def getRatings(description): 
                        array1 = re.findall(r'Rtg:.\w+', description)
                        return array1
                    race_rating = getRatings(description) 

                    ##split race_rating
                    code_value1 = description.split('(L:')[0]


                    ###getDistance
                    def getDistance(code_value1): 
                        array = re.findall(r'[0-9]+m ', code_value1)
                        return array
                    array = getDistance(code_value1) 
                    race_distance = array[0]


                    def remove(string): 
                        pattern = re.compile(r'\s+') 
                        return re.sub(pattern, ' ', code_value1) 
                    code_value1 = remove(code_value1) 


                    def getClass(code_value1): 
                        array2 = re.findall(r'(?<=\dm)(.*)(?=\$)', code_value1)
                        return array2
                    race_class = getClass(code_value1) 


                    def getWeight(code_value1): 
                        array2 = re.findall(r'(?<=\))(.*)(?=\ )', code_value1)
                        return array2
                    race_weight = getWeight(code_value1) 



                    if len(race_position) > 1:
                        def remove(string): 
                            pattern = re.compile(r'\s+') 
                            return re.sub(pattern, ' ', race_position) 
                        race_position = remove(race_position)                           

                        race = Race(
                            player_name = player_name[j],
                            race_class = race_class,
                            race_position = race_position,
                            race_distance = race_distance,
                            race_rating = race_rating,
                            race_weight = race_weight,
                            race_date = race_date,
                            created_by = admin,
                            modified_by = admin,
                            )
                        race.full_clean()
                        race.save()

        print('Player Details Create Successfully')
    except Exception as e:
        print(e)
        print("Error in Player Details Create")


if __name__ == '__main__':
    data = {
        'page_url': "https://report.racenet.com.au/templates/HJHHcCdef?meeting=devonport-20200913&race=toorak-toff-at-kingsley-park-benchmark-6-race-1",
    }
    create_player_details(data)