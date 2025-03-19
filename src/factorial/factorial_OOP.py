import sys

class Factorial:
    """Clase para calcular el factorial de un número o un rango de números."""
    
    def __init__(self, min_value=1, max_value=1):
        self.min_value = min_value
        self.max_value = max_value

    def calcular_factorial(self, num):
        """Calcula el factorial de un número."""
        if num < 0:
            raise ValueError("El factorial de un número negativo no existe")
        fact = 1
        for i in range(2, num + 1):
            fact *= i
        return fact

    def run(self):
        """Calcula el factorial para el rango definido en la instancia."""
        for num in range(self.min_value, self.max_value + 1):
            print(f"Factorial de {num}! es {self.calcular_factorial(num)}")

# Manejo de argumentos de entrada
if len(sys.argv) < 2:
    entrada = input("Ingrese un número o rango (ej. 4-8, -10, 5-): ")
else:
    entrada = sys.argv[1]

# Determinar los valores de min y max
if "-" in entrada:
    partes = entrada.split("-")

    if entrada.startswith("-"):  # Caso "-hasta" (ej. "-10")
        min_value = 1
        max_value = int(partes[1])
    elif entrada.endswith("-"):  # Caso "desde-" (ej. "5-")
        min_value = int(partes[0])
        max_value = 60
    else:  # Caso "desde-hasta" (ej. "4-8")
        min_value = int(partes[0])
        max_value = int(partes[1])
else:
    min_value = max_value = int(entrada)  # Caso de un solo número

# Crear instancia de la clase y ejecutar
factorial_calc = Factorial(min_value, max_value)
factorial_calc.run()
