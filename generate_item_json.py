import os
import random
import string

folders = [['esine', 'E', 'avail_items'], ['hattu', 'H', 'avail_hats'], ['juoma', 'J', 'avail_drinks'], ['vaate', 'V', 'avail_clothings']]
adjecti = { 'E': ['', 'Käyttökelpoinen ', 'Näppärä ', 'Erittäin hyödyllinen ', 'Aivan jumalattoman kätevä '], 
            'H': ['', 'Kiva ', 'Säväyttävä ', 'Upea ', 'Aivan jumalattoman tyylikäs '], 
            'J': ['Tyhjä ', 'Loppumaisillaan oleva ', 'Laatutarkastettu ', 'Juuri avattu ', 'Korkkaamaton '], 
            'V': ['', 'Hyvin istuva ', 'Tahraton ', 'Tilaustyönä teetetty ', 'Ihailua ja kateutta herättävä ']}

item_json = {}
qr_items = {}

freq_by_rarity = {0: 10, 1: 5, 2:3, 3:2, 4:1}

for folder, t, db_name in folders:
    for filename in os.listdir('result/'+folder):
        if filename.endswith('png'):
            name = filename[:-5]
            rarity = int(filename[-5])
            i = t + filename[-5] + name
            description = adjecti[t][int(filename[-5])] + name.replace("_", " ")
            is_siili = "siili" in name
            number_to_generate = freq_by_rarity[rarity]
            if( is_siili ):
                number_to_generate = number_to_generate * 3
            for n in range(number_to_generate):
                if (is_siili):
                    key = 'BOI'+''.join([random.choice(string.ascii_letters + string.digits) for n in range(29)])
                else:
                    key = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
                while key in qr_items:
                    print("Duplicate?!")
                    key = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
                qr_items[key] = {"item": i, "type": db_name}


            item_json[i] = {"name": description, "url": os.path.join(folder, filename)}

import json
with open('items.json', 'w', encoding='utf8') as fp:
    json.dump(item_json, fp, ensure_ascii=False)
with open('qrcodes.json', 'w', encoding='utf8') as fp:
    json.dump(qr_items, fp, ensure_ascii=False)