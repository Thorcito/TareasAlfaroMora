# Este es el algoritmop para el metodo string_work
# Chequea si un string contiene solo letras sino retorna un codigo de error

def string_work(entrada):# se crea la funcion
    if entrada.isalpha(): # se crea un condicional en el que se compara si la entrada es un caracter de la A a las Z
        entradilla = entrada.swapcase() # en caso de ser TRUE, se alternan las letras mayusculas con las minusculas
        print(entradilla) # da como resultado la entrada alternada
    else: # en caso de no ser FASE
        print ("1") #imprime codigo de error unico, el 1 se imprime cunado el texto ingresado contiene numeros
        return # se finaliza la funcion

# Este es el algoritmo para el metodo num_to_str
# verifica que el string entrado contenga solo numeros y de no serlo, retorna un codigo
# de error unico, en caso de ser verdadero traduce el numero a texto
from num2words import num2words #se importan las librerias a utilizar

def num_to_string(entry): #se crea la funcion
    if entry.isnumeric(): #se crea un condicional en el que se verifica si el entry es un caracter del 0 al 9
        letras_esp = num2words(entry, lang='es') #si la condicion se cumple, convierte el numero a letras
        letras_fin = letras_esp.replace(" ","_"); #la libreria divide las palabras con un espacio, entonces se cambia el espacio con el simbolo _
        print(letras_fin) #se imprime el resultado del numero en letras
    else: #en caso de que la condicion se false
        print ("2")#imprime codigo de error unico, el 2 se imprime cunado el texto ingresado contiene letras
        return #finaliza la funcion


entry = str(input("Inserte mensaje con numeros")) #se le solicita al usuario que inserte in string y este se le asigne a una variable
num_to_string(entry) #se hace un llamado a la funcion num_to_string
entrada = str(input("Inserte mensaje con letras")) #se le solicita al usuario que inserte un string y este se le asigna a una variable
string_work(entrada) # se hace un llamado a la funcion string_work

