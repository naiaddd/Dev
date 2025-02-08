# weatherer
#
# COMPLETE :
#
# fetches current weather data and displays in CLI [x] 0.0.1
#
# FUTURE :
#
# fetch five day forecast [ ] 
#

import requests

version = '0.0.1'

def get_weather(cityName):

    api_key = 'b1d986349c2f063b664687621068ec8f'

    base_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(cityName, api_key)


    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather_desc = data['weather'][0]['description']

        temperature = main['temp']
        feels_like = main['feels_like']
        humidity = main['humidity']

        print('weather in {}:'.format(cityName))
        print('Temp: {}'.format(temperature))
        print('Feels like: {}'.format(feels_like))
        print('Humidity: {}%'.format(humidity))
        print('Descript: {}'.format(weather_desc))
        print('         ')
    else:
        print('City not found.')

        
def presets():
    get_weather('Brisbane')
    get_weather('Emmaville')
    get_weather('Pattaya')
    get_weather('Bangkok')
    get_weather('Moscow')

        


def main():
    print(f'Weatherer version {version}\n')
    presets()
    while True: 
        print('Input city name to check, or press q to quit.')
        reply = input('..')
        if reply == 'q':
            break
        else: get_weather(reply)


    
    

    




if __name__ == '__main__':
    main()
