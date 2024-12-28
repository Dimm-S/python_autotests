import requests
import json

URL = 'https://api.pokemonbattle.ru/v2'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : 'TOKEN'}

body_createPokemon = {
    "name": "Double Flip",
    "photo_id": 666
}

response = requests.post(url = f'{URL}/pokemons',
                         headers = HEADERS,
                         json = body_createPokemon)
print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))

POKEMON_ID = response.json()['id']

response = requests.put(url = f'{URL}/pokemons',
                        headers = HEADERS,
                        json = {
                            "pokemon_id": POKEMON_ID,
                            "name": "Triple Axel",
                            "photo_id": 666,
                        })
print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))

response = requests.post(url = f'{URL}/trainers/add_pokeball',
                         headers = HEADERS,
                         json = {
                             "pokemon_id": POKEMON_ID
                         })
print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))
