import requests

API_KEY = 'YiLRKz33s/9rKRZAVD1gag==2Ue5RVRY4ijqhCOl'
API_URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_data(name):
    """
    Fetches the animal data for the given name.

    Returns:
        A list of animal dictionaries.
    """
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(f"{API_URL}?name={name}", headers=headers)
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print(f"Error: API request failed with status code "
              f"{response.status_code}")
        return []
