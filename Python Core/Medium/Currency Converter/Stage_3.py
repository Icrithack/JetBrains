#  https://hyperskill.org/projects/157/stages/819/implement

class CurrencyConverter:
    def __init__(self):
        self.conicoin = input('Please, enter the number of conicoins you have: ')
        self.exchange_rate = input('Please, enter the exchange rate: ')

    def parse(self, str):
        try:
            return int(str)
        except ValueError:
            return float(str)

    def convert_info(self):
        first_parse = self.parse(self.conicoin)
        second_parse = self.parse(self.exchange_rate)
        print(f'The total amount of dollars: {first_parse * second_parse}')


if __name__ == '__main__':
    conicoin = CurrencyConverter()
    conicoin.convert_info()
