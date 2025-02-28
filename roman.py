#Nombre: Juan Iran Lopez Mercado
#Materia: Back End 1
# Fecha: 02/27/25

import re  #Importa la librería re para expresiones regulares

def is_valid_roman(s): #Funcion que valida si un número romano es valido, aqui se usa el regex.
    valid_roman_pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return re.fullmatch(valid_roman_pattern, s) is not None

roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} #Diccionario para mapear los numeros romanos.
int_to_roman = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
    (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
    (5, "V"), (4, "IV"), (1, "I")
]

def roman_to_int(s):    #Funcion para convertir un numero romano a entero.
    if not is_valid_roman(s):
        raise ValueError("Número romano inválido")
    
    total, prev = 0, 0  
    for char in reversed(s):
        val = roman_map[char]
        if val < prev:
            total -= val
        else:
            total += val
            prev = val
    return total

def int_to_roman_func(num):   #Funcion para convertir un entero a numero romano
    result = []
    for value, symbol in int_to_roman:
        while num >= value:
            result.append(symbol)
            num -= value
    return "".join(result)

def main():     #Funcion principal
    input_value = input("Ingrese un número o un número romano: ")   #Le pide al usuario que ingrese un numero o un numsero romano.
    
    if input_value.isdigit():
        print("En romano es:", int_to_roman_func(int(input_value)))
    else:
        try:
            print("En número es:", roman_to_int(input_value))
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":  
    main()
