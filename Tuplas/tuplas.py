
precioMax = 120
marca = 'Adidas'
lista = [('nombrepProducto', 100, 2, 'Nike'),('nombreProducto', 120, 2, 'Nike'),('nombreProducto', 110, 2, 'Adidas')]
lista2= []
for i in lista:
    if i [1] <= precioMax and i [3] == marca:
        lista2.append(i)
print(lista2)
        

meses = ('','Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Noviembre','Diciembre')
num_mes = 1 
while num_mes != 0:
    num_mes = int(input('Ingrese un Numero: '))
    if num_mes > 12:
        print('Error no hay mas de 12 meses')
    for i in meses:
        if meses.index(i) == num_mes:
            print(i)         

numeros = (1,2,2,4,5,8,9,6,5,4,3,9,7,8,9,0,1)
num_consulta = int(input('Ingrese un numero a buscar: '))
num_encontrado = numeros.count(num_consulta)
print('La cantidad de veces que se repite es: ' + str(num_encontrado))


numerosAltosBajos = (1,2,3,4,5,6,7,8,9,10,12,15,8,4,23,89,6,9)

num_alto = max(numerosAltosBajos)
num_bajo = min(numerosAltosBajos)

print('El numero mas bajo es: ' + str(num_bajo))
print('El numero mas alto es: ' + str(num_alto))


tupla = (1,2,3,4,5,6,7,8,9,10)
num_ingresado = int(input('Ingrese un Indice: '))


while True:
    if num_ingresado < 0 or num_ingresado > 9:
        print('Indice fuera de parametro')
        break
    else:
        (print(tupla[num_ingresado]))
        break
    
