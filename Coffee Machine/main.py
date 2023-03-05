MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def report():
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: ${resources["money"]}')


def insert_coins():
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    return [quarters, dimes, nickles, pennies]


def calculate_amount(coins):
    amount = 0.25 * coins[0] + 0.1 * coins[1] + 0.05 * coins[2] + 0.01 * coins[3]
    return round(amount, 2)


def update_resources(element):
    if choice == "espresso":
        resources["water"] -= MENU[element]["ingredients"]["water"]
        resources["coffee"] -= MENU[element]["ingredients"]["coffee"]
        resources["money"] += MENU[element]["cost"]
    elif choice == "latte":
        resources["water"] -= MENU[element]["ingredients"]["water"]
        resources["coffee"] -= MENU[element]["ingredients"]["coffee"]
        resources["milk"] -= MENU[element]["ingredients"]["milk"]
        resources["money"] += MENU[element]["cost"]
    else:
        resources["water"] -= MENU[element]["ingredients"]["water"]
        resources["coffee"] -= MENU[element]["ingredients"]["coffee"]
        resources["milk"] -= MENU[element]["ingredients"]["milk"]
        resources["money"] += MENU[element]["cost"]


def check_quantity(user_choice):
    is_missing = ""
    if not (resources["water"] >= MENU[user_choice]["ingredients"]["water"]):
        is_missing = "water"
    elif not (resources["milk"] >= MENU[user_choice]["ingredients"]["milk"]):
        is_missing = "milk"
    elif not (resources["coffee"] >= MENU[user_choice]["ingredients"]["coffee"]):
        is_missing = "coffee"
    return is_missing


choice = input("What would you like? (espresso/latte/cappuccino): ")
while choice != "off":
    if choice == "report":
        report()
    else:
        availability = check_quantity(choice)
        if  availability != "":
            print(f"Sorry there is not enough {availability}.")
        else:
            coins_inserted = insert_coins()
            check_amount = calculate_amount(coins_inserted)
            if check_amount >= MENU[choice]["cost"]:
                update_resources(choice)
                rest = check_amount - MENU[choice]["cost"]
                print(f"Here is ${round(rest, 2)} in change.")
                print(f"Here is your {choice} ☕️.Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
    choice = input("What would you like? (espresso/latte/cappuccino): ")
