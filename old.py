import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_race.settings')

import django
django.setup()

from django.contrib.auth.models import User
from django.db import transaction


import requests
from bs4 import BeautifulSoup
import pandas 
import re
from datetime import datetime
from app_race.models import Player  #Vishnupriya

url = "https://report.racenet.com.au/templates/HJHHcCdef?meeting=devonport-20200913&race=toorak-toff-at-kingsley-park-benchmark-6-race-1"
# url = "https://report.racenet.com.au/templates/HJHHcCdef?meeting=devonport-20200913&race=toorak-toff-at-kingsley-park-benchmark-6-race-1"
page = requests.get(url)
page_data = BeautifulSoup(page.content,"html.parser")
#print(page_data)

# Heading 
for heading in page_data.find_all(["h1", "h2"]):
    print(heading.name + ' ' + heading.text.strip())
# Heading END


    # print(111111111111,heading.name)
    # print(2222222222222,heading.text.strip( ))

    # name = heading.text.strip( )[0]
    # print('name',name)

    if heading.name == 'h2':
        code_value1 = heading.text
        def getDistance(code_value1): 
            array = re.findall(r'[0-9]+m ', code_value1)
            return array
        array = getDistance(code_value1) 
        current_race_distance = array[0]
        # print('current_race_distance',current_race_distance)


        def getClass(code_value1): 
            array2 = re.findall(r'(?<=\dm)(.*)(?=\$)', code_value1)
            return array2
        race_class = getClass(code_value1) 
        print('race_class',race_class)








# #Players Details
# items = page_data.find_all("div",class_ = "form-runner-details-main")
# player_name = [item.find(class_="horseName bold").get_text() for item in items]
# player_idex_num = [item.find(class_="number bold").get_text() for item in items]
# player_num = [item.find(class_="horseNumber").get_text() for item in items]  
# player_weight = [item.find(class_="horseWeight").get_text() for item in items]
# player_rating = [item.find(class_="RTG").get_text() for item in items]
# #previous Datas   
# #all form Rows HTML content


# table = page_data.find_all("table",class_ = "runsTable margin-top-10")
# table_len = len(table)
# table_type = type(table)
# table_index = type(table[1])
# table_num_tr = len(table[1].find_all('tr'))
# results = table[0].find_all('tr', attrs={'class':'form-row'})

# for result in results: 
#     name = result.find('td', attrs={'class':'previousRunsLeftTableCell'}).text # result not results
#     description = result.find('td', attrs={'class':'align-top'}).text # result not results

#     ##date
#     match = re.search(r'\d{2}/\d{2}/\d{4}', description)
#     date = datetime.strptime(match.group(), '%d/%m/%Y').date()

#     ###Number
#     def getNumbers(description): 
#         array = re.findall(r'[0-9]+m ', description)
#         return array
#     array = getNumbers(description) 
#     array = list(filter(lambda x: len(x) == 6, array))
#     # print(*array) 


#     ###Rating
#     def getNumbers2(description): 
#         re.compile('[a-z]+')
#         array1 = re.findall(r'Rtg: +[0-99]', description)
#         return array1
#     array1 = getNumbers2(description) 
#     # array1 = list(filter(lambda x: len(x) == 6, array1))
#     # print(*array1) 

#     # (?<=Synthetic )(.*)(?=True )


#     # start_index2 = description.find('Rtg:') + 4
#     # end_index2 = description.find('horse(s')
#     # if end_index2 != -1:
#     #     code_value2 = description[start_index2 : end_index2].strip()        
#     #     # print('code_value2',code_value2)

#     # start_index1 = description.find('Synthetic') + 9
#     # end_index1 = description.find('Hcp')
#     # if start_index1 != -1:
#     #     if end_index1 != -1:
#     #         code_value1 = description[start_index1 : end_index1].strip()
#     #         # print('code_value1',code_value1)

#     # # start_index1 = description.find('Synthetic') + 9
#     # end_index3 = description.split('(')
#     # print('end_index3',end_index3)
#     # if end_index1 != -1:
#     #     code_value1 = description[0 : end_index1].strip()
#     #     print('code_value1',code_value1)

#     # code_value1 = description[::end_index1].strip()
#     # print('code_value1',code_value1)

#     # s = "abc123AUG|GAC|UGAasdfg789"
#     # pattern = "AUG\|(.*?)\|UGA"
#     # substring = re.search(pattern, s).group(1)
#     # print(substring)

#     # start_word = "Synthetic"
#     # end_word = "Hcp"
   


#     # # re.search(r'\d{2}/\d{2}/\d{4}', description)
#     # expr = re.search(r'\*' + start_word + '(.+?)' + end_word)
#     # match_list = list(map(lambda x: x.strip(), expr.findall(description)))
#     # match_list = list(filter(lambda x: x[:2] == "BM", match_list))
#     # print(match_list)



#     # start_word = "Synthetic"
#     # end_word = "Hcp"
#     # expr = re.compile(r'.*' + start_word + '(.+?)' + end_word)
#     # match_list = list(map(lambda x: x.strip(), expr.findall(description)))
#     # match_list = list(filter(lambda x: x[:2] == "BM", match_list))
#     # print('match_list',match_list)

#     # # if start_index != -1:
#     # #     code_value = description[start_index :: ].split(' ')[0].strip()
#     # code_value = description[ :: end_index ].split(' ')[-1].strip()

#     # test_val = 'Synthetic'
#     # for i in description:
#     #     if test_val in i:
#     #         if test_val == 'Synthetic':
#     #             print(4444444444,i.split(' ')[1])


# rng = len(player_name)
# for i in range(0,rng):
#     player = Player(
#         player_name = player_name[i],
#         player_idex_num = player_idex_num[i],
#         player_num = player_num[i],
#         player_weight = player_weight[i],
#         player_rating = player_rating[i],
#         )
#     player.full_clean()
#     player.save()





# rng = len(player_name)
# for i in range(0,rng):
#     race = Race(
#         player = player_name[i],
#         race_name = player_idex_num[i],
#         race_rating = player_num[i],
#         race_date = player_weight[i],
#         )
#     race.full_clean()
#     race.save()
