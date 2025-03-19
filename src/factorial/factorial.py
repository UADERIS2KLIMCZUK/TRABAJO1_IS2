#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num):
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
    for num in range(desde, hasta + 1):
        print(f"Factorial de {num}! es {factorial(num)}")

if len(sys.argv) < 2:
    entrada = input("Ingrese un rango en formato desde-hasta (ej. 4-8): ")
else:
    entrada = sys.argv[1]

if "-" in entrada:
    partes = entrada.split("-")
    desde = int(partes[0])
    hasta = int(partes[1])
else:
    desde = hasta = int(entrada)

calcular_rango(desde, hasta)


