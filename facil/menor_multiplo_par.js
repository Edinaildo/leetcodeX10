// https://leetcode.com/problems/smallest-even-multiple/


// Dado um inteiro positivon , retorne o menor inteiro positivo que seja múltiplo de ambos 2 en .
 

// Exemplo 1:

// Entrada: n = 5
// Saída: 10
// Explicação: O menor múltiplo de 5 e 2 é 10.

// Exemplo 2:

// Entrada: n = 6
// Saída: 6
// Explicação: O menor múltiplo de 6 e 2 é 6. Observe que um número é um múltiplo de si mesmo.
n = 6
var smallestEvenMultiple = function(n) {
    for (let i = 1; i > 0; i++) {
     let num = n * i;
     if ((num % 2) === 0) {
         return num;
     }
 }
};
console.log(smallestEvenMultiple(n))
