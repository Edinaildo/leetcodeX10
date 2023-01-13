# https://leetcode.com/problems/generate-parentheses/

# Dados os n pares de parênteses, escreva uma função para gerar todas as combinações de parênteses bem formados .

# Exemplo 1:

# Entrada: n = 3
# Saída: ["((()))","(()())","(())()","()(())","()()( )"]

# Exemplo 2:

# Entrada: n = 1
# Saída: ["()"]
n = 10
def generateParenthesis(n):
    def combination(i,j):
        if i==0:
            return [')'*j]
        if j<i:
            return []
        lis1=combination(i-1,j)
        lis2=combination(i,j-1)
        for l in range(len(lis1)):
            lis1[l]="("+lis1[l]
        for m in range(len(lis2)):
            lis2[m]=")"+lis2[m]
        return lis1+lis2
    return combination(n,n)

print(generateParenthesis(n))