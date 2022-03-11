#Se importan librerias a usar
import threading  #Hilos
import time  #Clock
import argparse  #Control desde Shell
import RPi.GPIO as GPIO  #Control de Pines

#Programación del boton y el pin 7  
GPIO.setmode(GPIO.BOARD)
buttonPin = 7;
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
buttonState = GPIO.input(buttonPin)


tiempo = 0.1  #Tiempo entre procesos

#Función genera una lista de x elementos.
def crearlista(arreglo):
    lista = list()
    for i in range(arreglo):
        lista.append(i)
    return lista  #Retorna la lista


#Función para recorrer la lista con 4 hilos
#Requiere 3 entradas, el número de elementos en el arreglo
#el índice de cada uno de los hilos y la lista. 
def recorrido_con_hilos(arreglo, numero, lista):
    suma = 0
    #Se divide el trabajo de los hilos en partes iguales
    for valor in range(numero * (arreglo), (numero + 1) * arreglo):
        #Se realiza la sumatoria de la lista
        suma += lista[valor]
        time.sleep(tiempo)  #Tiempo de espera


#Se recorre la lista de forma simple
def recorrido_sin_hilos(lista):
    suma2 = 0
    for valor in lista:
        suma2 += lista[valor]
        time.sleep(tiempo)


#Se establece una variable para recibir indicaciones desde el shell
#La variable tienen que ser de tipo int, es un arreglo y el default es de 20
parser = argparse.ArgumentParser(description='Número de elementos en el arreglo')
parser.add_argument('arreglo', type=int, default=20, help='Número de elementos en el arreglo')
args = parser.parse_args()

#Se crean 2 listas
lista_1 = crearlista(args.arreglo)
lista_2 = crearlista(args.arreglo)

#Se divide el valor de entrada entre 4
#para distribuir el trabajo entre los hilos
fraccion = round(int(args.arreglo/4))


#Se crea un main donde se llaman las funciones
def main():
    #Se mide el tiempo de inicio y finalización de cada función
    tiempo_i = time.time()  #Tiempo de inicio
    recorrido_sin_hilos(lista_1)  #Función
    tiempo_f = time.time()  #Tiempo Final
    #Se hace el uso de hilos
    hilos = list()
    tiempo_i2 = time.time()  #Tiempo inicial
    #Se llama la función correspondiente con cada hilo
    for cont in range (4):
        hilo = threading.Thread(target=recorrido_con_hilos, args=(fraccion, cont, lista_2))
        hilos.append(hilo)
        hilo.start()
    #Se le dan índices a los hilos
    hilos[0].join()
    hilos[1].join()
    hilos[2].join()
    hilos[3].join()
    tiempo_f2 = time.time()  #Tiempo final
    #Se imprimen los resultados
    if __name__ == '__main__':
        print('Tiempo sin hilos', tiempo_f - tiempo_i)
        print('Tiempo con hilos', tiempo_f2 - tiempo_i2)
    return 


#Se define una variable booleana
bol = True
#While permite que el programa funcione si el boton es presionado 
while bol:
    buttonState = GPIO.input(buttonPin)
    #Si el botón se presiona, se procede a realizar el programa
    if buttonState == False:
        main()
        #Se termina el programa
        bol = False
        
        
    
    