from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    choice = input(f"What would you like? ({menu.get_items()}) ").lower()
    menu_item = menu.find_drink(choice)
    if choice == "off":
        machine_on = False
    elif choice == "prompt":
        coffee_maker.report()
        money_machine.report()
    elif choice == "latte" or choice == "cappuccino" or choice == "espresso":
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)