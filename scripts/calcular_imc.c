#include <stdio.h>

// Función para calcular el IMC, ALGO PARA VER SI GENERA CONFLICTOS
float calcularIMC(float peso, float altura) {
	return peso / (altura * altura);
}

int main() {
	float peso, altura;

	// Solicitar datos al usuario
	printf("Ingresa tu peso en kilogramos: ");
	scanf("%f", &peso);
	printf("Ingresa tu altura en metros: ");
	scanf("%f", &altura);

	float imc = calcularIMC(peso, altura);
	printf("Tu IMC es: %.2f\n", imc);

	return 0;
}