"""student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_scores["Keylin"] = 100  # añadimos una nueva clave con su valor, o se puede modificar con una clave ya existente y el nuevo valor
# student_scores = {}  # borra todo lo que hay dentro del diccionario
print(student_scores.get("Harry"))  # accedo al valor usando su clave dentro de get, si no existe solo devuelve None
del student_scores["Keylin"]  # borra un elemento usando la clave o:
nombre = student_scores.pop("Draco")  # borra un elemento
print(nombre)

# Imprime solo las claves
for thing in student_scores:
    print(thing)

# creamos un diccionario vacio
student_grades = {}

# Devuelve todos los valores
for name, valor in student_scores.items():
    if 91 <= valor <= 100:
        student_grades[name] = "Sobresaliente"
    elif 81 <= valor <= 90:
        student_grades[name] = "Supero las expectativas"
    elif 71 <= valor <= 80:
        student_grades[name] = "Aceptable"
    else:
        student_grades[name] = "Reprobado"

print(student_grades)

# student_grades[name] = "Sobresaliente" agrega cada nombre como su clave  y su clasificación como el valor correspondiente

travel_log = {
    'France': {
        "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12,
    },
    'Germany': {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5,
    }
}

print(travel_log["Germany"]["cities_visited"][2])
nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])"""

from Hangman_art import Martillo

print(Martillo)

should_continue = True
gambling = {}

while should_continue:
    name = input("¿Cómo te llamas? \n")
    bet_money = int(input("¿Cual es tu oferta?: C$ \n"))
    gambling[name] = bet_money
    bidders = input('¿Hay otros postores? Digite "sí" o "no". \n').lower()

    if bidders == 'no':
        should_continue = False
    elif bidders == 'si':
        should_continue = True
    else:
        print('\nSu respuesta no es valida, vuelva a intentarlo')

# Encontrar el mayor postor
mayor_postor = max(gambling, key=gambling.get)
mayor_cantidad = gambling[mayor_postor]

print(f'El ganador es {mayor_postor} con una oferta de C${mayor_cantidad}')

"""gambling.get es una referencia al método .get() del diccionario gambling.
Cuando max() evalúa cada clave, usa gambling.get(clave) para obtener su valor.
max() recorre el iterable (en este caso, las claves del diccionario gambling).
Usa la función proporcionada en key= para decidir cómo comparar los elementos.
Devuelve el elemento con el valor más alto según esa función."""