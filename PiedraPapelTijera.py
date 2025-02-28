import random

"""print(random.randint(1, 20))
print(random.random())

game = random.randint(0, 1)
if game == 0:
    print("cara")
else:
    print("escudo")"""

friend = ["Vidal", "Kevin", "Maykel", "Bob", "Rita", "Keylin"]

# forma 1
print(random.choice(friend))

# forma 2
random_index = random.randint(0, 4)
print(friend[random_index])

print("Bienvenido al juego de piedra 🪨, papel 📃 o tijera ✂️")
usuario = input("Favor elije una de las 3 opciones: ").lower()

if usuario == "piedra":
    print('''
           ,--.--._
    ------" _, \___)
            / _/____)
            \//(____)
    ------\     (__)
           `-----"
    ''')

elif usuario == "papel":
    print('''
      .--""--.___.._
     (  <__>  )     `-.
     |`--..--'|      <|
     |       :|       /
     |       :|--""-./
     `.__  __;' o!O
         ""     
    ''')
elif usuario == "tijera":
    print('''
      _       ,/'
       (_).  ,/'
       __  ::
      (__)'  `\.
                `\.
    ''')
else:
    print("No entendi esa opcion, favor vuelve a intentarlo")

print("la computadora eligio: ")
machine = random.randint(0, 2)

if machine == 0:
    print('''
          _       ,/'
           (_).  ,/'
           __  ::
          (__)'  `\.
                    `\.
        ''')

elif machine == 1:
    print('''
               ,--.--._
        ------" _, \___)
                / _/____)
                \//(____)
        ------\     (__)
               `-----"
        ''')
else:
    print('''
          .--""--.___.._
         (  <__>  )     `-.
         |`--..--'|      <|
         |       :|       /
         |       :|--""-./
         `.__  __;' o!O
             ""     
        ''')

if usuario == "tijera" and machine == 0:
    print("Es un empate")

elif usuario == "papel" and machine == 2:
    print("Es un empate")

elif usuario == "piedra" and machine == 1:
    print("Es un empate")

if usuario == "tijera" and machine == 2:
    print("GANASTE")

elif usuario == "tijera" and machine == 1:
    print("Computadora gana")

if usuario == "papel" and machine == 1:
    print("GANASTE")
elif usuario == "papel" and machine == 0:
    print("Computadora gana")

if usuario == "piedra" and machine == 0:
    print("GANASTE")

elif usuario == "piedra" and machine == 2:
    print("Computadora gana")
