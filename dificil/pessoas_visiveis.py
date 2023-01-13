# Há n pessoas em uma fila e elas são numeradas da esquerda 0 para a direita . Você recebe uma matriz de números inteiros distintos ,
# onde representa a altura da pessoa.
# Uma pessoa pode ver outra pessoa à sua direita na fila se todos no meio forem mais baixos do que os dois.
# Mais formalmente, a pessoa pode ver as outras pessoas se forem mais baixas que ela, e estiverem a sua direita, apenas.
# Retorne uma matriz answer de comprimento n onde answer[i] é o número de pessoas que a pessoa pode ver à sua direita na fila.

 

# Exemplo 1:

# Entrada: alturas = [10,6,8,5,11,9]
#  Saída: [3,1,2,1,1,0]

# Explicação: 
# A pessoa 0 pode ver as pessoas 1, 2 e 4. 
# A pessoa 1 pode ver pessoa 2. 
# A pessoa 2 pode ver a pessoa 3 e 4. 
# A pessoa 3 pode ver a pessoa 4. 
# A pessoa 4 pode ver a pessoa 5. 
# A pessoa 5 não pode ver ninguém, pois ninguém está à direita dela.


# Exemplo 2:

# Entrada: alturas = [5,1,2,3,10]
#  Saída: [4,1,1,1,0]


heights = [10,6,8,5,11,9]

def canSeePersonsCount(heights):
    res, stack = [0] * len(heights), [(len(heights) - 1, heights[-1])]
    for i in range(len(heights) - 2, -1, -1):
        while stack and heights[i] > stack[-1][1]:
            stack.pop()
            res[i] += 1
        if stack:
            res[i] += 1
            stack.append((i, heights[i]))
        return res

print(canSeePersonsCount(heights))