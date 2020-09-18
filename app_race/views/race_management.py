import string
import random
import os
import string 
import requests
import json, base64, traceback, sys
from django.core.files import File

from decimal import Decimal
from datetime import datetime

from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound

from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_GET
from django.db import transaction
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone

from django.contrib.auth.models import User
from django.db.models import Q
import re
import pandas 
from django.contrib.auth.models import User
from django.db import transaction
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from app_race.models import *

@require_POST
def user_login(request):
    try:
        username = request.POST.get('username')
        if username in [None,'']:
            return HttpResponse(content=json.dumps("username not available"), content_type="application/json", status=406)
        
        password = request.POST.get('password')
        if password in [None,'']:
            return HttpResponse(content=json.dumps("password not available"), content_type="application/json", status=406)

        user = User.objects.filter(is_active=True,username=username)
        if not user.exists():
            return HttpResponse(content=json.dumps("Invalid username or password"), content_type="application/json", status=406)
        user = user[0]

        login(request, user)
        return HttpResponse(content=json.dumps("Successfully"), status=200, content_type="application/json")
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err = "\n".join(traceback.format_exception(*sys.exc_info()))
        print(err)
        return HttpResponse(content=json.dumps("Invalid username or password"), content_type="application/json", status=406)



@require_GET
@login_required
def api_player_list_get(request):
    try:
        user = request.user
        headings = list(Heading.objects.filter(is_active=True).values_list('heading',flat=True))
        players = Player.objects.filter(is_active=True).order_by('id')
        player_lst = []
        for player in players:
            player_weight = ''
            if player.player_weight not in [None,'']:                
                player_weight =player.player_weight.replace('kg', '')
            player_dict = {}
            player_dict['player_id'] = player.id
            player_dict['player_name'] = player.player_name
            player_dict['player_idex_num'] = player.player_idex_num
            player_dict['player_num'] = player.player_num
            player_dict['player_weight'] = player_weight
            player_dict['player_rating'] = player.player_rating

            race_lst = []
            races = Race.objects.filter(is_active=True,player_name=player.player_name).order_by('id')
            for race in races:
                bad_chars = ['[', ']', "'", "*"]   
                race_class = race.race_class                  
                race_class = ''.join(i for i in race_class if not i in bad_chars)
                race_class = race_class.replace('Synthetic', '')
                race_class = race_class.replace('True', '')
                race_class = race_class.replace('Entire', '')
                race_class = race_class.replace('Circuit', '')
                race_class = race_class.replace('Course', '')

                test_string = "Hcp"  
                # print("The original string : " + str(test_string))                   
                res = isinstance(test_string, str)                   
                # print("Is variable a string ? : " + str(res)) 
                if res == True:
                    race_class = race_class
                else:
                    race_class = 'N/A'


                bad_chars = ['[', ']', "'", '"']   
                race_rating = race.race_rating                  
                race_rating = ''.join(i for i in race_rating if not i in bad_chars) 


                bad_chars = ['[', ']', "'", '"',","]   
                race_weight = race.race_weight                
                race_weight = ''.join(i for i in race_weight if not i in bad_chars) 




                

                race_dict = {}
                race_dict['player_name'] = race.player_name
                race_dict['race_class'] = str(race_class)
                race_dict['race_position'] = race.race_position
                race_dict['race_distance'] = race.race_distance
                race_dict['race_rating'] = str(race_rating).upper()
                race_dict['race_weight'] =  str(race_weight)
                race_dict['race_date'] = race.race_date
                race_lst.append(race_dict)
            player_dict['race_lst'] = race_lst
            player_lst.append(player_dict)


        data_dict = {}
        data_dict['player_lst'] = player_lst
        data_dict['headings'] = headings
        return HttpResponse(content=json.dumps(data_dict), status=200, content_type="application/json")
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err = "\n".join(traceback.format_exception(*sys.exc_info()))
        print(err)
        return HttpResponse(content=json.dumps(err), status=406, content_type="application/json")



@require_POST
@login_required
def api_create_player_details(request):
    try:        
        user=request.user
        Player.objects.all().delete()
        Race.objects.all().delete()
        Heading.objects.all().delete()
        
        page_url = request.POST.get('page_url')     
        if page_url in [None,'','undefined']:
            return HttpResponse(content=json.dumps('Please Fill Page Url'), status=406, content_type="application/json")
        page = requests.get(page_url)
        page_data = BeautifulSoup(page.content,"html.parser")

        ###Heading 
        for heading in page_data.find_all(["h1", "h2"]):
            heading = Heading(
                heading = heading.text.strip(),
                created_by = user,
                modified_by = user,
                )
            heading.full_clean()
            heading.save()


        ###Players Details
        items = page_data.find_all("div",class_ = "form-runner-details-main")
        player_name = [item.find(class_="horseName bold").get_text() for item in items]
        player_idex_num = [item.find(class_="number bold").get_text() for item in items]
        player_num = [item.find(class_="horseNumber").get_text() for item in items]  
        player_weight = [item.find(class_="horseWeight").get_text() for item in items]
        player_rating = [item.find(class_="RTG").get_text() for item in items]
        #previous Datas   


        table = page_data.find_all("table",class_ = "runsTable margin-top-10")
        if table not in [None,'',[]]:
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
                        created_by = user,
                        modified_by = user,
                        )
                    player.full_clean()
                    player.save()

                for j in range(0,table_len):
                    results = table[j].find_all('tr', attrs={'class':'form-row'})

                    for result in results: 
                        race_position = result.find('td', attrs={'class':'previousRunsLeftTableCell'}).text 
                        description = result.find('td', attrs={'class':'align-top'}).text 

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


                        ###getClass
                        def getClass(code_value1): 
                            array2 = re.findall(r'(?<=\dm)(.*)(?=\$)', code_value1)
                            return array2
                        race_class = getClass(code_value1) 


                        ###getWeight
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
                                created_by = user,
                                modified_by = user,
                                )
                            race.full_clean()
                            race.save()
            return HttpResponse(content=json.dumps('Player Details Create Successfully'), status=200, content_type="application/json")
        return HttpResponse(content=json.dumps("Server Error, URL Not Found"), status=406, content_type="application/json")
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err = "\n".join(traceback.format_exception(*sys.exc_info()))
        print(err)
        return HttpResponse(content=json.dumps(err), status=406, content_type="application/json")

