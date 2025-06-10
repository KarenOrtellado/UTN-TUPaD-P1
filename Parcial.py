i = 1
#while i <= 2:
#    print("iteración exterior:", i, end= "")
#    j=1
#    bandera = True
#    while bandera:
#        print("iteración interior:", j, end= "")
#        j -= 1
 #       if j !=2:
 #           bandera = False
 #           
 #   i= i+ 1


#for t in range(1,3):
#    for n in range (1,4):
#        print(t*n, end="")


#for n in range (1,11):
#    bandera = False
#    d= 0
#
#    for c in range (1, n+1):
#        if n % c == 0:
#            d += 1
#
#            if d >=  2:
#                bandera = True
#            else:
#                bandera =False
#
#    if bandera:
#        print(n,end="")

N = 5
A = [0] * N
B = [0] * N

#for i in range(N):
#    A[i] = i + i + i
#
#for i in range(N):
#    B[i]= i*2
#
#contador=0
#for i in range (N):
#    if A[0] == A[i] ==  B[i]:
#        contador += 1
#    N =N - contador
#
#resultado =str(contador)
#
#if A[0] ==  1:
#    resultado = "VERDADERO"
#elif A[0] ==  2:
#    resultado = "2"
#elif A[0] == 3:
#    resultado = "FALSO"
#
#print(resultado)*#

#contador = 1
#suma = 0
#bandera = True
#
#num1 = int(input("Ingrese un valor N°1: "))
#
#while bandera:
#    num2 = int(input("Ingrese un valor N°2: "))
#    suma = suma + num2
 #   contador = contador + 1
#
#    while contador <= num1:
#        print(suma, end=" ")
#        bandera = False
#        if contador == num1:
#            bandera = True
#        break

#num1 =3
#vector =[4,6,1]

#mayor=vector[0]

#for i in range(1,num1):
#        if vector[i] > mayor:
#                mayor = vector[i]

#print(mayor)

nota = 85

if nota >= 90:

    print("Excelente.")

elif nota >= 75:

    print("Muy bien.")

else:

    print("Suficiente.")