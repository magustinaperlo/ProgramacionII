#Ejercicio 1:
#Gestor de Contactos Crea un programa que funcione como un gestor de contactos. El
#programa debe permitir al usuario almacenar nombres y números de teléfono en un
#diccionario, así como buscar, agregar y eliminar contactos. Debe mostrar un menú con las
#siguientes opciones:
#1. Agregar contacto
#2. Buscar contacto
#3. Eliminar contacto
#4. Mostrar todos los contactos
#5. Salir
#El programa debe ejecutarse hasta que el usuario elija la opción "Salir" del menú.
import os 
from Funciones import *

contactos = {}

while True:
    
    print('Bievenido al Gestor de Contactos\n Selecciona la opcion a realizar: \n 1-Agregar Contactos \n 2-Buscar Contacto \n 3-Eliminar Contacto \n 4-Mostrar todos los contactos \n 5-Salir')
    opc = input('Ingresa una opcion: ')
    
    if esNumero(opc) == True:
        opc = int(opc)
        
        if opc == 1:
            
            os.system('clear')
            print('Ingresaste en la opcion 1.\nAgrega el nuevo contacto\n')
            nombre = input('Ingres el nombre: ')
            while True:
                try:
                    numero = int(input('Ingrese el numero: '))
                except ValueError:
                    print('Ingresa un numero valido')
                    continue
                else:
                    break
            contactos[nombre] = numero
        
        elif opc == 2:
            os.system('clear')
            print('Ingresaste en la opcion 2.\nBuscar un contacto\n')
            buscar = input('Ingresa el nombre del contacto a buscar: ')
            
            if buscar in contactos:
                numero = contactos[buscar]
                print(f'El numero de telefono de {buscar} es {numero}')
            else:
                print(f'El contacto {buscar} no existe.')
                
        elif opc == 3:
            os.system('clear')
            print('Ingresaste en la opcion 3.\nEliminar un contacto\n')
            eliminar = input('Ingresa el nombre del contacto a eliminar: ')
            del contactos[eliminar]
        
        elif opc == 4:
            os.system('clear')
            print(f'Ingresaste en la opcion 4.\nAqui tienes la lista de contactos completa:\n{contactos}')
        
        elif opc == 5:
            os.system('clear')
            print('Gracias por usar el sistema, hasta la proxima.')
            break
                        