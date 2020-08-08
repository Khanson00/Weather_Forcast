# Kyle Hanson
# Feb 23, 2020

import requests
from pprint import pprint
from datetime import date
from config_api import api_key_phrase



# Function that that provides the URL and API Key
def weather_data(query):
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    api_key = api_key_phrase

    res = requests.get(url + query + ',us&units=imperial&APPID=' + api_key)

    return res.json()


def print_weathercity(result, city):
    today = date.today()

    # Exception handling for the API code
    try:
        if result['cod'] != 401:
            print('\n>>> Your Key is Valid')

        if result['cod'] == 401:
            raise ValueError
    except:

        print('\033[31m' + 'API Key is not found' + '\033[30m')

    # Prints out the returned result
    print(">>> Code: {}".format(result['cod']))


    try:
        if result['cod'] != 404:
            print('--------------------------')
            print('\033[1m' + 'Current Weather Conditions for {} \033[0m'.format(city))
            print('Current Date:', today)
            print('--------------------------')
            print('Current Temp: {}°F '.format(result['main']['temp']))
            print('Low Temp: {}°F '.format(result['main']['temp_min']))
            print('High Temp: {}°F '.format(result['main']['temp_max']))
            print('Wind speed: {} m/s'.format(result['wind']['speed']))
            print('Cloud Cover: {}'.format(result['weather'][0]['description']))
            print('Humidity: {}% '.format(result['main']['humidity']))
            print('--------------------------')

        if result['cod'] == 404:
            raise ValueError

    except:
        print('\033[31m' + '\nCity not found' + '\033[30m')


def print_weatherzip(result, zip):
    today = date.today()

    # Exception handling for the API code
    try:
        if result['cod'] != 401:
            print('\n>>> Valid API Key!')

        if result['cod'] == 401:
            raise ValueError
    except:
        print('\033[31m' + 'API Key Not Found' + '\033[30m')

    print(">>> Code: {}".format(result['cod']))

    # Validates the correct zip, then prints if correct
    try:
        if result['cod'] != 404:
            pprint('--------------------------')
            print('\033[1m' + 'Current Weather Conditions for {} \033[0m'.format(zip))
            print('Current Date:', today)
            print('--------------------------')
            print('US City Name: {}'.format(result['name']))
            print('Current Temp: {}°F '.format(result['main']['temp']))
            print('Low Temp: {}°F '.format(result['main']['temp_min']))
            print('High Temp: {}°F '.format(result['main']['temp_max']))
            print('Wind speed: {} m/s'.format(result['wind']['speed']))
            print('Cloud Cover: {}'.format(result['weather'][0]['description']))
            print('Humidity: {}% '.format(result['main']['humidity']))
            pprint('--------------------------')

        if result['cod'] == 404:
            raise ValueError

    except:
        print('\033[31m' + 'ZIP Code Not Found' + '\033[30m')


def main():
    # Prints the header
    print('\033[1m' + 'Weather Program!\n' + '\033[0m')
    print('This program requests a zip or city from the user. It then uses the OpenWeatherMap API to pull and print the info')

    print('---------------------------------------------------------------------------------------------------------------')

    user_input = input('\nWould you like to lookup the weather via city or zip. Enter 1 for City, 2 for ZIP, 3 to end: ')

    # Validates whether user_input is equal to 1, 2, or 3
    if user_input not in ('1', '2', '3'):
        print('\033[31m' + '\nAn invalid option' + '\033[30m')
        user_input = input('\nWould you like to lookup the weather via city or zip. Enter 1 for City, 2 for ZIP, 3 to end: ')

    # While loop to run the program infinitely until user selects end
    while user_input:

        # Checks user input
        if user_input not in ('1', '2', '3'):
            print('\033[31m' + '\nAn Invalid Option' + '\033[30m')
            user_input = input('\nWould you like to lookup the weather via city or zip. Enter 1 for City, 2 for ZIP, 3 to end: ')


        elif user_input == '1':
            city = input('\nEnter the city: ')
            query = 'q=' + city;
            w_data = weather_data(query);
            print_weathercity(w_data, city)

            user_input = input('\nWould you like to lookup the weather via city or zip. Enter 1 for City, 2 for ZIP, 3 to end: ')

        elif user_input == '2':
            zip = input('\nEnter the ZIP Code: ')
            query = 'zip=' + zip;
            w_data = weather_data(query);
            print_weatherzip(w_data, zip)
            user_input = input('\nWould you like to lookup the weather via city or zip. Enter 1 for City, 2 for ZIP, 3 to end: ')

        elif user_input == '3':
            print('\nEnd')
            break


# Calls the main() function
if __name__ == '__main__':
    main()
