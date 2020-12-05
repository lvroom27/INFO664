import requests
import json

headers = {
    'User-Agent': 'Lauras Project'
}

payload = {'GET': 'https://api.rawg.io/api/games?dates=2019-01-01,2019-12-31&ordering=-added'}

url = 'https://api.rawg.io/api/games'

r = requests.get(url, headers=headers, params=payload)

data_dict = json.loads(r.text)
game_count = len(data_dict['results'][0]['name'])

processed_data = []

for i in range(0, 1):
    processed_data.append({'name': data_dict['results'][i]['name']})
    processed_data.append({'rating': data_dict['results'][i]['rating']})
    processed_data.append({'released': data_dict['results'][i]['released']})

    genre_count = len(data_dict['results'][i]['genres'])
    for x in range(0, genre_count):
        genres = []
        genres.append({'genre': data_dict['results'][i]['genres'][x]['name']})
        processed_data.append({'genres': genres})

    platform_count = len(data_dict['results'][i]['platforms'])
    for y in range(0, platform_count):
        platforms = []
        platforms.append({'platform': data_dict['results'][i]['platforms'][y]['platform']['name']})
        processed_data.append({'platforms': platforms})

    screenshot_count = len(data_dict['results'][i]['short_screenshots'])
    for z in range(0, screenshot_count):
        screenshots = []
        screenshots.append({'screenshot': data_dict['results'][i]['short_screenshots'][z]['image']})
        processed_data.append({'screenshots': screenshots})

    tag_count = len(data_dict['results'][i]['tags'])
    for k in range(0, tag_count):
        tags = []
        tags.append({'tag': data_dict['results'][i]['tags'][k]['name']})
        processed_data.append({'tags': tags})
    processed_data.append({'clip': data_dict['results'][i]['clip']['clip']})

print(json.dumps(processed_data, indent=2))