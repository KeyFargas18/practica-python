print("Bienvenido al programa de python pizza delivery")

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

pepperoni = input("Quiere agregar peperoni a su pizza? (S o N) \n")
if pepperoni == "S":
    if size == "S":
        print("El precio del extra es de $2")
        bill += 2
    else:
        print("El precio del extra es de $3")
        bill += 3

extra_cheese = input("Desea agregar extra de queso? (S o N) \n")
if extra_cheese == "S":
    print("El precio del extra de queso es de $1 \n")
    bill += 1

print(f"Su factura final es: ${bill}")
