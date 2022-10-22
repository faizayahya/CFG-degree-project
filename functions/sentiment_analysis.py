import requests
# from settings import rapid_headers, rapid_url

rapid_headers = {
    "X-RapidAPI-Key": "0f7fcf82f7mshab0cc347d0f8bfbp1062cdjsn2303b677e6cf",
    "X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com"
}

rapid_url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

def mood_analysis_api(querystring):
    try:
        response = requests.request("GET", rapid_url, headers=rapid_headers, params=querystring)
    except requests.exceptions.RequestException as err:
        print(err)
        raise
    return response

def mood_analysis(journal_entry):
    querystring = {"text": journal_entry}
    analysis = mood_analysis_api(querystring).json()
    mood_score = analysis["score"]

    if mood_score == 0:
        raise Exception("Sorry, didn't quite get that, let's try again")
    else:
        return mood_score

