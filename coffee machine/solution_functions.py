import main

def check_resources(order_ingredients, current_resources):
    """Ελέγχει αν επαρκούν τα υλικά για την παραγγελία."""
    for item in order_ingredients:
        if order_ingredients[item] > current_resources[item]:
            print(f"Δεν επαρκεί το {item}.")
            return False
    return True

def process_coins():
    """Ζητάει νομίσματα από τον χρήστη και επιστρέφει το συνολικό ποσό."""
    print("Πόσα νομίσματα διαθέτεις;")
    try:
        quarters = int(input("quarters: "))
        dimes = int(input("dimes: "))
        nickles = int(input("nickles: "))
        pennies = int(input("pennies: "))
    except ValueError:
        print("Παρακαλώ εισάγετε έγκυρους αριθμούς (ακέραιους).")
        return 0
    
    amount = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return round(amount, 2)

def transaction_result(money_received, drink_cost):
    """Ελέγχει αν τα χρήματα επαρκούν και υπολογίζει τα ρέστα."""
    if money_received < drink_cost:
        print("Το χρήμα δεν επαρκεί. Επιστροφή χρημάτων.")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Τα ρέστα σου είναι {change} ευρώ.")
        return True

def make_coffee(drink_name, order_ingredients, current_resources):
    """Αφαιρεί τα υλικά από το απόθεμα και σερβίρει τον καφέ."""
    for item in order_ingredients:
        current_resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy! ☕")

def start_machine():
    # Αρχικοποίηση αποθέματος (αντίγραφο από το main.py για να μπορούμε να το αλλάζουμε)
    current_resources = {
        "water": main.resources["water"],
        "milk": main.resources["milk"],
        "coffee": main.resources["coffee"],
    }
    
    is_on = True

    while is_on:
        user_cof = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_cof == "off":
            is_on = False
        elif user_cof == "report":
            print(f"Water: {current_resources['water']}ml")
            print(f"Milk: {current_resources['milk']}ml")
            print(f"Coffee: {current_resources['coffee']}g")
        elif user_cof in main.MENU:
            drink = main.MENU[user_cof]
            if check_resources(drink["ingredients"], current_resources):
                payment = process_coins()
                if payment > 0 and transaction_result(payment, drink["cost"]):
                    make_coffee(user_cof, drink["ingredients"], current_resources)
        else:
            print("Λάθος επιλογή. Παρακαλώ διάλεξε espresso, latte ή cappuccino.")

if __name__ == "__main__":
    start_machine()