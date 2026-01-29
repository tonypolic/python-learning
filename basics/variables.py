def life_in_weeks(age):
    weeks=(90-age)*12*4.5
    print(weeks)
    print(f'You have {weeks} weeks left.')
    
age=int(input('Δώσε την ηλικία σου'))
life_in_weeks(age)