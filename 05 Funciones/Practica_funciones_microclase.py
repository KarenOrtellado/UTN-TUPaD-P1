#Funciones
'''
def incrementar (x):
    x += 1
    return x

n = 5
print(incrementar(n))
print (n)
'''

#Valor por referencia
#Parámetro por valor
'''
def agregar_elemento(lista,elemento):
    lista.append(elemento)

mi_lista = [1,2,3]
agregar_elemento(mi_lista, 4)
print(mi_lista)
'''

'''
def obtener_resto(a,b):
    return a % b

def obtener_resto_sin_mod(a,b):
    return a -(b * (a//b))

def es_multiplo(x,y):
    return obtener_resto(x,y) == 0

print(obtener_resto(10,3))
print(obtener_resto_sin_mod(10,3))
print(es_multiplo(12,3))
'''

'''
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Ana")
'''

'''
def siguiente(n):
    return n +1

def doble(n):
    return n *2

print(doble(siguiente(4)))


valor = int(input("Ingrese un numero entero: "))
print("El siguiente es: " , siguiente(valor))
'''

a = 10
def cambiar():
    global a
    a = 20

cambiar()
print(a)