import requests
from settings import rapid_headers, rapid_url


def mood_analysis(journal_entry):
    querystring = {"text": journal_entry}

    response = requests.request("GET", rapid_url, headers=rapid_headers, params=querystring)

    analysis = response.json()
    mood_score = analysis["score"]

    if mood_score == 0:
        raise Exception("Sorry, didn't quite get that, let's try again")
    else:
        return mood_score

