import random
print("Καλωσήρθες στον tip calculator")
total_bill=float(input("Ποιο είναι το συνολικό ποσό του λογαριασμού; \n"))
pososto=int(input("Ποσοστό φιλοδωρήματος\n"))
atoma=int(input("Για πόσα άτομα είναι ο λογαριασμός; \n"))
tip=round(float((total_bill+total_bill*pososto/100)/atoma),2)
print(f"Το ποσό που πρέπει να πληρώσει το κάθε άτομο είναι: {tip}")
if tip>25:
    print("Πολύ γενναιόδωρο φιλοδώρημα!")
else:
    print("Ευχαριστούμε για το φιλοδώρημα!")   
print("Καλή σας μέρα!") 
rand=random.randint(1,10)
print (f"Τυχαίος αριθμός από το 1 έως το 10: {rand}")
randomnum=random.randint(1,45)
print (f"Τυχαίος αριθμός από το 1 έως το 45: {randomnum}")


