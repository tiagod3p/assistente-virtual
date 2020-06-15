import telebot
from weather_forecast import weather_forecast
from covid import covid_country, covid_state
from soccer import soccer_today
from news import news_today, news_by_subject
from currency import currency_today

token = "YOUR_TELEGRAM_TOKEN"
bot = telebot.TeleBot(token)
bot_name = bot.get_me().first_name


@bot.message_handler(commands=["start"])
def send_welcome(message):
    name = message.from_user.first_name
    bot.reply_to(
        message,
        (f'Olá {name}, eu sou o {bot_name}, como posso te ajudar?\n' +
         'Digite /help para saber os comandos que você pode utilizar.'))


@bot.message_handler(commands=["help"])
def send_commands(message):
    bot.reply_to(
        message,
        ('Comandos:\n\n' +
         '/previsao  --> Informações sobre o clima de uma cidade.\n' +
         '/covid_pais --> Informações sobre o covid-19 em um país.\n' +
         '/covid_estado --> Informações sobre o covid-19 em um ' +
         'estado brasileiro.\n' +
         '/futebol_hoje --> Jogos de futebol do dia.\n' +
         '/noticias_hoje --> Notícias em alta no dia.\n' +
         '/noticias_tema --> Notícias de um tema específico.\n' +
         '/moedas--> Cotações de Moedas.\n'))


@bot.message_handler(commands=["previsao"])
def weather(message):
    city = bot.reply_to(
        message, "Qual cidade você deseja obter informações climáticas?")
    bot.register_next_step_handler(city, get_city)


def get_city(message):
    city = message.text
    bot.reply_to(message, weather_forecast(city))


@bot.message_handler(commands=["covid_pais"])
def covid_ctr(message):
    country = bot.reply_to(
        message, "Qual país você deseja obter informações sobre o covid-19?")
    bot.register_next_step_handler(country, get_country)


def get_country(message):
    country = message.text
    bot.reply_to(message, covid_country(country))


@bot.message_handler(commands=["covid_estado"])
def covid_stt(message):
    state = bot.reply_to(
        message, "Qual estado você deseja obter informações sobre o covid-19?")
    bot.register_next_step_handler(state, get_state)


def get_state(message):
    state = message.text
    bot.reply_to(message, covid_state(state))


@bot.message_handler(commands=["futebol_hoje"])
def soccer(message):
    bot.reply_to(message, soccer_today())


@bot.message_handler(commands=["noticias_hoje"])
def news(message):
    bot.reply_to(message, news_today())


@bot.message_handler(commands=["noticias_tema"])
def news_sub(message):
    subject = bot.reply_to(message, "Qual tema você deseja procurar notícias?")
    bot.register_next_step_handler(subject, get_subject)


def get_subject(message):
    subject = message.text
    bot.reply_to(message, news_by_subject(subject))


@bot.message_handler(commands=["moedas"])
def currency_now(message):
    currency = bot.reply_to(
        message, "Qual moeda você deseja ver a cotação?\n" +
        "Digite o código conforme a lista:\n\nUSD-(Dólar Comercial)\n" +
        "USDT-(Dólar Turismo)\nCAD-(Dólar Canadense)\n" +
        "AUD-(Dólar Australiano)\nEUR-(Euro)\n" +
        "GBP-(Libra Esterlina)\nARS-(Peso Argentino)\n" +
        "JPY-(Iene Japonês)\nCHF-(Franco Suíço)\n" +
        "CNY-(Yuan Chinês)\nYLS-(Novo Shekel Israelense)\n" +
        "BTC-(Bitcoin)\nLTC-(Litecoin)\n" + "ETH-(Ethereum)\nXRP-(Ripple)\n" +
        "\nCotações atualizadas a cada 30 segundos!\n")

    bot.register_next_step_handler(currency, get_currency)


def get_currency(message):
    currency = message.text
    bot.reply_to(message, currency_today(currency))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'Comando não encontrado. Tente novamente.')


bot.polling()
