#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#Edad = int(input("Ingrese su edad"))      #Se Solicita al usuario que ingrese su edad

#if Edad > 18:                            # Condición If que sea mayor a 18 años
#    print ("Es mayor de edad")           # Entonces devuelve el mensaje "Es mayor de edad".

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un 
#mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

#Nota = float(input("Por favor, ingrese su nota"))              #Se solicita al usuario que ingrese su nota

#if Nota >= 6:                                                #Condición que la nota sea mayor o igual a 6
#    print("Aprobado")                                        # entonces devuelve aprobado
#else:                                                        # Si no se cumple devuelve desaprobado
#    print("Desaprobado")

#3)Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par".

#numero = int(input("Ingrese un número Par: "))              

#if (numero%2 == 0):                                           #condición que tomar que el número sea par
#    print ("ha ingresado un número par")                      # entonces imprime el mensaje "ha ingresado un numero par", de lo contrario vuelve a solicitar un núm par
#else:
#    print ("Por favor, ingrese un número par")

#4)Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# Niño/a: menor de 12 años. Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años. Adulto/a: mayor o igual que 30 años.

#Edad = int(input("Ingrese su edad: "))

#primera condición para Niño
#if Edad < 12:
#    print("es un Niño/a")
#Condición para adolescente
#elif (Edad >=12 and Edad < 18):
#    print("es un Adolescente")
#condición para adulto joven
#elif (Edad >=18 and Edad < 30):
#    print("es un Adulto/a joven")
#else:
#    print("es un Adulto")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, 
#imprimir por pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir porpantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"


#contraseña=input("Ingrese su contraseña, debe tener entre 8 y 14 caracteres: ")
#Condicion de longitud utilizando len. Imprime que es correcto
#if(len(contraseña)>=8 and len(contraseña)<=14):
#    print("Ha ingresado una contraseña correcta")  
#Caso contrario solicita nuevamente ingresar una contraseña
#else: 
#    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# ejercicio 6 

#importamos los datos
#import random
#from statistics import mode, median, mean

#genero una lista 
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
#medidas
#moda = mode(numeros_aleatorios)
#mediana = median(numeros_aleatorios)
#media =mean(numeros_aleatorios)

#Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda
#if media > mediana > moda:
#    print ("Sesgo positivo o a la derecha")
#Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda
#elif media < mediana < moda:
#    print ("Sesgo negativo")
#Sin sesgo: cuando la media, la mediana y la moda son iguales.
#elif media == moda == mediana:
#    print("Sin sesgo")
#Si no se cumple ninguna
#else:
#    print("no se puede determinar")

#7)Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, 
#añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual
#lo ingresó el usuario e imprimirlo por pantalla.

#frase = input("Por favor ingrese una frase o una palabra: ")

#encontré que para poder acceder a la última letra tenemos que utilizar -1 así (frase[-1])y utilizamos IN para determinar dentro de..
#if frase [-1] in ("AEIOUaeiou"):
#    print(f"{frase}!")
#caso contrario imprime tal cual se ingresó
#else:
#    print(f"{frase}")


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla


#nombre = input("Ingrese su nombre, por favor: ")

#mostramos en pantalla las opciones a elegir
#print("""En este programa puede realizar cualquiera de las siguientes operaciones:
#1. Si quiere su nombre en mayúsculas.
#2. Si quiere su nombre en minúsculas.
#3. Si quiere su nombre con la primera letra mayúscula.""")

#opcion = int(input("Ingrese la opción deseada: "))

#if opcion == 1:
#    print (nombre.upper())
#elif opcion == 2:
#    print (nombre.lower())
#elif opcion == 3:
#    print (nombre.title())
#else:
#    print("Por favor, seleccione una opción válida")

#ejercicio 96


# Pedimos al usuario que ingrese la magnitud del terremoto
#magnitud_terremoto = float(input("Por favor, ingrese la magnitud del terremoto según la escala de Ritcher: "))

# Si la magnitud del terremoto < que 3, imprimimos "Muy leve"
#if magnitud_terremoto < 3:
#  print("Muy leve")
# Si la magnitud del terremoto es >= que 3 y < que 4, imprimimos "Leve"
#elif 3 <= magnitud_terremoto < 4:
#  print("Leve")
# Si la magnitud del terremoto es >= que 4 y < que 5, imprimimos "Moderado"
#elif 4 <= magnitud_terremoto < 5:
#  print("Moderado")
# Si la magnitud del terremoto es >= que 5 y < que 6, imprimimos "Fuerte"
#elif 5 <= magnitud_terremoto < 6:
#  print("Fuerte")
# Si la magnitud del terremoto es >= que 6 y m< que 7, imprimimos "Muy fuerte"
#elif 6 <= magnitud_terremoto < 7:
#  print("Muy fuerte")
#else:
#  print("Extremo")

#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
#El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# Pedimos al usuario que ingrese el hemisferio
#hemisferio = input("Por favor, ingrese el hemisferio (N/S): ")
# Estandarizamos la respuesta del usuario convirtiéndola en minúscula
#hemisferio = hemisferio.lower()

# Pedimos al usuario que ingrese el mes del año
#mes = int(input("Por favor, ingrese el mes del año en números: "))

# Pedimos al usuario que ingrese el día del mes
#dia = int(input("Por favor, ingrese el día del mes en números: "))


# Hacemos un condicional anidado, primero colocamos todo lo relativo al hemisferio sur
#if hemisferio == "s":
  # Si es después del 21/12, en cualquier momento de enero o febrero, o antes del 20/3 imprimimos "Verano"
#  if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
#    print("Verano")
  # Si es después del 21/3, en cualquier momento de abril o mayo, o antes del 20/6 imprimimos "Otoño"
#  elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
#    print("Otoño")
  # Si es después del 21/6, en cualquier momento de julio o agosto, o antes del 20/9 imprimimos "Invierno"
#  elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
#    print("Invierno")
  # Si es después del 21/9, en cualquier momento de octubre o noviembre, o antes del 20/12 imprimimos "Primavera"
#  elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
#    print("Primavera")
# Luego colocamos lo relativo al hemisferio norte
#elif hemisferio == "n":
  # Si es después del 21/12, en cualquier momento de enero o febrero, o antes del 20/3 imprimimos "Invierno"
#  if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
#    print("Invierno")
  # Si es después del 21/3, en cualquier momento de abril o mayo, o antes del 20/6 imprimimos "Primavera"
#  elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
#    print("Primavera")
  # Si es después del 21/6, en cualquier momento de julio o agosto, o antes del 20/9 imprimimos "Verano"
#  elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
#    print("Verano")
  # Si es después del 21/9, en cualquier momento de octubre o noviembre, o antes del 20/12 imprimimos "Otoño"
#  elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
#    print("Otoño")