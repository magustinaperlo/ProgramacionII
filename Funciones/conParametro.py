


def sum(a,b):
    resultado = a + b
    print(resultado)
    
def concatenacionSaludo(nombre):
    saludo = f'Hola' + nombre
    print(saludo)
    
def numPar(a):
    if a % 2 == 0:
        print('El numero ' + a +'es par')

def numImpar(a):
    if a % 2 != 0:
        print('El numero ' + a + 'es impar')
        

def validacion_edad(edad):
    if edad >= 18:
        print('Eres mayor')
    elif edad >= 100:
        print('No creo que tengas esa edad')
    elif edad < 0:
        print('No existen edades negativas')
    else:
        print('Eres menor')
#validacion_edad(int(input('Ingrese Su edad: ')))



def ingresarNumeros(num):
    numeros = []
    cont = 0 
    while cont < 2:
        num = int(input('Ingrese Numeros: '))
        numeros.append(num)
        cont += 1
    print(numeros)
    
ingresarNumeros(int(input('Ingrese Numeros: ')))
