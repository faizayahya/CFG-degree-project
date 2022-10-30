import os

# sentiment analysis keys

rapid_headers = {
    "X-RapidAPI-Key": "XXX",
    "X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com"
}

rapid_url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

# spotipy
os.environ['SPOTIPY_CLIENT_ID'] = 'XXX'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'XXX'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost/'
