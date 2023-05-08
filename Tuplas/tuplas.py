#Precio Maximo 120
precioMax = 120
marca = 'Adidas'
lista = [('nombrepProducto', 100, 2, 'Nike'),('nombreProducto', 120, 2, 'Nike'),('nombreProducto', 110, 2, 'Adidas')]
lista2= []
for i in lista:
    if i [1] <= precioMax and i [3] == marca:
        lista2.append(i)
print(lista2)
        
            