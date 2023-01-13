# https://leetcode.com/problems/permutations/

# Dado um array nums de inteiros distintos, retorne todas as permutações possíveis . 
# Você pode retornar a resposta em qualquer ordem .

 

# Exemplo 1:

# Entrada: nums = [1,2,3]
# Saída: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1 ,2],[3,2,1]]
# Exemplo 2:

# Entrada: nums = [0,1]
# Saída: [[0,1],[1,0]]
# Exemplo 3:

# Entrada: nums = [1]
# Saída: [[1]]
import itertools
nums = [1,2,3,4,5]
def permute(nums):
    x = itertools.permutations(nums)
    m = [i for i in x]
    return m

print(permute(nums))
