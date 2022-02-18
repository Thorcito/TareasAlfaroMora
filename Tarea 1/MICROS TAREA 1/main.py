# Programacion realizada por Nadir Alfaro y Randy Mora
# Los codigos de error utilizados son los siguientes
# 1 = Error unico cuando el paramentro ingresado contiene numeros
# 2 = Error unico cuando el paramentro ingresado contiene numeros y simbolos
# 3 = Error unico cuando el parametro ingresado contiene un numero mayor a 99, decimal o negativo
# 4 = Error unico cuadno el paramentro ingresado es un string


# Es importante instalar la libreria num2words que la funcion
# num_to_str funcione adecuadamente
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
        if ent <= 99:  # en caso de ser menor a 99
            # si la condicion se cumple, convierte el numero a letras
            letras_esp = num2words(ent, lang='es')
            # la libreria divide las palabras con un espacio
            # se cambia el espacio con el simbolo _
            letras_fin = letras_esp.replace(" ", "_")
            print(letras_fin)  # se imprime el resultado del numero en letras
            return letras_fin  # retorna el resultado
        elif ent > 99:  # en caso de ser mayor a 99
            print("3")  # imprime error unico 3
            return 3  # retorna error: 3
    else:  # en caso de que pase un string
        if entry.isalpha():  # verifica si es alfanumerico
            print("4")  # imprime codigo de error unico 4
            return 4  # finaliza la funcion
        else:  # caso contrario
            print("3")  # imprime codigo de error unico 3
            return 3  # reotrna error:3
