
# yourapp/utils.py
import requests
from django.conf import settings

def fetch_adzuna_jobs():
    base_url = "https://api.adzuna.com/v1/api/jobs/in/search/1"
    params = {
        'app_id': settings.ADZUNA_APP_ID,
        'app_key': settings.ADZUNA_API_KEY,
        'results_per_page': 20,
        'what': 'software developer',
        'where': 'india',
        'content-type': 'application/json'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching jobs: {e}")
        return None