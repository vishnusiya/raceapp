import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_race.settings')

import django
django.setup()

from django.contrib.auth.models import User
from django.db import transaction
import requests
from datetime import datetime
from app_race.models import *  #Vishnupriya
import string 

if __name__ == '__main__':
    print ('Starting database population...')
    print ("Creating Admin User")
    with transaction.atomic():
        username = 'admin'
        email = 'admin@getnada.com'
        password = "admin@123*"
        first_name = 'admin'
        last_name = ''
        mobileno = '9876543210'
        
        admin_user = User(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_superuser=True,
        )
        admin_user.set_password(password)
        admin_user.full_clean()
        admin_user.save()
        print ("SuperAdmin User Created Sucessfully!!!")

        