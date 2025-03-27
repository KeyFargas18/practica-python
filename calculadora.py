"""print("Bienvenido al programa de python pizza delivery")

size = input("De que tamaño quiere la pizza? S, M o L \n")
bill = 0
if size == "S":
    print("El precio del tamaño S es de $15")
    bill = 15
elif size == "M":
    print("El precio del tamaño M es de $20")
    bill = 20
elif size == "L":
    print("El precio del tamaño L es de $25")
    bill = 25
else:
    print("Has escrito las entradas incorrectas, intentalo nuevamente")

#
pepperoni = input("Quiere agregar peperoni a su pizza? (S o N) \n")
if pepperoni == "S":
    if size == "S":
        print("El precio del extra es de $2")
        bill += 2
    else:
        print("El precio del extra es de $3")
        bill += 3

extra_cheese = input("Quiere agregar queso extra?")
if extra_cheese == "S":
    print("El precio del extra de queso es de $1 \n")
    bill += 1

print(f"Su factura final es: ${bill}")

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return '{formated_f_name} {formated_l_name}'
format_name("KEYLIN", "fargAs")"""


def is_leap_year(year):
    """Funcion para saber si un año es bisiesto, esto se llama docstrings"""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input('Ingrese el año: \n'))

if is_leap_year(year):
    print(f"El año {year} es bisiesto. ✅")
else:
    print(f"El año {year} NO es bisiesto. ❌")

from Hangman_art import calculadora_art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(calculadora_art)
    continues = True
    num1 = float(input("¿Cuál es el primer número?: "))

    while continues:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Elija una operación: ")

        if operation_symbol not in operations:
            print("❌ Opción no válida, vuelva a intentarlo.")
            continue

        num2 = float(input("¿Cuál es el siguiente número?: "))
        answer = operations[operation_symbol](num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        while True:
            choice = input(
                f'Escriba "y" para continuar calculando con {answer}, "n" para iniciar una nueva o "f" para salir: ').lower()
            if choice == "y":
                num1 = answer
                break  # Sale del loop y continúa con la calculadora
            elif choice == "n":
                continues = False
                print("\n" * 20)
                calculator()  # Reinicia la calculadora
                break  # Sale del loop
            elif choice == "f":
                print("Gracias por usar la calculadora. 👋")
                return
            else:
                print("❌ Opción no válida, ingrese 'y' o 'n'.")


calculator()
