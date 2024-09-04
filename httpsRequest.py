import urllib.request
import json
from urllib.error import HTTPError

def get_user_agent():
    return "Showdown Helper (Discord Bot)"  

def make_request_with_user_agent(url, user_agent):
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as response:
        return response.read().decode()



def getData(url):

    user_agent = get_user_agent()
    #print("User-Agent des Browsers:", user_agent)


    try:
        response = make_request_with_user_agent(url, user_agent)
        data = json.loads(response)
       # print("API-Antwort:", data)
    except HTTPError as e:
        print("HTTP Error:", e)

    return data
