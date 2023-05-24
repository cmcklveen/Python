#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']




# Step 1

end_of_game = False
word_list =["ardvark", "baboon", "camel", "goat", "monkey"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# TODO 1. Randomly choose a word from word list and assignt it to a variable called chosen_word

lives = 6

# Create blanks

display =[]

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter? \n").lower()

# TODO 2. Ask the user to guess a letter and assign it to a variable call guess.
    # Check for guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # Print
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!: ")


# TODO 3. Check if letter guessed matches any letter in chosen word.
    print(f"{' '.join(display)}")



    if "_" not in display:
        end_of_game = True
        print("You win!")

print(stages[lives])