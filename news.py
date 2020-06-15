import requests
from datetime import datetime

api_key = 'YOUR_API_KEY'


def news_today():
    api = 'http://newsapi.org/v2/top-headlines?sources=google-news-br&apiKey='
    response = requests.get(api + api_key).json()

    i = 0

    string_with_articles = ''
    for article in response['articles']:
        i += 1
        if i > 5:
            break
        title = article['title']
        author = article['author']
        description = article['description']
        url = article['url']
        date = article["publishedAt"]
        date = datetime.strptime(date[:10], '%Y-%m-%d')
        date = date.strftime("%d/%m/%Y")

        if author:
            string_with_articles += (
                f'\n\t{title.upper()}\n' +
                f'ESCRITO POR: {author.upper()} {date}\n' +
                f'{description}\nPara ler mais: {url}\n')
        else:
            string_with_articles += (
                f'\n\t{title.upper()}\n{date}\n{description}\n' +
                f'Para ler mais: {url}\n')

    return string_with_articles


def news_by_subject(subject):
    api = f'http://newsapi.org/v2/everything?q={subject}&apiKey='
    response = requests.get(api + api_key).json()
    if response['totalResults'] == 0:
        return f'Não foi encontrada nenhuma matéria relativa a {subject}'

    string_with_articles = ''
    for article in response['articles']:
        i = 0

        date = article["publishedAt"]
        date = datetime.strptime(date[:10], '%Y-%m-%d')
        today = datetime.now()
        diff = today - date

        if diff.days <= 10:
            i += 1
            if i > 5:
                break

            title = article['title']
            author = article['author']
            description = article['description']
            url = article['url']
            date = date.strftime("%d/%m/%Y")

            if author:
                string_with_articles += (
                    f'\n\t{title.upper()}\n' +
                    f'ESCRITO POR: {author.upper()} {date}\n' +
                    f'{description}\nPara ler mais: {url}\n')
            else:
                string_with_articles += (
                    f'\n\t{title.upper()}\n{date}\n{description}\n' +
                    f'Para ler mais: {url}\n')
    return string_with_articles
