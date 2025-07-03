'''def funcion_s(lista, largo):
    if largo == 0:

        return 0
    else:
        return lista[largo - 1] + funcion_s(lista, largo - 1)
 

vector = [0] * 100
vector[0] = 1
vector[1] = 1
vector[2] = 1
vector[3] = 2
vector[4] = 1
longitud = 5

print(funcion_s(vector, longitud))

def funcion_s(i_ref, j):

    i_ref[0] = i_ref[0] + j:

    j = 
 

    print(f" i = {i_ref[0]} / j = {j}", end='')



var1 = [2]

var2 = 3

funcion_s(var1, var2)

print(f"\ni = {var1[0]} / j = {var2}")'''


'''3#Completa el siguiente código para que imprima por pantalla 12357.

#------------------------

def funcion_b(cantidad):

    if cantidad <=2:

        return True

    else:

        return False



def funcion_a(numero):

    resultado = False

    divisores = 0

    for candidato in range(1, numero +1):

        if numero % candidato == 0:

            divisores += 1

            resultado = funcion_b(divisores)

    return resultado



for numero in range(1, 11):

    if funcion_a(numero):

        print(numero, end=" ")'''

'''4#Completa el siguiente código para que imprima por pantalla: 6, 108, 648

def funcion_a(numero, multiplicador):

    resultado = 20

    if numero % 2 == 0 :

        resultado = numero * multiplicador

    else:

        resultado = multiplicador * numero

    return resultado



def operar_listas(lista_a, lista_b, lista_c):

    lista_a[0] = funcion_a(lista_a[0], 2)

    lista_b[0] = funcion_a(lista_a[0], funcion_a(lista_a[0], 3))

    lista_c[0] = funcion_a(lista_a[0], lista_b[0])



a = [3]

b = [7]

c = [4]



operar_listas(a, b, c)



print(a[0], ",", b[0], ",", c[0])'''

5#Completa el código para que la salida sea: 123246

''''
for t in range(1,3):

    for n in range(1,4):

        print(t * n, end="")'''

#para que de un bucle infinito
'''i = 1



while i <= 3:

    print("Iteración exterior:", i, end="")



    j = 1

    while True:

        print("   Iteración interior:", j, end="")

        j += 1

        if j == 2:
            break



    i += 1'''

#Completa el código para que la salida sea: ruel


'''def funcion_c(frase):

    resultado = frase

    longitud = len(frase)

    for i in range(0,longitud,5):

        resultado = frase[i:longitud]
 

    return resultado



frase = "HolaMundoCruel"

print(funcion_c(frase))'''
#al ingresar 24 sea año bisiesto
'''
def transformar(valor):
    valor = valor * 7
    valor = valor * 11
    valor = valor + 176
    return valor

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return f"{anio} es un año bisiesto"
    else:
        return f"{anio} no es un año bisiesto"

entrada = int(input("Ingrese un número: "))
anio_transformado = transformar(entrada)
print(es_bisiesto(anio_transformado))'''

9# Completa el código para que se muestren los mensajes A y D al ingresar 5, 0 y 25 respectivamente

'''def ejercicio():
    dia = int(input("Introduce el valor N°1 (día): "))
    mes = int(input("Introduce el valor N°2 (mes): "))
    anio = int(input("Introduce el valor N°3 (año): "))

    dd = 100

    if mes in [1, 3, 5, 7, 8, 10, 12]:
        ultimo_dia_mes = 31
    elif mes in [4, 6, 9, 11]:
        ultimo_dia_mes = 30
    elif mes == 2:
        if (anio % 4 == 0 and not (anio % 100 == 0)) or (anio % 400 == 0):
            ultimo_dia_mes = 29
        else:
            ultimo_dia_mes = 28
    else:
        print("A")  
        if not(dia > 0 or dia ultimo_dia_mes):
             print("B")  
    else:
        if mes < 0 or mes > 12:
            print("C")  
        else:
            print("D")
            ejercicio()'''

'''def funcion_m(valores, tamaño):

    max =[0]


    for indice in range(1, tamaño + 1):



        if valores[indice]>= max:

            max = valores[indice]



    return max



tamaño = 3

valores = [0] * tamaño

valores[0] = 4

valores[1] = 6

valores[2] = 1



print(funcion_m(valores, tamaño))'''

#Completa el siguiente código para que al ingresar el numero 5, se obtenga como salida el numero 13.


def funcion_recursiva(vector, numero):

    contador = 1

    if numero == 1:

        contador = vector[3]+ contador

    else:

        contador = funcion_recursiva(vector, numero - 2)

    return contador



numero = int(input("Ingresar valor: "))



if numero < 4:

    print("El valor debe ser al menos 4 para evitar error en vector[3].")

else:

    vector = [0] * numero

    for indice in range(2, numero):

        vector[indice] =indice * 4



    resultado = funcion_recursiva(vector, numero)

    print(resultado)

