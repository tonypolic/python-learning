import random
player_number=0
epityxia=False
hynumber=random.randint(1,100)

def guess_number(player_number):    
    if player_number>hynumber:
        print("too high") 
        return False   
    elif player_number<hynumber:
        print("too low")
        return False
    else:
        print("ok")
        return True
        

while epityxia==False:
    player_number=int(input("dose arithmo\n"))
    epityxia=guess_number(player_number)

    
    
