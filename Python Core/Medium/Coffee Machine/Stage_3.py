class CoffeeMachine:
    water_for_cup = 200
    milk_for_cup = 50
    coffee_for_cup = 15

    def __init__(self, water=0, milk=0, coffee=0):
        self.water = water
        self.milk = milk
        self.coffee = coffee

    def min_cups(self):
        water = self.water // self.water_for_cup
        milk = self.milk // self.milk_for_cup
        coffee = self.coffee // self.coffee_for_cup
        return min(water, milk, coffee)

    def make_coffee(self, cups):
        if self.min_cups() == cups:
            print('Yes, I can make that amount of coffee')
        elif self.min_cups() < cups:
            print(f'No, I can make only {self.min_cups()} cups of coffee')
        elif self.min_cups() > cups:
            print(f'Yes, I can make that amount of coffee (and even {self.min_cups()-cups} more than that)')


machine = CoffeeMachine()
machine.water = int(input('Write how many ml of water the coffee machine has:\n'))
machine.milk = int(input('Write how many ml of milk the coffee machine has:\n'))
machine.coffee = int(input('Write how many grams of coffee beans the coffee machine has:\n'))
cups_of_coffee = int(input('Write how many cups of coffee you will need:\n'))

machine.make_coffee(cups_of_coffee)
