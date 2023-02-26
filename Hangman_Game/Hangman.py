import random


lives = 6
from Hangman_word import word_list
chosen_word = random.choice(word_list)
end_of_game = False

from Hangman_art import logo
print(logo)

display =[]
word_lenght = len(chosen_word)
for _ in range(word_lenght):
    display += "_"
print(display)

####################################################


while not end_of_game:
    guess =input("Enter the letter that can be present in word: ").lower()

    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    from Hangman_art import stages
    print(stages[lives])

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Hahaa What a loser!")
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("Congrats!  YOU WIN.")
    
    

    