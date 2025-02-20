import requests
import json

def fetch_data(name):
    """Fetch animal data from the API for the given name."""
    API_KEY = 'YiLRKz33s/9rKRZAVD1gag==2Ue5RVRY4ijqhCOl'
    API_URL = f'https://api.api-ninjas.com/v1/animals?name={name}'
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(API_URL, headers=headers)
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return []