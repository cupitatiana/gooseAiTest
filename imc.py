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
