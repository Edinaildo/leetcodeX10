// https://leetcode.com/problems/number-of-1-bits/
 
 
// A ideia é que ao informar uma cadeia binária, o resultado exiba a(s) quantidade(s) de bits "1".


// Exemplo 1:

// Entrada: n = 00000000000000000000000000001011
// Saída: 3
// Explicação: A cadeia binária de entrada 000000000000000000000000000001011 tem um total de três bits '1'.


// Exemplo 2:

// Entrada: n = 00000000000000000000000010000000
// Saída: 1
// Explicação: A cadeia binária de entrada 00000000000000000000000010000000 tem um total de um bit '1'.


// Exemplo 3:

// Entrada: n = 11111111111111111111111111111101
// Saída: 31
// Explicação: A cadeia binária de entrada 111111111111111111111111111111101 tem um total de trinta e um bits '1'.
n = 00000000011100000001000001000011
var hammingWeight = function(int) {
n = n.toString(2);
var result = 0;
for (var i in n) {
    if (n[i] == '1') {
        result++;
    }
}
return result;
};
console.log(hammingWeight(n));
