import requests
from bs4 import BeautifulSoup
import re


def soccer_today():
    url = 'http://www.futebolnatv.com.br/jogos-hoje/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    list_matches = []
    for value in soup.find_all('td'):
        matches = value.select('div', _class='col-md-12')
        for match in matches:
            list_matches.append(match.text)

    leagues = []
    for i in range(0, len(list_matches), 4):
        leagues.append(list_matches[i].rstrip('\n').strip())

    teams = []
    for i in range(1, len(list_matches), 4):
        team_1 = list_matches[i].strip()
        team_1 = re.sub('[^A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ ]', '',
                        team_1).strip()

        team_2 = list_matches[i + 1].strip()
        team_2 = re.sub('[^A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ ]', '',
                        team_2).strip()

        teams.append(f'{team_1} x {team_2}')

    channels = []
    for i in range(3, len(list_matches), 4):
        channels.append(list_matches[i].strip())

    for date in soup.select('ol', _class='breadcrumb'):
        date = date.select_one('li a').text.strip()
        break

    hours = []
    for horary in soup.select('th h4 b'):
        hours.append(horary.text)

    string_with_matches = ''
    for i in range(len(channels)):
        string_with_matches += (
            f'\nCanal: {channels[i]}\n{leagues[i]} - {teams[i]}\n' +
            f'Horário: {hours[i]}\n')

    return (f'{date}\n' + string_with_matches)
