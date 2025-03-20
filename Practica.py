import random
from Hangman_art import word_list

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
    =========
    ''', '''
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

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

for script in chosen_word:
    placeholder += '_'
print(placeholder)

game_over = True
correct_letters = []
lives = 6

while game_over:
    guess = input("\nAdivine una letra de la palabra oculta: ").lower()

    display = ""
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f'No forma parte de la palabra 😢 se te resta 1 vida')
        if lives == 0:
            game_over = False
            print("\n********************* AHORCADO, Perdiste 🥲*********************")

    if "_" not in display:
        game_over = False
        print("\n********************* Haz ganado, felicidades 🏆🥳!! *********************")

    print(stages[lives])
