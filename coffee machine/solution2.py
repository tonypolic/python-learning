import main
cof_proc=True
current_water=main.resources["water"]
current_milk=main.resources["milk"]
current_coffee=main.resources["coffee"]
print (current_water,current_milk,current_coffee)


user_cof=input("What would you like? (espresso/latte/cappuccino):").lower
if user_cof=="off":
    cof_proc=False
elif user_cof=="report":
   # print(apouema tvrino)
   cof_proc=False
else:
    print()
    #έλεγχος ποσοτήτων
#έλεγχος νομισματων και πιθανόν ρέστα

#αφαιρεση ποσοτητων από αποθεμα

#ξανατρέξιμο από την αρχή
