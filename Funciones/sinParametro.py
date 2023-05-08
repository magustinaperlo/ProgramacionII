import random


def numRandom():
    cont = 0 
    while cont < 3:
        num_random = random.randint(0,100)
        cont += 1
        print(num_random)


def multiplicacionAleaotira():
    cont = 0
    numeros = []
    
    while cont < 3 :
        num_random = random.randint(0,100)
        numeros.append(num_random)
        cont += 1
    print(numeros)
    
    for i in numeros:
        resultado = i * 2 
        print(resultado)
           
        
def saludar():
    print('Hola Mundo')
    
    
def numPar():
    cont = 0
    num_pares = []
    while cont < 5 :
        num_random = random.randint(0,100)
        if num_random % 2 == 0:
            num_pares.append(num_random)
            cont += 1
    print(num_pares)
#numPar()

def numImpar():
    cont = 0
    num_impares = []
    while cont < 5:
        num_random = random.randint(0,100)
        if num_random % 2 != 0 :
            num_impares.append(num_random)
            cont += 1 
    print(num_impares)
#numImpar()


def mezcladetupla():
    numeros = [1,2,3,4,5,6,7,8,9]
    random.shuffle(numeros)
    print(numeros)
#mezcladetupla()

def mayus():
    nombre = 'GonZaLo'
    nombres_mayus = nombre.upper()
    print(nombres_mayus)
    
#mayus()

def minusculas():
    nombre = 'SANTIAGO'
    nombre_min = nombre.lower()
    print(nombre_min)
#minusculas()

def crearPass():
    caracteres = 'aDFawd123787Klkmnsaq1239865270LQW'
    random.shuffle(caracteres)
    print(caracteres)
crearPass()
    