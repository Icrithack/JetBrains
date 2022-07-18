# https://hyperskill.org/projects/157/stages/821/implement

import requests
import json

# link = 'http://www.floatrates.com/daily/{}.json'
# currency = input().lower()
# currency_info = json.loads(requests.get(link.format(currency)).text)
#
# print(currency_info['usd']['rate'], currency_info['eur']['rate'], sep='\n')


def get_currency(currency):
    link = 'http://www.floatrates.com/daily/{}.json'
    currency_info = json.loads(requests.get(link.format(currency)).text)
    return currency_info


print(get_currency(input().lower()))