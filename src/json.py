import requests
import pandas as pd

#genera la url segun las condiciones dadas
def Gen_url(provincia,year):
    est_prov = {'Sevilla': '5783',
                'Madrid': '3129',
                'Bilbao': '1082',
                'Barcelona': '0076',
                'Valencia': '8414A'}
    url = f'https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/{year[0]}-01-01T00:00:00UTC/fechafin/{year[len(year)-1]}-12-31T23:59:59UTC/estacion/{est_prov[provincia]}'
    return weather(url)

#realiza la peticion    
def weather(url):
    token=open("./input/key.txt").readlines()[0]
    token = token.strip()
    response = requests.get(url, headers={"api_key": token})
    return response.json()

#Extrae la url que esta en datos y a su vez uso la funcion weather para obtener la informacion en .json
def data_weather(x):
    return pd.DataFrame(weather(x['datos']))

#Extrae la url que esta en metadatos y a su vez uso la funcion weather para obtener la informacion en .json
def metadata_weather(x):
    return pd.DataFrame(weather(x['metadatos']))

