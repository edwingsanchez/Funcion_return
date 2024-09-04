import math

def Saludar(nombre):
    return f"Hola, {nombre}"

def areadeuncirculo(radio):
    return 2.1416 * radio ** 2

def millasakilometros(millas):
    return millas * 1.60934

def repetirtexto(texto, veces):
    return texto * veces

def multiplicar(a, b):
    return a * b

def cambiarcaso(texto):
    return texto.swapcase()

def perimetroderectangulo(largo, ancho):
    return 2*(largo+ancho)

def temperatura_media(maxtemp, mintemp):
    return (maxtemp+mintemp)/2

def calculartempmedia():
    dias = int(input("¿Cuántos días desea introducir? "))
    for i in range(dias):
        max_temp = float(input(f"Introduce la temperatura máxima del día {i + 1}: "))
        min_temp = float(input(f"Introduce la temperatura mínima del día {i + 1}: "))
        media = temperatura_media(max_temp, min_temp)
        print(f"La temperatura media del día {i + 1} es: {media}°C")
        #Tuve que investigarlo

if __name__ == "__main__":
    calculartempmedia()
