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

# def test_0_a_99():
    # x=0
    # while x<100:
    # y=x;
    # x=x+1;
    # assert num_to_str(y)==letras_fin


def test_0_a_99():  # prueba que traduzca el numero a letras
    x = "68"
    assert num_to_str(x) == "sesenta_y_ocho"


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
