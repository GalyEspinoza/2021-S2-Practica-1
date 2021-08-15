def contarDigitosPares(num):
    if isinstance(num, int):
        return contarDigitosPares_Aux(num)
    else:
        return 'Error: Solo es permitido número de tipo entero'


def contarDigitosPares_Aux(num):
    if num < 10:
        if((num % 10) % 2 == 0):
            return 1
        else:
            return 0
    else:
        if((num % 10) % 2 == 0):
            return 1 + contarDigitosPares_Aux(num // 10)
        else:
            return contarDigitosPares_Aux(num // 10)
       
        
###########################################################################

def contarTriosDeDigitos(num):
    if isinstance (num, int):
        return contarTriosDeDigitos_Aux(num)
    else:
        return 'Error: Solo es permitido número de tipo entero'
    
    
def contarTriosDeDigitos_Aux(num):
    if num<100:
        return 0
    else:
        return 1 + contarTriosDeDigitos (num // 10 // 10 // 10)

##########################################################################


def sumatoriaParcial(ini,fin):
    if (isinstance(ini, int) and isinstance (fin, int)):
        if (fin < ini):
            return 'Error: El parámetro Fin debe ser mayor o igual que Ini'
        else:
            return sumatoriaParcial_Aux(ini, fin)
    else:
        return 'Error: Solo es permitido número de tipo entero'
        
def sumatoriaParcial_Aux(ini,fin):
    if (ini > fin):
        return 0
    else:
        return ini + sumatoriaParcial_Aux(ini + 1, fin)
    
########################################################################

def multiplicacion(op1, op2):
    if (isinstance(op1, int) and isinstance(op2, int)):
        return multiplicacion_Aux(op1, op2)
    else:
        return 'Error: Solo es permitido número de tipo entero'


def multiplicacion_Aux(op1, op2):
    if (op1 >= 0) and (op2 >= 0):
        if (op2 <= 0):
            return 0
        else:
            return op1 +  multiplicacion_Aux(op1,op2 - 1)
    else:
        return 'Error: Solo es permitido número de tipo entero'
