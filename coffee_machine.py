class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):  # values for coffee machine's resources
        self.water = water
        self.milk = milk
        self.coffee_beans = beans
        self.cups = cups
        self.money = money


    # amounts of each ingredient needed for each type of coffee
    # [espresso, latte, cappuccino]
    water_list = [250, 350, 200]
    milk_list = [0, 75, 100]
    beans_list = [16, 20, 12]
    money_list = [4, 7, 6]

    def how_much_supplies_left(self):  # screen showing how much supplies left
        print()
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee_beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'${self.money} of money')

    def coffee_maker(self, coffee_type):  # actions needed to prepare a coffee
        self.water = self.water - CoffeeMachine.water_list[int(coffee_type) - 1]
        self.milk = self.milk - CoffeeMachine.milk_list[int(coffee_type) - 1]
        self.coffee_beans = self.coffee_beans - CoffeeMachine.beans_list[int(coffee_type) - 1]
        self.money = self.money + CoffeeMachine.money_list[int(coffee_type) - 1]
        self.cups -= 1

    def supplies_checker(self, coffee_type):  # method that checks if there are enough supplies left for selected coffee
        water_condition = self.water - CoffeeMachine.water_list[int(coffee_type) - 1] < 0
        milk_condition = self.milk - CoffeeMachine.milk_list[int(coffee_type) - 1] < 0
        beans_condition = self.coffee_beans - CoffeeMachine.beans_list[int(coffee_type) - 1] < 0
        cups_condition = self.cups - 1 < 0
        if water_condition is True or milk_condition is True or beans_condition is True or cups_condition is True:
            if water_condition is True:
                print('Sorry, not enough water!')
            if milk_condition is True:
                print('Sorry, not enough milk!')
            if beans_condition is True:
                print('Sorry, not enough coffee beans!')
            if cups_condition is True:
                print('Sorry, not enough disposable cups!')
        else:
            print('I have enough resources, making you a coffee!')
            CoffeeMachine.coffee_maker(self, coffee_type)

    def filler(self):  # method for filling the coffee machine
        print()
        print('Write how many ml of water do you want to add:')
        self.water = self.water + int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk = self.milk + int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.coffee_beans = self.coffee_beans + int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.cups = self.cups + int(input())

    def taker(self):  # mathod for taking the money
        print()
        print(f'I gave you ${self.money}')
        self.money = 0


# START OF THE PROGRAM

coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    print()
    print('Write action (buy, fill, take, remaining, exit):')
    user_input = input()
    if user_input == 'buy':
        for char in 'a':
            print()
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            chosen = input()
            if chosen == 'back':
                break
            elif chosen == '1' or chosen == '2' or chosen == '3':
                if chosen == '1':
                    coffee_machine.supplies_checker(1)
                if chosen == '2':
                    coffee_machine.supplies_checker(2)
                if chosen == '3':
                    coffee_machine.supplies_checker(3)
    elif user_input == 'fill':

        coffee_machine.filler()
    elif user_input == 'take':
        coffee_machine.taker()
    elif user_input == 'remaining':
        coffee_machine.how_much_supplies_left()
    elif user_input == 'exit':
        break
