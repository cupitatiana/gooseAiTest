def calcular_imc(peso_kg, altura_metros):
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso_kg (float): Peso en kilogramos.
        altura_metros (float): Altura en metros.

    Returns:
        float: El valor del IMC.
    """
    if altura_metros <= 0:
        return "Error: La altura debe ser mayor que cero."
    imc = peso_kg / (altura_metros ** 2)
    return round(imc, 2)

if __name__ == "__main__":
    # Ejemplo de uso:
    peso = 70  # kg
    altura = 1.75  # metros
    imc_calculado = calcular_imc(peso, altura)
    print(f"Para un peso de {peso} kg y una altura de {altura} m, el IMC es: {imc_calculado}")

    if isinstance(imc_calculado, (int, float)):
        if imc_calculado < 18.5:
            print("Clasificación: Bajo peso")
        elif 18.5 <= imc_calculado < 24.9:
            print("Clasificación: Peso normal")
        elif 25 <= imc_calculado < 29.9:
            print("Clasificación: Sobrepeso")
        else:
            print("Clasificación: Obesidad")

def fibonacci(n):
    """
    Calcula el n-ésimo número de la serie Fibonacci.

    Args:
        n (int): El índice del número en la serie (0-indexado).

    Returns:
        int: El n-ésimo número de Fibonacci.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Ejemplo de uso de Fibonacci:
# print(f"El 10mo número de Fibonacci es: {fibonacci(10)}")
