import requests
import json
from bs4 import BeautifulSoup

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats?country=India"

querystring = {"country" :  "India"}
headers = {
        "x-rapidapi-host": "covid-19-coronavirus-statistics.p.rapidapi.com",
        "x-rapidapi-key": "e5325ad406msh6e89cf3203bc081p1f51cejsna214611875f1"
    } 

response = requests.request("GET", url, headers = headers, params = querystring)
ourdata = response.json()

# checklList = ourdata["message"] ,ourdata["data"]["covid19Stats"][0]["country"],  ourdata["data"]["covid19Stats"][0]["confirmed"], ourdata["data"]["covid19Stats"][0]["deaths"], ourdata["data"]["covid19Stats"][0]["recovered"] ] 

checklList = {

    "LastChecked" : ourdata["data"]["lastChecked"],
    "message" : ourdata["message"],
    "country" : ourdata["data"]["covid19Stats"][0]["country"],
    "confirmedCases" : ourdata["data"]["covid19Stats"][0]["confirmed"],
    "deaths" : ourdata["data"]["covid19Stats"][0]["deaths"],
    "recovered" : ourdata["data"]["covid19Stats"][0]["recovered"] 
}


with  open("newfile.json", "w") as json_file:
    json.dump(checklList, json_file, indent= 4)