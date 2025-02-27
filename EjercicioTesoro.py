print("🏝️ ¡Bienvenido a la isla del tesoro! 🏝️")
print("Tu misión es encontrar el tesoro escondido.")

# Primera decisión
print("\nEstás en la playa. Frente a ti hay un sendero en la jungla y otro por la costa.")
decision1 = input("¿A dónde quieres ir? Escribe 'jungla' o 'costa': ").lower()

if decision1 == "jungla":
    print("\n🌿 Caminas por la jungla densa y escuchas ruidos extraños...")
    print("Después de un rato, llegas a un río caudaloso.")
    decision2 = input("¿Quieres 'nadar' o 'construir una balsa'?: ").lower()

    if decision2 == "nadar":
        print("\n🌊 El agua es muy fuerte y te arrastra. ¡Has sido llevado lejos de la isla! 😢")
        print("FIN DEL JUEGO.")

    elif decision2 == "construir una balsa":
        print(
            "\n🛶 Construyes una balsa y cruzas con éxito el río. Del otro lado hay una cueva misteriosa y un sendero.")
        decision3 = input("¿Quieres entrar en la 'cueva' o seguir el 'sendero'?: ").lower()

        if decision3 == "cueva":
            print("\n🏆 ¡Encontraste el tesoro dentro de la cueva! ¡Eres rico! 🎉")
            print("FIN DEL JUEGO. ¡Felicidades! 🏆")
            print('''
            *******************************************************************************
                      |                   |                  |                     |
             _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                      |                `"=._o`"=._      _`"=._                     |
             _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
             _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
            |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/[TomekK]
            *******************************************************************************
            ''')
        else:
            print("\n🐍 Sigues el sendero y eres atacado por una serpiente venenosa. ¡Oh no! 😱")
            print("FIN DEL JUEGO.")
    else:
        print("\nNo entendí tu elección. ¡Fin del juego! 😵")

elif decision1 == "costa":
    print("\n🌊 Caminas por la orilla, pero empieza a subir la marea y te quedas atrapado. 😨")
    print("FIN DEL JUEGO.")

else:
    print("\nNo elegiste una opción válida y te quedaste parado. Un grupo de piratas te captura. ☠️")
    print("FIN DEL JUEGO.")
