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
def api_result_list_get(request):
    try:
        user = request.user
        results = Result.objects.filter(is_active=True).order_by('id')
        result_lst = []
        for result in results:
            result_dict = {}
            result_dict['raceno'] = result.raceno
            result_dict['race_primarykey'] = result.race_primarykey
            result_dict['main_head'] = result.main_head
            result_dict['main_subhead'] = result.main_subhead
            result_dict['race_distance'] = result.race_distance

            race_detail_lst = []
            resultdetails = ResultDetails.objects.filter(is_active=True,main_head=result.main_head).order_by('id')
            for index,resultdetail in enumerate(resultdetails):
                result_details_dict = {}
                result_details_dict['result_id'] = resultdetail.id
                result_details_dict['Pl'] = resultdetail.Pl
                result_details_dict['h_no'] = resultdetail.h_no
                result_details_dict['horse_pedigree'] = resultdetail.horse_pedigree
                result_details_dict['desc'] = resultdetail.desc
                result_details_dict['trainer'] = resultdetail.trainer
                result_details_dict['jockey'] = resultdetail.jockey
                result_details_dict['wt'] = resultdetail.wt
                result_details_dict['al'] = resultdetail.al
                result_details_dict['dr'] = resultdetail.dr
                result_details_dict['sh'] = resultdetail.sh
                result_details_dict['won_by'] = resultdetail.won_by
                result_details_dict['dist_win'] = resultdetail.dist_win
                result_details_dict['rtg'] = resultdetail.rtg
                result_details_dict['odds'] = resultdetail.odds
                result_details_dict['time'] = resultdetail.time
                result_details_dict['raceno'] = resultdetail.raceno
                result_details_dict['race_primarykey'] = resultdetail.race_primarykey
                result_details_dict['main_head'] = resultdetail.main_head
                result_details_dict['main_subhead'] = resultdetail.main_subhead
                result_details_dict['race_distance'] = resultdetail.race_distance
                race_detail_lst.append(result_details_dict)
            result_dict['race_detail_lst'] = race_detail_lst
            result_lst.append(result_dict)
        return HttpResponse(content=json.dumps(result_lst), status=200, content_type="application/json")
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err = "\n".join(traceback.format_exception(*sys.exc_info()))
        print(err)
        return HttpResponse(content=json.dumps(err), status=406, content_type="application/json")



@require_POST
@login_required
def api_create_result_details(request):
    try:        
        user=request.user      
        page_url = request.POST.get('page_url')     
        if page_url in [None,'','undefined']:
            return HttpResponse(content=json.dumps('Please Fill Page Url'), status=406, content_type="application/json")
        page = requests.get(page_url)
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
                        datas.append(cols)
                        data_len = len(datas)

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


                    result = Result(
                        raceno = raceno,
                        race_primarykey = race_primarykey,
                        main_head = main_head,
                        main_subhead = main_subhead,
                        race_distance = race_distance,
                        created_by = user,
                        modified_by = user,
                        )
                    result.full_clean()
                    result.save()


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

                        resultdetails = ResultDetails(
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
                            created_by = user,
                            modified_by = user,
                            )
                        resultdetails.full_clean()
                        resultdetails.save()
            return HttpResponse(content=json.dumps('Player Details Create Successfully'), status=200, content_type="application/json")
        return HttpResponse(content=json.dumps("Server Error, URL Not Found"), status=406, content_type="application/json")
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err = "\n".join(traceback.format_exception(*sys.exc_info()))
        print(err)
        return HttpResponse(content=json.dumps(err), status=406, content_type="application/json")

