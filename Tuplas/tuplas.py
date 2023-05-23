#Tenemos una lista de Tuplas que representan ciertas características de una serie de productos.
#Cada tupla tiene 4 elementos:
#nombre del producto
#precio
#cantidad disponible
#marca
#Se desea obtener una lista de productos que cumplan con ciertas condiciones de búsqueda:
#precio máximo
#marca específica

precioMax = 120
marca = 'Adidas'
lista = [('nombrepProducto', 100, 2, 'Nike'),('nombreProducto', 120, 2, 'Nike'),('nombreProducto', 110, 2, 'Adidas')]
#error de tipeo en index0 de la lista "nombrepProducto"
lista2= []
for i in lista:
    if i [1] <= precioMax and i [3] == marca:
        lista2.append(i)
print(lista2)
       
#Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la
#longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
#El programa termina cuando el usuario introduce un cero.

meses = ('','Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Noviembre','Diciembre')
num_mes = 1 
while num_mes != 0:
    num_mes = int(input('Ingrese un Numero: '))
    if num_mes > 12:
        print('Error no hay mas de 12 meses')
    for i in meses:
        if meses.index(i) == num_mes:
            print(i)   
           
  #sugerencia: 
meses = ('', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Noviembre', 'Diciembre')
num_mes = 1
while num_mes != 0:
    num_mes = int(input('Ingrese un número: '))
    if num_mes == 0:
        break
    elif num_mes < 1 or num_mes > len(meses) - 1:
        print('Error: El número está fuera del rango.')
    else:
        print(meses[num_mes])


#Crea una tupla con números, pide al usuario un número por teclado e indica cuantas veces se
#repite según lo halle en la tupla que has creado.
#RESUELVE validar los ingresos del usuario. 

numeros = (1,2,2,4,5,8,9,6,5,4,3,9,7,8,9,0,1)

num_consulta = int(input('Ingrese un numero a buscar: '))
num_encontrado = numeros.count(num_consulta)
print('La cantidad de veces que se repite es: ' + str(num_encontrado))

#Crea una tupla con números e indica el numero con mayor valor y el que menor tenga.

numerosAltosBajos = (1,2,3,4,5,6,7,8,9,10,12,15,8,4,23,89,6,9)

num_alto = max(numerosAltosBajos)
num_bajo = min(numerosAltosBajos)

print('El numero mas bajo es: ' + str(num_bajo))
print('El numero mas alto es: ' + str(num_alto))

#Crea una tupla con valores ya predefinidos del 1 al 10, pide al usuario un índice por teclado y muestra los valores de la tupla.
#RESUELVE el caso en que no exista ese índice en la tupla.

tupla = (1,2,3,4,5,6,7,8,9,10)
num_ingresado = int(input('Ingrese un Indice: '))

while True:
    if num_ingresado < 0 or num_ingresado > 9:
        print('Indice fuera de parametro')
        break
    else:
        (print(tupla[num_ingresado]))
        break
        
  #sugerencia: 
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
try:
    num_ingresado = int(input('Ingrese un índice: '))
    if num_ingresado < 0 or num_ingresado >= len(tupla):
        print('Error: Índice fuera de rango.')
    else:
        print(tupla[num_ingresado])
except ValueError:
    print('Error: Ingrese un número entero válido.')

    
#Escribe un programa que solicite al usuario que ingrese una lista de números enteros.
#El programa debe crear una tupla a partir de la lista y luego imprimir la tupla en orden inverso.

cont = 0 
lista_numeros = []
while cont < 10:
    ing_num = int(input('Ingresa un numero entero: '))
    lista_numeros.append(ing_num)
    cont += 1
#lista_mezclada = reversed(lista_numeros)
#tupla_numeros = tuple(lista_mezclada)
#podemos hacer todo en 1 sola linea:
lista_mezclada = tuple(reversed(lista_numeros))
print(tupla_numeros)
