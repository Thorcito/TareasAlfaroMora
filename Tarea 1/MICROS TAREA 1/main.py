# Se importan librerías
from num2words import num2words

# Este es el algoritmop para el metodo string_work
# Chequea si un string contiene solo letras sino retorna un codigo de error


def string_work(entrada):  # Se crea la funcion
    # se compara si entrada es un caracter de la A a las Z
    if entrada.isalpha():
        entradilla = entrada.swapcase()  # if True, se cambian MAY por min
        print(entradilla)   # Imprime resultado
        return entradilla  # Retorna resultado
    if entrada.isnumeric():  # Verifica si es número
        print("1")  # Imprime código de error: 1
        return 1  # Retorna error:1
    else:  # En caso de ser alfanumérico
        print("2")  # Imprime error único 2
        return 2  # Retorna error:2


# Se define la función
def num_to_str(entry):
    if entry.isnumeric():  # Se verifica si el entry es un caracter del 0 al 9
        ent = int(entry)  # Define la entrada como int
        if ent <= 99:  #
            # si la condicion se cumple, convierte el numero a letras
            letras_esp = num2words(ent, lang='es')
            # la libreria divide las palabras con un espacio
            # se cambia el espacio con el simbolo _
            letras_fin = letras_esp.replace(" ", "_")
            print(letras_fin)  # se imprime el resultado del numero en letras
            return letras_fin
        elif ent > 99:
            print("3")
            return 3
    else:  # en caso de que pase un string
        if entry.isalpha():
            # imprime codigo de error unico, el 2 se imprime cunado el texto
            # ingresado contiene letras
            print("4")
            return 4  # finaliza la funcion
        else:
            print("3")
            return 3
