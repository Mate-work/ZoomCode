import sys
import jwt
import http.client
import datetime
import json
# Go to 
# Then get API Key, API Secret and insert below
api_key = 'p-zpPVCrQMy4SnOlAV9BGw'
api_sec = '8NWGe7uCQd8574r8EKpZJi3nrNRm3UPezoY7'


payload = {
'iss':api_key,
'exp': datetime.datetime.now() + datetime.timedelta(hours=2)
}

jwt_encoded = str(jwt.encode(payload, api_sec), 'utf-8')

conn = http.client.HTTPSConnection("api.zoom.us")
headers = {
'authorization': "Bearer %s" % jwt_encoded,
'content-type': "application/json"
}

def displayMeetings(user_id):
    #retrieve list of meeting ids
    for id in meeting_ids:
        conn.request("GET", "/v2/meetings/" + str(response_obj[id]) + "/invitation", headers=headers)
        res = conn.getresponse()
        response_string = res.read().decode('utf-8')
        response_obj = json.loads(response_string)
        # check if date has passed then move to past meetings
        # display on page
    
def removeMeeting(user_id, meeting_id):
    pass

