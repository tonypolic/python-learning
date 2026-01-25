word_list = ['larry', 'curly', 'moe']
import random
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
given_letter=input('Δώσε ένα γράμμα\n')
for i in range(word_length):
    if given_letter==chosen_word[i]:
        print('right', end=' ') 
    else:
        print ('wrong', end=' ')
print()
print(chosen_word)




