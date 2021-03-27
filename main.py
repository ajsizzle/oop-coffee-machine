from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while is_on:
    options = menu.get_items()
    selection = input(f"What would you like? ({options}): ").lower()
    if selection == 'off':
        is_on = False
        print("Shutting down...Goodbye.")
    elif selection == 'report':
        print("Current Resource Values:")
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(selection)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

