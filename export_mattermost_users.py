import requests
import sys
from  itertools import repeat
import time
import json

PAGES = 10 # will retrive 10*200 Users
WAIT_SEC = 5
API_VERSION = '4'

if __name__ == "__main__":
    #check parametes
    if len(sys.argv) < 4:
        sys.exit("There must be 3 Parameters: mattermost server, username or email and password!")

    URL =  sys.argv[1] + '/api/v' + API_VERSION
    LOGINURL = URL+"/users/login"
    USERSURL = URL + "/users"

    #login
    login_json = {'login_id':sys.argv[2],'password':sys.argv[3]}
    r = requests.post(LOGINURL, json=login_json)
    if r.status_code == 200: #login worked
        print('loged in')
        auth ={"Authorization" : 'Bearer ' + r.headers['Token']}

        users = {}
        payload = {
            'page':0,
            'per_page': 200
            }
 
        for i in repeat(None, PAGES):    
            r = requests.get(USERSURL, params=payload, headers= auth ) #params = querysting
            if r.status_code == 200: #getting users worked
                print('retrived data')
                users['users']= r.json()
                payload['page'] = payload['page'] +1
                print("waiting ... 5 seconds")
                time.sleep(WAIT_SEC) #wait 5 seconds to not look suspices 

        users['date_of_data_retrival'] = time.time()

        # wenn fertig schiebt in .json file
        with open('user_data.json', 'w') as outfile:
            json.dump(users, outfile)
            print("dumped to file user_data.json")

