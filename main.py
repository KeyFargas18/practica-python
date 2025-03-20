# print("Hola " + input("Cual es tu nombre?") + " desde Pycharm\nprobando sonido")
# print(f'Hola {input("Cual es tu nombre? ")}! gracias por usarme.')
# print(f'Hola, tu nombre tiene {len(input("Digite su nombre porfavor: "))} caracteres')

"""username = input("Enter your name: ")
length = len(username)
print(f'Hello {username}. tu nombre tiene {length} caracteres')

glass1 = "milk"
glass2 = "juice"
jugo = glass1
glass1 = glass2
glass2 = jugo
print(glass1)
print(glass2)"""

"""print("Bienvenido al generador de nombres de bandas.")
city = input("¿Cómo se llama la ciudad donde creciste? \n")
pets_name = input("¿Cómo se llama tu mascota? \n")

print(f'El nombre de tu banda podría ser: {city} {pets_name}')"""

"""print("¡Bienvenido a la calculadora de propinas!")
bill = float(input('¿Cuál fue la factura total? '))
tip = int(input('¿Cuánta propina le gustaría dar? ¿10, 12 o 15? '))
many_people = int(input('¿Cuántas personas se dividirán la cuenta? '))

total = (bill + (bill * (tip / 100))) / many_people
print(f'Cada persona deberá pagar: {total:.2f}')"""

print('Bienvenido a la montana rusa')
height = int(input('cual es su altura en CM? '))

if height >= 120:
    edad = int(input('cual es tu edad?: '))
    bill = 0

    if edad > 18:
        if 45 <= edad <= 55:  # edad >= 45 and edad <= 55
            print("Su entrada es GRATIS")
        else:
            print("Ticket para adulto cuesta $12")
            bill = 12
    elif edad < 12:
        print("Ticket para niño cuesta $5")
        bill = 5
    else:
        print("Ticket para joven cuesta $7")
        bill = 7

    foto = int(input("Quieres una fotografia? (S o N) "))
    if foto == "S":
        print("debe pagar $3 extra")
        bill += 3

    print(f"\nEl total de su factura: ${bill}")
else:
    print('no puedes subir la altura minima es 120 CM')

"""print("Maquina para saber si un numero es par o impar")
numbers = int(input("por favor introduzca un numero: "))

if numbers % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")"""
