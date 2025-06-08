function calcularIMC(peso, altura) {
    if (altura <= 0) {
        return "Error: La altura debe ser mayor que cero. solo para prevenir división por cero";
    }
    const imc = peso / (altura * altura);
    return Math.round(imc * 100) / 100;
}

function fibonacci(n) {
    if (n <= 0) return 0;
    if (n === 1) return 1;
    let a = 0, b = 1;
    for (let i = 2; i <= n; i++) {
        [a, b] = [b, a + b];
    }
    return b;
}

// Ejemplo de uso:
const peso = 70; // kg
const altura = 1.75; // metros
const imcCalculado = calcularIMC(peso, altura);
console.log(`Para un peso de ${peso} kg y una altura de ${altura} m, el IMC es: ${imcCalculado}`);

// Ejemplo de uso de Fibonacci:
console.log(`El 10mo número de Fibonacci es: ${fibonacci(10)}`);

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