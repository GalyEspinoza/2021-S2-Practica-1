import Practica1;
import pytest;

    
def test_contarDigitosPares_1():
    assert Practica1.contarDigitosPares(2345) == 2

def test_contarDigitosPares_2():
    assert Practica1.contarDigitosPares(345) == 1

def test_contarDigitosPares_3():
    assert Practica1.contarDigitosPares(-135) == 0

def test_contarDigitosPares_4():
    assert Practica1.contarDigitosPares(200400600) == 9

def test_contarDigitosPares_5():
    assert Practica1.contarDigitosPares(0) == 1

def test_contarDigitosPares_6():
    assert Practica1.contarDigitosPares('2345') == 'Error: Solo es permitido número de tipo entero'

def test_contarTriosDeDigitos_1():
    assert Practica1.contarTriosDeDigitos(256145)  == 2

def test_contarTriosDeDigitos_1():
    assert Practica1.contarTriosDeDigitos(245) == 1

def test_contarTriosDeDigitos_2():
    assert Practica1.contarTriosDeDigitos(15) == 0

def test_contarTriosDeDigitos_3():
    assert Practica1.contarTriosDeDigitos('abc') == 'Error: Solo es permitido número de tipo entero'

def test_sumatoriaParcial_1():
    assert Practica1.sumatoriaParcial(1, 3) == 6

def test_sumatoriaParcial_2():
    assert Practica1.sumatoriaParcial(-2, 3) == 3

def test_sumatoriaParcial_3():
    assert Practica1.sumatoriaParcial(0, 0) == 0

def test_sumatoriaParcial_4():
    assert Practica1.sumatoriaParcial(2, 1) == 'Error: El parámetro Fin debe ser mayor o igual que Ini'

def test_sumatoriaParcial_5():
    assert Practica1.sumatoriaParcial(2, 'abc') == 'Error: Solo es permitido número de tipo entero'

def test_multiplicacion_1():
    assert Practica1.multiplicacion(1, 3) == 3

def test_multiplicacion_2():
    assert Practica1.multiplicacion(3, 1) == 3

def test_multiplicacion_3():
    assert Practica1.multiplicacion(5, 0) == 0

def test_multiplicacion_4():
    assert Practica1.multiplicacion(5, 8) == 40

def test_multiplicacion_5():
    assert Practica1.multiplicacion('5', 0) == 'Error: Solo es permitido número de tipo entero'
