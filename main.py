import requests
import os
import datetime
import pandas as pd
import numpy as np


### CHANGE PARAMS HERE ###
img_path = '/code/everypixel/pictures/' #INSERT PATH HERE
api_secret = "sjkmZwk6mk82XtR622aDgoyAIRJpa0700YoeEJIdrmze9hOW" #ADD SECRET HERE
api_key = "PY7JPmcJmlRaktG05ADnT2d1" #ADD CLIENT ID HERE

url_ver = "https://api.everypixel.com/v1"


### DONT TOUCH ME BELOW ###
files = [f for f in os.listdir(img_path) if os.path.isfile(os.path.join(img_path,f))]

inferences = {}
for f in files:
    
    with open(os.path.join(img_path,f),'rb') as image:
        data = {'data': image}
        keywords = requests.post('https://api.everypixel.com/v1/keywords', files=data, auth=(api_key, api_secret)).json()
        inferences[f] = keywords['keywords']


df_all = pd.DataFrame()
for d in inferences:
    df = pd.DataFrame(inferences[d]).set_index('keyword').rename(columns={'score':d})
    df_all = pd.concat([df_all, df], axis=1)
df_all = df_all.fillna(0).sort_index()


df_all.to_csv('test.csv')