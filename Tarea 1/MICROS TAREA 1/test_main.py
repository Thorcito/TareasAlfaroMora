#este es el archivo para hacer la pruebas de pytest

from main import *  #se importa lo del main para no tener que definir de nuevo las funciones



entrada = str(input("Inserte mensaje con letras")) #se le solicita al usuario que inserte un string y este se le asigna a una variable
string_work(entrada) # se hace un llamado a la funcion string_work