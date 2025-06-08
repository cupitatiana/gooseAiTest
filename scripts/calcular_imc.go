package main

import (
	"fmt"
)

// Función para calcular el IMC, el peluca sapee cambio para generar confilcto
type Persona struct {
	Altura float64 // en metros
	Peso   float64 // en kilogramos
}

func (p Persona) CalcularIMC() float64 {
	return p.Peso / (p.Altura * p.Altura)
}

func main() {
	var altura, peso float64

	// Solicitar datos al usuario
	fmt.Print("Ingresa tu altura en metros: ")
	fmt.Scan(&altura)
	fmt.Print("Ingresa tu peso en kilogramos: ")
	fmt.Scan(&peso)

	persona := Persona{Altura: altura, Peso: peso}
	imc := persona.CalcularIMC()

	fmt.Printf("Tu IMC es: %.2f\n", imc)
}