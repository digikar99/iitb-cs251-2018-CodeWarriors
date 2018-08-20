#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import json
from datetime import datetime
import random

def iss_location():
    link = 'http://api.open-notify.org/iss-now.json'
    pg = requests.get(link)
    loc_dict = json.loads(pg.text)['iss_position']
    print('Current Location of ISS:')
    print('Latitude:', loc_dict['latitude'])
    print('Longitude:', loc_dict['longitude'])

def pass_time(lat,lng):
    link = 'http://api.open-notify.org/iss-pass.json?lat={0}&lon={1}'.format(str(lat),str(lng))
    pg = requests.get(link)
    time_list = json.loads(pg.text)['response']
    pos = random.randint(0,4)
    timestamp = time_list[pos]['risetime']
    dt = datetime.fromtimestamp(timestamp)
    print("Date:", str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year))
    print("Time:", str(dt.hour) + ":" + str(dt.minute))
    dur = int(time_list[pos]['duration'])
    dur_min = dur // 60
    dur_sec = dur % 60
    print("For:", str(dur_min) + " minute(s) and " + str(dur_sec) + " second(s)")
    
def people_info():
    link = "http://api.open-notify.org/astros.json"
    pg = requests.get(link)
    people_list = json.loads(pg.text)['people']
    print("People currently in space: ", len(people_list))
    for i,person in zip(range(len(people_list)), people_list):
        print(str(i+1)+".", person['name'])

iss_location()
print('Enter Details to know when ISS will pass over a location:')
lat = float(input('Latitude: '))
lng = float(input('Longitude: '))
pass_time(lat,lng)
people_info()
    
