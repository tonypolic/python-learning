import main


class CoffeeMachine:
    def __init__(self, menu, resources):
        self.menu = menu
        self.resources = {
            "water": resources["water"],
            "milk": resources["milk"],
            "coffee": resources["coffee"],
        }
        self.is_on = True

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink_name):
        drink = self.menu[drink_name]
        for item, amount_needed in drink["ingredients"].items():
            if amount_needed > self.resources[item]:
                print(f"Δεν επαρκεί το {item}.")
                return False
        return True

    def process_coins(self):
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

    def make_payment(self, money_received, drink_cost):
        if money_received < drink_cost:
            print("Το χρήμα δεν επαρκεί. Επιστροφή χρημάτων.")
            return False
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Τα ρέστα σου είναι {change} ευρώ.")
        return True

    def make_coffee(self, drink_name):
        drink = self.menu[drink_name]
        for item, amount in drink["ingredients"].items():
            self.resources[item] -= amount
        print(f"Here is your {drink_name}. Enjoy!")

    def run(self):
        while self.is_on:
            user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

            if user_choice == "off":
                self.is_on = False
            elif user_choice == "report":
                self.report()
            elif user_choice in self.menu:
                if self.is_resource_sufficient(user_choice):
                    payment = self.process_coins()
                    if payment > 0 and self.make_payment(payment, self.menu[user_choice]["cost"]):
                        self.make_coffee(user_choice)
            else:
                print("Λάθος επιλογή. Παρακαλώ διάλεξε espresso, latte ή cappuccino.")


if __name__ == "__main__":
    machine = CoffeeMachine(main.MENU, main.resources)
    machine.run()
