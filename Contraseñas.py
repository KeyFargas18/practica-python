import random

#Regresa el numero mayor de la lista
"""list = [81, 39, 54, 11, 45, 2, 15, 30, 50, 25, 36, 22]
mayor = 0
for a in list:
    if a > mayor:
       mayor = a
print(mayor)"""

#devuelve la suma del 1 al 100
"""number = 0
for a in range(1, 101):
    number += a
print(number)"""

#Si un número es divisible por 3 y 5, imprime "FizzBuzz".
#Si es divisible solo por 3, imprime "Fizz".
#Si es divisible solo por 5, imprime "Buzz".
#Si no es divisible por ninguno, imprime el número normal.
"""for a in range (1, 101):
    if a %3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    elif a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    else:
        print(a)"""

#Generadora de contraseñas
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

print("Bienvenido al generador de contraseñas!")
nr_letters = int(input("Digite de cuantos caracteres desea su contraseña:\n"))
nr_simbols = int(input("Ingrese el numero de caracteres especiales que desea añadir:\n"))
nr_numbers = int(input("Cuantos numeros le gustaria tener?\n"))

#version facil
"""password = ""

for a in range(0, nr_letters):
    password += random.choice(letters)

for a in range(0, nr_numbers):
    password += random.choice(numbers)

for a in range(0, nr_simbols):
    password += random.choice(special_characters)

print(password)"""

#version mas complicada
password_list = []

for a in range(0, nr_letters):
    password_list.append(random.choice(letters)) #añadimos al final de la lista lo que nos a generado

for a in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for a in range(0, nr_simbols):
    password_list.append(random.choice(special_characters))

random.shuffle(password_list) #pone los caracteres de la lista en orden aleatorio
print(password_list)

password = ""
for char in password_list:
    password += char

print(f'Su nueva password es: {password}')
