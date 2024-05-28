# Úkol 2: https://github.com/andywaltlova/programovani-v-pythonu-jaro-2024/blob/main/ukoly/ukol-2-zadani.md
# Autor: Dita Hronová

import requests
import json

# Pekne reseni!
# Chvalim:
#   - jednoduchost a citelnost
#   - strukturu: oddeleni jednotlivych kroku (1. ziskani dat, 2. transformace dat a 3. zapis dat)
#   - zjisteni, ze enumerate ma parametr `start`
#   - pruchod seznamem dat jen jednou
# Par podnetu k zamysleni:
#   - Ktere hodnoty v kodu by bylo vhodne definovat jako konstanty?
#   - Co kdyz ve `finally` bloku dojde rovnez k timeoutu?
#   - Pro jednotlive kroky (ne nutne vsechny) by se nabizelo pouziti funkci.

try:
    response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10', timeout=0.001)
    data = response.json()
except requests.Timeout:
    print('Jsi příliš nedočkavá/ý.')
finally:
    response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10', timeout=0.5)
    # Kdyz by try blok probehl bez vyjimky, tady si `data` prepiseme. Prirazeni v try bloku je tak zbytecne.
    # V idealnim kodu (bez ukazky timeoutu) bychom finally blok uplne vypustili a do except bloku pridali ukonceni
    # programu (`sys.exit()`).
    data = response.json()


cat_facts = []

for index, item in enumerate(data[:10], start=1):
    cat_facts.append(f"{index}. {item['text']}")

print(cat_facts)

with open('kocici_fakta.json', mode='w', encoding='utf-8') as output_file:
    json.dump(cat_facts, output_file, indent=4)
