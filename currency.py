import requests

url = 'https://economia.awesomeapi.com.br/json/all'


def currency_today(currency):
    response = requests.get(url).json()

    name = response[currency.upper()]["name"]
    bid = response[currency.upper()]["bid"]
    variation = response[currency.upper()]["pctChange"]

    string_with_values = (f'{name}\nPreço de compra: R${float(bid):.2f}\n' +
                          f'Percentual de variação: {variation}%')

    return string_with_values
