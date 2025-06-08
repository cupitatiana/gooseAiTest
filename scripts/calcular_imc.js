function calcularIMC(peso, altura) {
    if (altura <= 0) {
        // mensaje de error si la altura es cero o negativa
        return "Error: La altura debe ser mayor que cero.";
    }
    const imc = peso / (altura * altura);
    return Math.round(imc * 100) / 100;
}

// Ejemplo de uso:
const peso = 70; // kg
const altura = 1.75; // metros
const imcCalculado = calcularIMC(peso, altura);
console.log(`Para un peso de ${peso} kg y una altura de ${altura} m, el IMC es: ${imcCalculado}`);

if (typeof imcCalculado === 'number') {
    if (imcCalculado < 18.5) {
        console.log("Clasificación: Bajo peso");
    } else if (imcCalculado < 24.9) {
        console.log("Clasificación: Peso normal");
    } else if (imcCalculado < 29.9) {
        console.log("Clasificación: Sobrepeso");
    } else {
        console.log("Clasificación: Obesidad");
    }
}