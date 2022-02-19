# Programacion realizada por Nadir Alfaro y Randy Mora
# Los codigos de error utilizados son los siguientes
# 1 = Error unico cuando el paramentro ingresado contiene numeros
# 2 = Error unico cuando el paramentro ingresado contiene numeros y simbolos
# 3 = Error unico  numero mayor a 99, decimal o negativo
# 4 = Error unico cuadno el paramentro ingresado es un string


# este es el archivo para hacer la pruebas de pytest

# se importa lo del main para no tener que definir de nuevo las funciones
from main import string_work
from main import num_to_str


def test_cambio_letras():  # prueba si alterna las letras
    x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert string_work(
        x) == "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def test_entrada_numero():  # prueba si al introducir un numero retorna error 1
    x = "21"
    assert string_work(x) == 1


# prueba si al introducir un string con num y letras retorna error 2
def test_entrada_letrasynumeros():
    x = "ASjsd21"
    assert string_work(x) == 2


def test_0_a_99():
    # Se genera un diccionario que almacena los numeros con su valor en texto
    numerosdict = {
        "0": "cero",
        "1": "uno",
        "2": "dos",
        "3": "tres",
        "4": "cuatro",
        "5": "cinco",
        "6": "seis",
        "7": "siete",
        "8": "ocho",
        "9": "nueve",
        "10": "diez",
        "11": "once",
        "12": "doce",
        "13": "trece",
        "14": "catorce",
        "15": "quince",
        "16": "dieciseis",
        "17": "diecisiete",
        "18": "dieciocho",
        "19": "diecinueve",
        "20": "veinte",
        "21": "veintiuno",
        "22": "veintidós",
        "23": "veintitrés",
        "24": "veinticuatro",
        "25": "veinticinco",
        "26": "veintiséis",
        "27": "veintisiete",
        "28": "veintiocho",
        "29": "veintinueve",
        "30": "treinta",
        "31": "treinta_y_uno",
        "32": "treinta_y_dos",
        "33": "treinta_y_tres",
        "34": "treinta_y_cuatro",
        "35": "treinta_y_cinco",
        "36": "treinta_y_seis",
        "37": "treinta_y_siete",
        "38": "treinta_y_ocho",
        "39": "treinta_y_nueve",
        "40": "cuarenta",
        "41": "cuarenta_y_uno",
        "42": "cuarenta_y_dos",
        "43": "cuarenta_y_tres",
        "44": "cuarenta_y_cuatro",
        "45": "cuarenta_y_cinco",
        "46": "cuarenta_y_seis",
        "47": "cuarenta_y_siete",
        "48": "cuarenta_y_ocho",
        "49": "cuarenta_y_nueve",
        "50": "cincuenta",
        "51": "cincuenta_y_uno",
        "52": "cincuenta_y_dos",
        "53": "cincuenta_y_tres",
        "54": "cincuenta_y_cuatro",
        "55": "cincuenta_y_cinco",
        "56": "cincuenta_y_seis",
        "57": "cincuenta_y_siete",
        "58": "cincuenta_y_ocho",
        "59": "cincuenta_y_nueve",
        "60": "sesenta",
        "61": "sesenta_y_uno",
        "62": "sesenta_y_dos",
        "63": "sesenta_y_tres",
        "64": "sesenta_y_cuatro",
        "65": "sesenta_y_cinco",
        "66": "sesenta_y_seis",
        "67": "sesenta_y_siete",
        "68": "sesenta_y_ocho",
        "69": "sesenta_y_nueve",
        "70": "setenta",
        "71": "setenta_y_uno",
        "72": "setenta_y_dos",
        "73": "setenta_y_tres",
        "74": "setenta_y_cuatro",
        "75": "setenta_y_cinco",
        "76": "setenta_y_seis",
        "77": "setenta_y_siete",
        "78": "setenta_y_ocho",
        "79": "setenta_y_nueve",
        "80": "ochenta",
        "81": "ochenta_y_uno",
        "82": "ochenta_y_dos",
        "83": "ochenta_y_tres",
        "84": "ochenta_y_cuatro",
        "85": "ochenta_y_cinco",
        "86": "ochenta_y_seis",
        "87": "ochenta_y_siete",
        "88": "ochenta_y_ocho",
        "89": "ochenta_y_nueve",
        "90": "noventa",
        "91": "noventa_y_uno",
        "92": "noventa_y_dos",
        "93": "noventa_y_tres",
        "94": "noventa_y_cuatro",
        "95": "noventa_y_cinco",
        "96": "noventa_y_seis",
        "97": "noventa_y_siete",
        "98": "noventa_y_ocho",
        "99": "noventa_y_nueve"
    }
    for x in range(0, 99):  # Se genera un cicloc for para que vaya de 1 en 1
        assert num_to_str(str(x)) == numerosdict[str(x)]


def test_string():  # prueba si al introducir un string reotrna error 4
    x = "AlfaroMora"
    assert num_to_str(x) == 4


# prueba si al introducir un numero negativo, decimal o <99 retorna error 3
def test_neg_dec_may():
    x = "-20"
    y = "123"
    z = "3.2"
    assert num_to_str(x) == 3
    assert num_to_str(y) == 3
    assert num_to_str(z) == 3
