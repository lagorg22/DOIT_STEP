# დავალების შესასრულებლად გამოიყენეთ API: https://rickandmortyapi.com/api
# წაიკითხეთ თითოეული პერსონაჟის ინფორმაცია, მათი ეპიზოდები და JSON ფაილში ჩაწერეთ key მნიშვნელობა პერსონაჟის სახელი,
# value ეპიზოდების სახელი რომელშიც მონაწილეობს

import requests
import json

characters_data = []
episodes_data = {}


def get_char_data(url: str):
    resp = requests.get(url)
    if resp.status_code != 200:
        return

    data = resp.json()
    for current_info in data['results']:
        curr = {
            'name': current_info['name'],
            'episode_id': [id[id.rfind('/')+1:] for id in current_info['episode']]
        }
        characters_data.append(curr)
    next_url = data['info']['next']
    if next_url:
        get_char_data(next_url)

get_char_data('https://rickandmortyapi.com/api/character')

def get_episode_data(url: str):
    resp = requests.get(url)
    if resp.status_code != 200:
        return

    data = resp.json()
    for current_info in data['results']:
        episodes_data[current_info['id']] = current_info['name']
    next_url = data['info']['next']
    if next_url:
        get_episode_data(next_url)

get_episode_data('https://rickandmortyapi.com/api/episode')

result = {}

for character in characters_data:
    name = character['name']
    episode_ids = character['episode_id']
    episodes = []
    for ep_id in episode_ids:
        episodes.append(episodes_data[int(ep_id)])

    #mkvdari da cocxali xalxi gaertianebulia
    if name in result:
        result[name] += episodes
    else:
        result[name] = episodes

with open('result.json', 'w') as f:
    json.dump(result, f, indent=4)


