from requests_html import HTMLSession


def weather_forecast(city):

    html = HTMLSession()

    url = f'https://www.google.com/search?q=tempo+{city}'

    response = html.get(url)

    city = response.html.find('#wob_loc')[0].text
    state = response.html.find('#wob_dc')[0].text
    date = response.html.find('#wob_dts')[0].text.capitalize()
    rain = response.html.find('#wob_pp')[0].text.capitalize()
    temperature = response.html.find('#wob_tm')[0].text
    maximum = response.html.find('.wob_df')[0].text[5:7]
    minimum = response.html.find('.wob_df')[0].text[11:13]

    return (f'{city}, {date}\nPrevisão: Máx {maximum}°C, Min {minimum}°C' +
            f'\nTemperatura atual: {temperature}°C\n{state}' +
            f'\nChance de chuva: {rain}')
