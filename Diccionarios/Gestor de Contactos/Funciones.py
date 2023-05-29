def esNumero(a):
    if a.isnumeric():
        a = int(a)
        return(True)
    else:
        return(False)
   




#se me ocurre que podés añadir esta validación para ver si el contacto existe en la opción 3:

def contactoExiste(contactos, nombre):
    if nombre in contactos:
        return True
    else:
        return False

    
