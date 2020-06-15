import requests
from googletrans import Translator
from datetime import datetime
from unidecode import unidecode

translator = Translator()

url = ('https://covid19-brazil-api.now.sh/api/report/v1/')


def covid_country(country):
    country = country.lower()
    country_en = translator.translate(country, dest='en').text
    if country_en.lower() == 'united states' or country_en.lower() == 'usa':
        country_en = 'us'

    url_country = url + country_en
    data = requests.get(url_country).json()
    if not data['data']:
        return 'O país informado não foi encontrado.'

    confirmed = data['data']['confirmed']
    deaths = data['data']['deaths']
    recovered = data['data']['recovered']
    date = data['data']['updated_at']
    date = datetime.strptime(date[:10], '%Y-%m-%d').date()
    date = date.strftime("%d/%m/%Y")
    return (
        f'País: {country.capitalize()}\nCasos confirmados: {confirmed}\n' +
        f'Mortos: {deaths}\nRecuperados: {recovered}\nData da consulta: {date}'
    )


def covid_state(state):
    data = requests.get(url).json()

    indice = 0
    for i in range(27):
        if unidecode(state.lower()) == unidecode(
                data['data'][i]['state'].lower()):
            indice = i
            state = data['data'][i]['state']
            break
    else:
        return 'O estado informado não foi encontrado.'

    confirmed = data['data'][indice]['cases']
    deaths = data['data'][indice]['deaths']
    date = data['data'][indice]['datetime']
    date = datetime.strptime(date[:10], '%Y-%m-%d').date()
    date = date.strftime("%d/%m/%Y")
    return (
        f'Estado: {state}\nCasos confirmados: {confirmed}\nMortos: {deaths}\n'
        + f'Data da consulta: {date}')
