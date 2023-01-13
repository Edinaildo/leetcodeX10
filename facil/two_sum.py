# https://leetcode.com/problems/two-sum/

# Dada uma matriz de inteiros nums e um inteiro target, retorne os índices dos dois números de modo que eles somemtarget .
# Você pode supor que cada entrada teria exatamente uma solução e não pode usar o mesmo elemento duas vezes.
# Você pode retornar a resposta em qualquer ordem.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]
           
        if remaining in seen:
           return [seen[remaining], i ]
            
        seen[value] = i 

print(twoSum(nums, target))