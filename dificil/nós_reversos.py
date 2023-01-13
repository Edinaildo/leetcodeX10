# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Dado o valor headde uma lista encadeada, inverta os nós da lista k de cada vez e retorne a lista modificada .
# k é um número inteiro positivo e é menor ou igual ao comprimento da lista encadeada.
# Se o número de nós não for um múltiplo dos k nós deixados de fora, no final, deve permanecer como está.
# Você não pode alterar os valores nos nós da lista, apenas os próprios nós podem ser alterados.

# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]


head = [1,2,3,4,5]
k = 2
def reverseKGroup(self, k, head):
    curr = head
    for _ in range(k):
        if not curr: return head
        curr = curr.next
		        
    prev = None
    curr = head
    for _ in range(k):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    head.next = self.reverseKGroup(curr, k)
    return prev

print(reverseKGroup(k,head))
