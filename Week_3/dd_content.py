import csv
import random
from urllib import request
from json import datetime
import json
import tweepy

def get_random_quote(quotes_file='Quotes.csv'):
    try:
        with open(quotes_file) as csvfile:
            quotes=[{'author' : line[0],
                      'quotes': line[1]} for line in csv.reader(csvfile, delimeter= '|')]

    except Exception as e :
        quotes=[{'author' : 'Eric Idle',
                 'quote': 'Always look on the Bright side of life.'}]
    return random.choice(quotes)    

# etrieving the current weather forecast
def get_weather_forecast(coords={'lat':28.417,'lon':-80.5378}) :
    try:
        api_key='b77beb3caff4e64045ef5837b473c11a'
        url=f'https://openweathermap.org/forecast5'lat={coords["lat"]}&lon={coords["lon"]}&appid={api_key}
        data=json.loads(request.urlopen(url))
def get_twitter_trends(WOEID):
    pass

def get_wikipedia_article():
    pass

if __name__ == '_main_':
    # testing the code
    print('\nTesting quote generation....')

    quote= get_random_quote()
    print(f' -Random quote is "{quote["quote"]}" - {quote["author"]}')

    quote = get_random_quote(quotes_file= None)
    print(f' -Default quote is "{quote["quote"]}" -{quote["author"]}')