#Úkol 2: https://github.com/andywaltlova/programovani-v-pythonu-jaro-2024/blob/main/ukoly/ukol-2-zadani.md
#Autor: Dita Hronová

import requests
import json

try:
    response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10', timeout=0.001)
    data = response.json()
except requests.Timeout:
    print('Jsi příliš nedočkavá/ý.')
finally:
    response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10', timeout=0.5)
    data = response.json()


cat_facts = []

for index, item in enumerate(data[:10], start=1):
    cat_facts.append(f"{index}. {item['text']}")

print(cat_facts)


with open('kocici_fakta.json', mode='w', encoding='utf-8') as output_file:
    json.dump(cat_facts, output_file, indent=4)


