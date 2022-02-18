# Este es el algoritmop para el metodo string_work
# Chequea si un string contiene solo letras sino retorna un codigo de error

def string_work(entrada):# se crea la funcion
    if entrada.isalpha(): # se crea un condicional en el que se compara si la entrada es un caracter de la A a las Z
        entradilla = entrada.swapcase() # en caso de ser TRUE, se alternan las letras mayusculas con las minusculas
        print(entradilla) # da como resultado la entrada alternada
        return entradilla
    if entrada.isnumeric():
        print("1")
        return 1
    else: # en caso de no ser FASE
        print ("2") #imprime codigo de error unico, el 1 se imprime cunado el texto ingresado contiene numeros
        return 2 # se finaliza la funcion

# Este es el algoritmo para el metodo num_to_str
# verifica que el string entrado contenga solo numeros y de no serlo, retorna un codigo
# de error unico, en caso de ser verdadero traduce el numero a texto
from num2words import num2words #se importan las librerias a utilizar

def num_to_str(entry): #se crea la funcion
    if entry.isnumeric(): #se crea un condicional en el que se verifica si el entry es un caracter del 0 al 9
        ent=int(entry)
        if ent <= 99:
            letras_esp = num2words(ent, lang='es') #si la condicion se cumple, convierte el numero a letras
            letras_fin = letras_esp.replace(" ","_"); #la libreria divide las palabras con un espacio, entonces se cambia el espacio con el simbolo _
            print(letras_fin) #se imprime el resultado del numero en letras
            return letras_fin
        elif ent > 99:
            print("3")
            return 3
    else: #en caso de que pase un string
        if entry.isalpha():
            print ("4")#imprime codigo de error unico, el 2 se imprime cunado el texto ingresado contiene letras
            return 4 #finaliza la funcion
        else:
            print("3")
            return 3



