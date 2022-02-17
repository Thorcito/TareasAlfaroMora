# Este es el algoritmop para el metodo string_work
# Chequea si un string contiene solo letras sino retorna un codigo de error

entrada = str(input("Inserte un string toy chiquito")) #se le solicita al usurio que inserte un string y este se le asigna a una variable

if entrada.isalpha(): # se crea un condicional en el que se compara si la entrada es un caracter de la A a las Z
    entradilla = entrada.swapcase() # en caso de ser TRUE, se alternan las letras mayusculas con las minusculas
    print(entradilla) # da como resultado la entrada alternada
else: # en caso de no ser FLASE
    print ("1") #imprime codigo de error unico


