class CoffeeMachine:
    def __init__(self, money, water, milk, coffee, disposable_cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.disposable_cups = disposable_cups

    def __str__(self):
        return f'{self.water} ml of water\n' \
               f'{self.milk} ml of milk\n' \
               f'{self.coffee} g of coffee beans\n' \
               f'{self.disposable_cups} disposable cups\n' \
               f'${self.money} of money'

    def make_espresso(self):
        self.water -= 250
        self.coffee -= 16
        self.disposable_cups -= 1
        self.money += 4

    def make_latte(self):
        self.water -= 350
        self.milk -= 75
        self.coffee -= 20
        self.disposable_cups -= 1
        self.money += 7

    def make_cappuccino(self):
        self.water -= 200
        self.milk -= 100
        self.coffee -= 12
        self.disposable_cups -= 1
        self.money += 6

    def make_coffee(self, type_of_coffee):
        match type_of_coffee:
            case '1':
                self.make_espresso()
            case '2':
                self.make_latte()
            case '3':
                self.make_cappuccino()

    def fill_machine(self):
        self.water += int(input('Write how many ml of water you want to add:\n'))
        self.milk += int(input('Write how many ml of milk you want to add:\n'))
        self.coffee += int(input('Write how many grams of coffee beans you want to add:'))
        self.disposable_cups += int(input('Write how many disposable cups you want to add:\n'))

    def give_money(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def main(self):
        print(self)
        action = input('Write action (buy, fill, take):\n')

        if action == 'buy':
            coffee_type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
            self.make_coffee(coffee_type)
        elif action == 'fill':
            self.fill_machine()
        elif action == 'take':
            self.give_money()

        print(self)


machine1 = CoffeeMachine(550, 400, 540, 120, 9)
machine1.main()
