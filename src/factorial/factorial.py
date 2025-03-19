#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num):
    """Calcula el factorial de un número"""
    if num < 0:
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact

def calcular_rango(desde, hasta):
    """Calcula factoriales en el rango especificado"""
    for num in range(desde, hasta + 1):
        print(f"Factorial de {num}! es {factorial(num)}")

# Verificar si el usuario pasó argumentos
if len(sys.argv) < 2:
    entrada = input("Ingrese un número o rango (ej. 4-8, -10, 5-): ")
else:
    entrada = sys.argv[1]

# Determinar el rango según la entrada
if "-" in entrada:
    partes = entrada.split("-")

    if entrada.startswith("-"):  # Caso "-hasta" (ej. "-10")
        desde = 1
        hasta = int(partes[1])
    elif entrada.endswith("-"):  # Caso "desde-" (ej. "5-")
        desde = int(partes[0])
        hasta = 60
    else:  # Caso "desde-hasta" (ej. "4-8")
        desde = int(partes[0])
        hasta = int(partes[1])
else:
    desde = hasta = int(entrada)  # Caso de un solo número

# Calcular factoriales en el rango determinado
calcular_rango(desde, hasta)


