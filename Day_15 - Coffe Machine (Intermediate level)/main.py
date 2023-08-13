MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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


def prompt():
    """ Print the report(i.e. inventory - the current resource values)"""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')


def check_resources(drink):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] - MENU[drink]["ingredients"][ingredient] < 0:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        return True


def transaction_successful(drink, amount):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if amount - MENU[drink]["cost"] < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True


def update_resources(drink, all_resources):
    """Deduct the required ingredients from the resources and Return rhe updated resources"""
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    return all_resources


run_machine = True

while run_machine:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        run_machine = False
    elif choice == "prompt":
        prompt()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        resources_available = check_resources(choice)
        if resources_available:
            # Process coins
            print("Please insert coins.")
            quarters_amount = int(input("How many quarters?: "))
            dimes_amount = int(input("How many dimes?: "))
            nickles_amount = int(input("How many nickles?: "))
            pennies_amount = int(input("How many pennies?: "))
            total_amount = quarters_amount * 0.25 + dimes_amount * 0.10 + nickles_amount * 0.05 + pennies_amount * 0.01
            if total_amount > 100:
                total_amount /= 100
            # Check that there is sufficient payment and return change if there is excess payment
            if transaction_successful(choice, total_amount):
                resources["money"] += MENU[choice]["cost"]
                if total_amount > MENU[choice]["cost"]:
                    change = round(total_amount - MENU[choice]["cost"], 2)
                    print(f"Here is ${change} dollars in change.”")
                # Update the inventory (resources)
                resources = update_resources(choice, resources)
                print(f"Here is your {choice} ☕️. Enjoy!”")