# https://hyperskill.org/projects/157/stages/822/implement


import requests
import json


class CurrencyConverter:
    def __init__(self):
        self.currency_have = input().lower()
        self.exchange_rate = self.get_currency_info()


    #
    # def converter(self):
    #     for currency in self.exchange_rate:
    #         converted_currency = self.conicoin * self.exchange_rate[currency]


    def get_currency_info(self):
        link = 'http://www.floatrates.com/daily/{}.json'
        currency_info = json.loads(requests.get(link.format(self.currency_have)).text)
        return currency_info

    def main(self):
        currency_to_convert = input()
        money_have = int(input())


if __name__ == '__main__':
    conicoin = CurrencyConverter()

