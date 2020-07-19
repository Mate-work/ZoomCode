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



def createMeeting(start_time, duration, topic, participants):
    data = json.dumps({
      "duration": duration,
      "start_time": start_time,
      "topic": topic,
    })
    conn.request("POST", "/v2/users/z5164086@student.unsw.edu.au/meetings", body=data, headers=headers)
    res = conn.getresponse()
    response_string = res.read().decode('utf-8')
    response_obj = json.loads(response_string)
    print(response_obj)
    
    conn.request("GET", "/v2/meetings/" + str(response_obj['id']) + "/invitation", headers=headers)
    res = conn.getresponse()
    response_string = res.read().decode('utf-8')
    response_obj = json.loads(response_string)

    print(response_obj['invitation'])
    
    
    

    
            
createMeeting("2021-08-30T22:00:00Z", 60, "TestTopic", ["jamesclark@outlook.com.au"])