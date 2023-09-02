from data import MENU, resources


def print_report():
    Water = str(resources["water"]) + "ml"
    Milk = str(resources["milk"]) + "ml"
    Coffee = str(resources["coffee"]) + "g"
    Money = "$" + str(resources["money"])
    print(f"Water: {Water}\nMilk: {Milk}\nCoffee: {Coffee}\nMoney: {Money}")


def total_amount_received():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


def check_resources(customer_selection):
    for products in MENU[customer_selection]["ingredients"]:
        if resources[products] < MENU[customer_selection]["ingredients"][products]:
            print(f"Sorry there is not enough {products}.")
            return False
    return True


def check_amount_entered(customer_selection):
    total_received = total_amount_received()
    if total_received < MENU[customer_selection]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = total_received - MENU[selection]["cost"]
        if change > 0:
            print(f"Here is ${round(change, 2)} dollars in change")
        resources["money"] = total_received - change
        return True


should_continue = True
while should_continue:
    selection = input("What would you like? (espresso/latte/cappuccino): ")
    if selection == "report":
        print_report()
    elif selection == "off":
        print("Coffee Machine is now turned off.")
        should_continue = False
    else:
        if check_resources(selection) and check_amount_entered(selection):
            for product in MENU[selection]["ingredients"]:
                resources[product] -= MENU[selection]["ingredients"][product]
            print(f"Here is your {selection}. Enjoy!")
