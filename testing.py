import os
import random
from datetime import date
a=0
   
a=random.randint(0,100)
print(a)
today = date.today().isoformat()
print("Today's date:", today)
print("OS Name:", os.name)
f=open("test.txt","r")
print(f.read())
f.close()
os.remove("test.txt")   


