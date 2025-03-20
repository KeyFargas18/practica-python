import random
# import Hangman_art
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

chosen_word = random.choice(word_list)  # selecciona una palabra al azar de la lista.

placeholder = "La palabra es un nombre de animal 🦉🦁🐧🦅🐋🐢, adivina cual sera: "  # variable que almacena los - segun el tamaño de la palabra
word_length = len(chosen_word)  # nos dice cuántas letras tiene la palabra.

for position in range(word_length):  # bucle para que se coloque un _ representando las letras ocultas.
    placeholder += "_"  # se le agrega a la variable para visualizar de cuantas letras es la palabra
print(placeholder)

game_over = True  # significa que el juego sigue en marcha.
correct_letters = []  # es una lista donde guardaremos las letras que el jugador ha adivinado correctamente.
lives = 6

while game_over:  # bucle para que no se termine hasta el usuario complete la palabra
    print(f'\n********************* Te quedan: {lives}/6 intentos *********************')
    guess = input("Adivina una letra de la palabra: ").lower()  # pide una letra al jugador.

    display = ""  # variable para almacenar lo que el usuario vaya adivinando

    for letter in chosen_word:  # bucle para que la palabra elegia se recorra letra por letra
        if letter == guess:  # Si la letra es la que el jugador adivinó
            display += letter  # agrega la letra correcta a la variable
            correct_letters.append(guess)  # Guarda la letra correcta cuando se adivina por primera vez.
        elif letter in correct_letters:  # Asegura que las letras correctas previas sigan mostrándose en display.
            display += letter
        else:  # Si la letra no ha sido adivinada aún, la reemplaza con un guion bajo _
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f'No forma parte de la palabra 😢 se te resta 1 vida')
        if lives == 0:
            game_over = False
            print("\n********************* AHORCADO, Perdiste 🥲*********************")
    else:
        print(f'Correcto!! "{guess}" es una de las letras de la palabra, sigue asi! 🧚🏻‍')

    if "_" not in display:  # Si no hay más _ en display, significa que el jugador adivinó todas las letras.
        game_over = False  # detiene el bucle
        print("\n********************* Haz ganado, felicidades 🏆🥳!! *********************")

    print(stages[lives])
