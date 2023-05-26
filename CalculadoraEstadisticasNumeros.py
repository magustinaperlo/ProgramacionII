#Ejercicio2:
#Calculadora de Estadísticas de Números
#Escribe un programa que permita al usuario ingresar una lista de números y realice los
#siguientes cálculos estadísticos:
#1. Calcular la suma de los números.
#2. Calcular el promedio de los números.
#3. Encontrar el número mínimo y el número máximo de la lista.
#4. Calcular la desviación estándar de los números.
#El programa debe solicitar al usuario que ingrese la lista de números separados por espacios y
#luego imprimir los resultados de los cálculos estadísticos.

import statistics
import math

numeros_lista = []

print('Bienvenido a la Calculadora de Estadistica.\nPuedes ingresar la cantidad de numeros que desees separados por un espacio, luego se calculara:\n1-La suma de los numeros.\n2-Promedio de los numeros.\n3-Encuentra el numero minimo y maximo.\n4-La desviación estándar de los números.')

numeros = input("Ingrese varios números separados por espacios: ")
numeros = numeros.split()  

for numero in numeros:
    numeros_lista.append(int(numero))  
print(numeros_lista)

print(f'La suma de todos los elementos es: {sum(numeros_lista)}')

promedio = sum(numeros_lista)/len(numeros_lista)

print(f'El promedio de los numeros ingresados es: {promedio}')    

print(f'El numero minimo de la lista es {min(numeros_lista)} y el numero maximo es {max(numeros_lista)}')

cuadrado_lista = []

for num in numeros_lista:
    diferencia = num - promedio
    cuadrado = diferencia ** 2
    cuadrado_lista.append(cuadrado)
    
varianza = sum(cuadrado_lista) / len(numeros_lista)

desviacion_estandar = math.sqrt(varianza)

print('La desviacion estandar de los numeros es: ' + "{0:.2f}".format(float(desviacion_estandar)))

#Calculando la desviacion estandar utilizando la funcion stdev.

desviacion_estandar2 = statistics.stdev(numeros_lista)

print('La desviacion estandar calculada con la funcion es: ' + "{0:.2f}".format(float(desviacion_estandar2)))