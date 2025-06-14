def cuenta_regresiva(numero):
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero - 1)
    else:
        print("¡Despegue!")

cuenta_regresiva(3)

def saludo(nombre):
    return f"Hola, {nombre}!"

print(saludo("Ana"))

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

resultado = calcular_area_rectangulo(5, 3)
print(resultado)

def calcular_precio_final(precio, descuento=0):
    precio_final = precio - (precio * descuento / 100)
    return round(precio_final, 2)

resultado = calcular_precio_final(120, 15)
print(resultado)