# https://hyperskill.org/projects/78/stages/434/implement

from random import choice


class Game:
    options_list = ('rock', 'paper', 'scissors')
    lose_condition = {'scissors': 'rock', 'rock': 'paper', 'paper': 'scissors'}

    def __init__(self):
        self.computer_chose = None
        self.player_chose = None
        self.player_name = input('Enter your name: ')
        self.rating = self.get_rating()

        print(f'Hello, {self.player_name}')

    def find_winner(self):
        if self.player_chose == self.computer_chose:
            print(f'There is a draw ({self.computer_chose})')
            self.rating += 50
        elif self.lose_condition[self.player_chose] == self.computer_chose:
            print(f'Sorry, but the computer chose {self.computer_chose}')
        else:
            print(f'Well done. The computer chose {self.computer_chose} and failed')
            self.rating += 100

    def get_rating(self):
        with open('rating.txt', 'r') as rating:
            rating_list = [i.split() for i in rating.readlines()]
            rating_dict = {key: int(value) for (key, value) in rating_list}

        if self.player_name in rating_dict:
            return rating_dict[self.player_name]
        else:
            return 0

    def main(self):
        while True:
            self.player_chose = input()
            self.computer_chose = choice(self.options_list)

            if self.player_chose == '!exit':
                print('Bye!')
                break

            if self.player_chose == '!rating':
                print(f'Your rating: {self.rating}')
                continue

            if self.player_chose in self.options_list:
                self.find_winner()
            else:
                print('Invalid input')


if __name__ == "__main__":
    Game().main()
