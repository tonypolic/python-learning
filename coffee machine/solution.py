import main
#αποθεμα σε καφετιέρα
current_water=main.resources["water"]
current_milk=main.resources["milk"]
current_coffee=main.resources["coffee"]

# έλεγχος εάν υπάρχουν διαθέσιμα υλικά
for item in main.MENU[user_coffee]["ingredients"]:
    if main.MENU[user_coffee]["ingredients"][item] > main.resources[item]:
        print(f'den eparkei to {main.MENU[user_coffee]["ingredients"][item]}')
        coffee_proc=False

# εισαγωγή νομισμάτων, έλεγχος εαν το ποσό επαρκεί
print("Πόσα νομίσματα διαθέτεις;")
quarters=int(input("quarters: "))
dimes=int(input("dimes: "))
nickles=int(input("nickles: "))
pennies=int(input("pennies: "))
amount=quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
print(round(amount,2))
if amount<main.MENU[user_coffee]["cost"]:
    print ("το χρήμα δεν επαρκεί")
    coffee_proc=False
else:
    change=round(amount-main.MENU[user_coffee]["cost"],2)
    print(f"το ρέστα σου είναι {change} ευρώ")

#αφαιρεση υλικών από το μηχάνημα
def current_ressources():
    current_water=current_water-main.MENU[user_coffee]["ingredients"]["water"]
    current_milk=current_milk-main.MENU[user_coffee]["ingredients"]["milk"]
    current_coffee=current_coffee-main.MENU[user_coffee]["ingredients"]["coffee"]

user_coffee=input("What would you like? (espresso/latte/cappuccino):").lower()
coffeeid, coffee_proc=select_coffee(user_coffee)
print(coffeeid,coffee_proc)

print(main.resources["water"])
print(f"water={main.MENU[user_coffee]["ingredients"]["water"]}")
print(f"milk={main.MENU[user_coffee]["ingredients"]["milk"]}")
print(f"coffee={main.MENU[user_coffee]["ingredients"]["coffee"]}")

print(main.MENU[user_coffee]["cost"])

    

