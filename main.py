import requests
import os
import datetime


### CHANGE PARAMS HERE ###
img_path = '/code/everypixel/pictures/' #INSERT PATH HERE
api_secret = "sjkmZwk6mk82XtR622aDgoyAIRJpa0700YoeEJIdrmze9hOW" #ADD SECRET HERE
api_key = "PY7JPmcJmlRaktG05ADnT2d1" #ADD CLIENT ID HERE


url_ver = "https://api.everypixel.com/v1"




### DONT TOUCH ME BELOW ###
files = [os.path.join(img_path,f) for f in os.listdir(img_path) if os.path.isfile(os.path.join(img_path,f))]
for f in files:
    with open(f,'rb') as image:
        data = {'data': image}
        keywords = requests.post('https://api.everypixel.com/v1/keywords', files=data, auth=(api_key, api_secret)).json()
        print(keywords)