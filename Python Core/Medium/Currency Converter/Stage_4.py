#  https://hyperskill.org/projects/157/stages/820/implement

class CurrencyConverter:
    def __init__(self):
        self.conicoin = float(input())
        self.exchange_rate = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}
        self.msg = 'I will get {} {} from the sale of {} conicoins.'

    def get_info(self):
        for currency in self.exchange_rate:
            converted_currency = self.conicoin * self.exchange_rate[currency]
            print(self.msg.format(converted_currency, currency, self.conicoin))


if __name__ == '__main__':
    conicoin = CurrencyConverter()
    conicoin.get_info()
