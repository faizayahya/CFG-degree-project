import requests
from settings import rapid_headers, rapid_url


entry = input("How are you feeling today?\n")
querystring = {"text": entry}

response = requests.request("GET", rapid_url, headers=rapid_headers, params=querystring)

analysis = response.json()
mood_score = analysis["score"]
