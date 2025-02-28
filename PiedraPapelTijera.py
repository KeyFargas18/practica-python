import random

"""print(random.randint(1, 20))
print(random.random())

game = random.randint(0, 1)
if game == 0:
    print("cara")
else:
    print("escudo")"""

friend = ["Vidal", "Edgard", "Maykel", "Bob", "Rita", "Keylin"]

# forma 1
print(random.choice(friend))

# forma 2
random_index = random.randint(0, 4)
print(friend[random_index])

print("Bienvenido al juego de 0-piedra 🪨, 1-papel 📃, 2-tijera ✂️")
usuario = int(input("Favor elije una de las 3 opciones pero con numeros: "))

if usuario == 0:
    print('''
           ,--.--._
    ------" _, \___)
            / _/____)
            \//(____)
    ------\     (__)
           `-----"
    ''')

elif usuario == 1:
    print('''
      .--""--.___.._
     (  <__>  )     `-.
     |`--..--'|      <|
     |       :|       /
     |       :|--""-./
     `.__  __;' o!O
         ""     
    ''')
elif usuario == 2:
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
               ,--.--._
        ------" _, \___)
                / _/____)
                \//(____)
        ------\     (__)
               `-----"
        ''')

elif machine == 1:
    print('''
          .--""--.___.._
         (  <__>  )     `-.
         |`--..--'|      <|
         |       :|       /
         |       :|--""-./
         `.__  __;' o!O
             ""     
        ''')
else:
    print('''
          _       ,/'
           (_).  ,/'
           __  ::
          (__)'  `\.
                    `\.
        ''')

if usuario == machine:
    print("Es un empate")

if usuario == 0 and machine == 2:
    print("GANASTE")

elif usuario == 2 and machine == 0:
    print("Computadora gana")

if usuario == 1 and machine == 0:
    print("GANASTE")
elif usuario == 1 and machine == 2:
    print("Computadora gana")

if usuario == 0 and machine == 2:
    print("GANASTE")

elif usuario == 0 and machine == 1:
    print("Computadora gana")
