# def life_in_weeks(age):
#     weeks = (90 - age) * 52
#
#     print(f'te quedan {weeks} semanas')
#
#
# life_in_weeks(22)

"""def calculate_love_score(name1, name2):
    # total_T = total_R = total_U = total_tE = 0
    # total_L = total_O = total_V = total_E = 0
    #
    # for char in name2.lower():
    #     if char == "t":
    #         total_T += 1
    #     if char == "r":
    #         total_R += 1
    #     if char == 'u':
    #         total_U += 1
    #     if char == "e":
    #         total_tE += 1
    #
    # sumTRUE = total_T + total_U + total_R + total_tE
    # print(sumTRUE)

    name1 = name1.lower()
    name2 = name2.lower()  # Convertimos todo a minúsculas
    sumTRUE = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e") + name1.count('t') + name1.count("r") + name1.count('u') + name1.count('e')
    sumLOVE = name1.count('l') + name1.count("o") + name1.count('v') + name1.count('e') + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
    print(f'{sumTRUE}{sumLOVE}')

calculate_love_score("Keylin Fargas", "Vidal Baquedano")"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def decrypt(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decodeficar":
        shift_amount *= -1
    elif encode_or_decode != "codeficar":
        print("\nOpción inválida. Intente de nuevo.")
        return None

    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[
                shifted_position]  # Busca en el abecedario la letra que está en la posición nueva y la añade al texto cifrado.
            #shifted_position %= len(alphabet)  # asegura que el indice no se salga del rango del abecedario.
        else:
            output_text += letter

    return output_text


should_continue = True

while should_continue:
    encode_or_decode = input("\nEscriba 'codeficar' para cifrar o escriba 'decodeficar' para descifrar \n").lower()
    original_text = input("Ingrese el mensaje: ").lower()
    shift_amount = int(input("Ingrese el número de desplazamiento: "))

    result = decrypt(original_text, shift_amount, encode_or_decode)
    print(f'La palabra cifrada es: {result}')

    restart = input("\nEscriba 'si' si desea continuar o 'no' para terminar: ").lower()

    if restart == 'no':
        should_continue = False
