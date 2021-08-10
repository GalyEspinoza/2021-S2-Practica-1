# 2021-S2 Práctica 1

## Instrucciones Generales
- El archivo **debe** llamarse **Practica1.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe utilizar la programación recursiva de pila

## contarDigitosPares(num)
- Construir una función que retorne la cantidad de dígitos que compone el número de parámetro de entrada.
- El parámetro **num** debe ser entero
- El dígito **CERO** es considerado como **Par**

```python
>>>contarDigitosPares(2345)     
2

>>>contarDigitosPares(345)     
1

>>>contarDigitosPares(-135)     
0

>>>contarDigitosPares(200400600)     
9

>>>contarDigitosPares(0)     
1

>>>contarDigitosPares('2345')     
'Error: Solo es permitido número de tipo entero'
```

## contarTriosDeDigitos(num)
- Construir una función que retorne la cantidad de grupos de 3 dígitos que compone el número de parámetro de entrada.
- El parámetro **num** debe ser entero
- Por ejemplo : 
  -  num = 256145, el resultado a retornar es 2, porque hay 2 grupos de 3 dígitos,  256 y 145
  -  num = 245, el resultado a retornar es 1, porque hay 1 grupo de 3 dígitos,  solo 245
  -  num = 15, el resultado a retornar es 0, porque NO hay de 3 dígitos,  solo dos dígitos

```python
>>>contarTriosDeDigitos(256145)     
2

>>>contarTriosDeDigitos(245)     
1

>>>contarTriosDeDigitos(15)     
0

>>>contarTriosDeDigitos('abc')     
'Error: Solo es permitido número de tipo entero'
```

## sumatoriaParcial(ini, fin)
- Construir una función que retorne la sumatoria de una secuencia de números desde un número hasta uno final.
- El parámetro **ini** y **fin** deben ser enteros
- El parámtro **fin** debe ser mayor o igual que **ini**

```python
>>>sumatoriaParcial(1, 3)     
6

>>>sumatoriaParcial(-2, 3)     
3

>>>sumatoriaParcial(0, 0)     
0

>>>sumatoriaParcial(2, 1)     
'Error: El parámetro Fin debe ser mayor o igual que Ini'

>>>sumatoriaParcial(2, 'abc')     
'Error: Solo es permitido número de tipo entero'
```
## multiplicacion(op1, op2)
- Construir una función que retorne la multiplicación de dos números pero a través de la recursión.
- El parámetro **op1** y **op2** deben ser enteros e incluir el CERO
- Ambos parámetros deben ser positivos
- Recordar la regla de la multiplicación con el **CERO**
- Ejemplo: 5 x 2
  - 5 x 2 sería sumar dos veces 5, es decir 5 + 5
  - 4 x 3 sería sumar tres veces 4, es decir 4 + 4 + 4

```python
>>>multiplicacion(1, 3)     
1

>>>multiplicacion(3, 1)     
1

>>>multiplicacion(5, 0)     
0

>>>multiplicacion(5, 8)     
40

>>>multiplicacion('5', 0)     
'Error: Solo es permitido número de tipo entero'
```
