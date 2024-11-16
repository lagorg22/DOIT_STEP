# დავალების შესასრულებლად გამოიყენეთ API: https://rickandmortyapi.com/api
# წაიკითხეთ თითოეული პერსონაჟის ინფორმაცია, მათი ეპიზოდები და JSON ფაილში ჩაწერეთ key მნიშვნელობა პერსონაჟის სახელი,
# value ეპიზოდების სახელი რომელშიც მონაწილეობს

import requests
import json

url = 'https://rickandmortyapi.com/api/character'

data: dict = requests.get(url).json()

result = {ch['name']: ch['episode'] for ch in data['results']}

with open('result.json', 'w') as f:
    json.dump(result, f, indent=4)