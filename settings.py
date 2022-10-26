import os
# my settings:
rapid_headers = {
    'X-RapidAPI-Key': 'd89dbfec21msh0ac7cb89c5b57bdp1bff79jsn37bdf0cb0833',
    'X-RapidAPI-Host': 'twinword-sentiment-analysis.p.rapidapi.com'
  }
rapid_url = "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/"

# spotipy
os.environ['SPOTIPY_CLIENT_ID'] = '2e277b0ef82944c69f46360bff60ed8b'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'fde54d8c27d545cba469c0b2acd6dcf5'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost/'
