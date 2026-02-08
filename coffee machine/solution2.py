import main
cof_proc=True
current_water=main.resources["water"]
current_milk=main.resources["milk"]
current_coffee=main.resources["coffee"]

while cof_proc==True:
    user_cof=input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_cof=="off":
        cof_proc=False
        continue
    elif user_cof=="report":
        print(f"Water: {current_water}ml")
        print(f"Milk: {current_milk}ml")
        print(f"Coffee: {current_coffee}g")
        continue
    elif user_cof not in main.MENU:
        print("Λάθος επιλογή. Παρακαλώ διάλεξε espresso, latte ή cappuccino.")
        continue
    else:
        if main.MENU[user_cof]["ingredients"]["water"] > current_water:
            print(f'den eparkei to water')
            continue
        elif main.MENU[user_cof]["ingredients"]["milk"] > current_milk:
            print(f'den eparkei to milk')
            continue
        elif main.MENU[user_cof]["ingredients"]["coffee"] > current_coffee:
            print(f'den eparkei to coffee')
            continue

    #έλεγχος νομισματων και πιθανόν ρέστα
    print("Πόσα νομίσματα διαθέτεις;")
    try:
        quarters=int(input("quarters: "))   
        dimes=int(input("dimes: "))
        nickles=int(input("nickles: "))
        pennies=int(input("pennies: "))
    except ValueError:
        print("Παρακαλώ εισάγετε έγκυρους αριθμούς (ακέραιους).")
        continue
    amount=quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
    print(round(amount,2))
    if amount<main.MENU[user_cof]["cost"]:
        print ("το χρήμα δεν επαρκεί")
    else:
        change=round(amount-main.MENU[user_cof]["cost"],2)
        print(f"το ρέστα σου είναι {change} ευρώ")  
        print(f"Here is your {user_cof}. Enjoy!")

        #αφαιρεση ποσοτητων από αποθεμα
        current_water-=main.MENU[user_cof]["ingredients"]["water"]
        current_milk-=main.MENU[user_cof]["ingredients"]["milk"]
        current_coffee-=main.MENU[user_cof]["ingredients"]["coffee"]    
        # print(current_water,current_milk,current_coffee)
