from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffe_machine = CoffeeMaker()
new_menu = Menu()
money_machine = MoneyMachine()
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_machine.report()
        money_machine.report()
    else:
        menu_item = new_menu.find_drink(choice)
        if coffe_machine.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
                coffe_machine.make_coffee(menu_item)
