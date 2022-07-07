import requests

def get_dict():
    response = requests.get('https://jsonkeeper.com/b/QN1I')
    data = response.json()
    return data
