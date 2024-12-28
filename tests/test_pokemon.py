import requests
import pytest
import json

URL = 'https://api.pokemonbattle.ru/v2'

def test_statusCode():
    response = requests.get(url = f'{URL}/trainers',
                            params = {'trainer_id' : '11299'})
    print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))

    assert response.status_code == 200
    assert response.json()['data'][0]['id'] == '11299'