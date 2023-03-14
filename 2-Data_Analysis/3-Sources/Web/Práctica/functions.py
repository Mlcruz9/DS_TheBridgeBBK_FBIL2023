import hashlib
import requests
import datetime
import pandas as pd
import variables as var

def hash_params(timestamp,priv_key,pub_key):
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params

def hacer_peticion(letra, offset = None):

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

    pub_key = var.pub_key
    priv_key = var.priv_key

    params = {'ts': timestamp, 
            'nameStartsWith': letra,
            'apikey': pub_key, 
            'hash': hash_params(timestamp,priv_key,pub_key),
            'offset': offset,
            'limit': 100};

    url = 'http://gateway.marvel.com/v1/public/characters'

    res = requests.get(url,params=params)

    characters = res.json()

    return characters


def crear_csv_comics(letra, nombre_archivo, offset=None):

    letra = letra

    characters = hacer_peticion(letra, offset)

    dict_comics = {'id': [], 'name': [], 'picture_url': []}

    for i in range(len(characters['data']['results'])):

        dict_comics['name'].append(characters['data']['results'][i]['name'])
        dict_comics['id'].append(characters['data']['results'][i]['id'])
        path = characters['data']['results'][i]['thumbnail']['path']
        extension = characters['data']['results'][i]['thumbnail']['extension']

        dict_comics['picture_url'].append(f'{path}.{extension}')

        comics_df = pd.DataFrame(dict_comics)

        comics_df.to_csv(nombre_archivo)