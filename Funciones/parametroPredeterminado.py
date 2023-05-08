def celsius_a_fahrenheit(celsius, escala='fahrenheit'):
    if escala == 'fahrenheit':
        return (celsius * 9/5) + 32
    elif escala == 'kelvin':
        return celsius + 273.15
    else:
        return "Error: Escala no válida"

def sumar(a, b=0):
    return a + b

def restar(a, b=0):
    return a - b

def dividir(a, b=1):
    return a / b

def area_triangulo(base, altura= 12):
    area = (base * altura) / 2
    return area
