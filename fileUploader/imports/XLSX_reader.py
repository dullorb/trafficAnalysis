import pandas as pd
from random import randint

def handle_file(file):
    reading = file.read()
    data = pd.read_excel(reading)
    length = data.size
    return grab_essentials(data)


def grab_essentials(pd_DataFrame):
    lat_and_long = []
    all_data = pd_DataFrame.to_dict('records')
    for x in all_data:
        r = randint(1, 100)
        if x['LATDECDG'] > 0:
            lat_and_long.append({'latitude': x['LATDECDG'], 'longitude': x['LONDECDG'], 'weight': r})
    return lat_and_long
