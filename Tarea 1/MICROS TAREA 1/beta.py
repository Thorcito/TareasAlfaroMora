# Este es el algoritmo para el metodo num_to_str
# verifica que el string entrado contenga solo numeros y de no serlo, retorna un codigo
# de error unico, en caso de ser verdadero traduce el numero a texto

from num2words import num2words

entry = str(input("Ingrese un string por favor guapo"))

if entry.isnumeric():
    #letras = num2words(entry, to='ordinal')
    #print(letras)
    letras_esp = num2words(entry, lang='es')
    #print(letras_esp)
    letras_fin = letras_esp.replace(" ","_");
    print(letras_fin)



else:
    print ("1")