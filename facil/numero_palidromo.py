# https://leetcode.com/problems/palindrome-number/description/

# Dado um inteiro x, retorne true se x for um palíndromo, e false caso contrário .

 
# Exemplo 1:

# Entrada: x = 121
# Saída: verdadeiro
# Explicação: 121 é lido como 121 da esquerda para a direita e da direita para a esquerda.

# Exemplo 2:

# Entrada: x = -121
# Saída: falso
# Explicação: Da esquerda para a direita, lê -121. Da direita para a esquerda, torna-se 121-. Portanto, não é um palíndromo.

# Exemplo 3:

# Entrada: x = 10
# Saída: falso
# Explicação: Lê 01 da direita para a esquerda. Portanto, não é um palíndromo.



x = 555

def isPalindrome(x):
    return str(x) == str(x)[::-1]

print(isPalindrome(x))