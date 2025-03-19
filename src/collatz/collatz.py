import matplotlib.pyplot as plt

def collatz(n):
    """Calcula la cantidad de iteraciones hasta llegar a 1 en la secuencia de Collatz."""
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

# Generar datos
x_vals = list(range(1, 10001))  # Números del 1 al 10,000
y_vals = [collatz(n) for n in x_vals]  # Cantidad de iteraciones para cada número

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.scatter(x_vals, y_vals, s=1, color='blue')
plt.xlabel("Número inicial (n)")
plt.ylabel("Número de iteraciones")
plt.title("Conjetura de Collatz (1-10,000)")
plt.grid()
plt.show()
