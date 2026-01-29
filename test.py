def calculate_love_score(name1,name2):
    ttrue=0
    tlove=0
    name1=name1.lower()
    name2=name2.lower()
 
    
    for letter in name1:
        if letter=="t" or letter=='r' or letter=='u' or letter=='e':
           ttrue=ttrue+1
        if letter=='l' or letter =='o' or letter=='v' or letter=='e':
            tlove=tlove+1
    for letter in name2:
        if letter=="t" or letter=='r' or letter=='u' or letter=='e':
           ttrue=ttrue+1
        if letter=='l' or letter =='o' or letter=='v' or letter=='e':
            tlove=tlove+1     
    print(f'Love score {str(ttrue)+str(tlove)}')
    

calculate_love_score (name1 = "Angela Yu", name2 = "Jack Bauer")