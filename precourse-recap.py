# SET value of animal and clues
# PRINT explination of the game - Three clues to guess the animal.
# SET Guess = INPUT - Clue 1 text
# IF guess is right
    # PRINT - Congratulations got it first time!
# ELSE
    # SET Guess = INPUT - Clue 2 text
    # IF guess is right
        # PRINT - Congratulations got it second time!
    # ELSE
        # SET Guess = INPUT - Clue 3 text
        # IF guess is right
            # PRINT - Congratulations, third time lucky!
        # ELSE
            # PRINT - Unlucky, better luck next time :-(

# Set up 
animal = 'Spider'
clue1 = 'This animal has an exo-skeleton. Type your first guess: '
clue2 = 'This animal can have a venomous bite. Type your second guess: '
clue3 = 'This animal has eight legs. Type your third guess: '

print('You will be given three clues and have three chances to guess the animal')
guess = input(clue1)
if guess.strip().capitalize() == animal:
    print('Congratulations, got it first time!')
else:
    guess = input(clue2)
    if guess.strip().capitalize() == animal:
        print('Well done, your second guess is right!')
    else:
        guess = input(clue3)
        if guess.strip().capitalize() == animal:
            print('correct, third time lucky!')
        else:
            print('Unlucky, better luck next time :-(')

