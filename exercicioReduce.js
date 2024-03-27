const numeros = [5, 10,, 15, 20, 25, 30, 35, 40, 45, 50]

const soma = numeros.reduce(function(acumulador, numero) {
    return acumulador + numero;

}, 0);

console.log(soma);

