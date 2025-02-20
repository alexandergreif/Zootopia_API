import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def fetch_data(name):
    """Fetch animal data from the API for the given name."""
    API_URL = f'https://api.api-ninjas.com/v1/animals?name={name}'
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(API_URL, headers=headers)
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return []