import os

# sentiment analysis keys

rapid_headers = {
    "X-RapidAPI-Key": "0f7fcf82f7mshab0cc347d0f8bfbp1062cdjsn2303b677e6cf",
    "X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com"
}

rapid_url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

# spotipy
os.environ['SPOTIPY_CLIENT_ID'] = '880217de6cf947fea5543c7d419cdc62'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'a9191b8701264865affad32c351bd378'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost/'
