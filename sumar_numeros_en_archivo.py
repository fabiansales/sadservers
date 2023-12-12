import os
# suma la segunda columna de Numeros de una lista
def suma(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

def leer_numeros(nombre_lista):
    promedio = 0.0
    suma = 0
    contador = 0
    with open(nombre_lista,"r") as lista:
        content = lista.read()
        #creo lista con el contenido de lo leido
        contenido = content.split()     
        #print(contenido)

    for longitud in range(1,len(contenido),2):
        suma += float(contenido[longitud])
        contador += 1 # para saber por cuando dividir
    promedio = float(suma/contador)
    print("{:.2f}".format(promedio))
    return format(promedio)

# print(suma([1,3,4]))

print(leer_numeros('list'))

