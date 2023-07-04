from os import sep
import requests
from requests.models import ReadTimeoutError 
import csv
import pandas as pd 

def main():
    url = "https://pokeapi.co/api/v2/pokemon/"
    args = {'offset' : 0, 'limit' : 1118 }
    response = requests.get(url, params=args)
    name = []
    if response.status_code == 200:
        payload = response.json()
        results = payload.get("results", [])        
        if results:
            for pokemon in results:
                name.append(pokemon['name'])
        return name
    else:
        return 404

def get_pokemon (id):
    args = {'offset' : 0, 'limit' : 1118 }
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}/", params= args)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get("results", [])

        pokemon_data={'ID':'',
                   'name':'',
                  'height':'',
                  'abilities':'',
                   'weight':''}
        
        pokemon_data['name']=results['name']
        pokemon_data['height']=results['height']
        pokemon_data['abilities']=len(results['abilities'])
        pokemon_data['ID']=results['ID']
        pokemon_data['weight']=results['weight']

        
       

        return pokemon_data

def archivo ():
    star_index='0'
    end_index='5'
    names = main()
    headers = ['name', 'weight', 'height','abilities','ID']
    resultado=headers[int(star_index): int(end_index)]
    with open('pokemon_details.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=resultado)
        writer.writeheader()
       

        for id in range(1, 1119):
            id =str(id)
            rows =get_pokemon(id)
            writer.writerows(rows)


    f.close()

if __name__ == "__main__":
    archivo()
