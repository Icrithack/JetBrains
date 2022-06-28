# https://hyperskill.org/projects/78/stages/432/implement

from random import choice


class Game:
    options_list = ('rock', 'paper', 'scissors')
    lose_condition = {'scissors': 'rock', 'rock': 'paper', 'paper': 'scissors'}

    def __init__(self):
        self.computer_chose = choice(self.options_list)
        self.player_chose = input()

    def get_result(self):
        if self.player_chose == self.computer_chose:
            print(f'There is a draw ({self.computer_chose})')
        elif self.lose_condition[self.player_chose] == self.computer_chose:
            print(f'Sorry, but the computer chose {self.computer_chose}')
        else:
            print(f'Well done. The computer chose {self.computer_chose} and failed')


if __name__ == "__main__":
    Game().get_result()
