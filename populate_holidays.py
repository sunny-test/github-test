import re
import os
from random import *
import datetime

from faker import Faker

fr = open("holidays.txt")
holidays = []
# reading holidays file
for i in fr:
	i = i.strip()
	holidays.append(re.split(r"\s+", i, 3))
fr.close()

os.environ['DJANGO_SETTINGS_MODULE'] = 'Tracker.settings'

import django

django.setup()

from holidays.models import *

f1 = Faker()
	

def populate():
	for holiday in holidays:
		year = holiday[0]
		date = holiday[1]
		day = holiday[2]
		desc = holiday[3]
		date_time_obj = datetime.datetime.strptime(date, '%Y/%m/%d')
		date = date_time_obj
		Holidays.objects.create(year=year, date=date, day=day, desc=desc)
		
populate()