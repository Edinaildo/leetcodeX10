# https://leetcode.com/problems/convert-the-temperature/description/


# Você recebe um número de ponto flutuante não negativo arredondado para duas casas decimais celsius, que denota a temperatura em Celsius .
# Você deve converter Celsius em Kelvin e Fahrenheit e retorná-lo como uma matriz ans = [kelvin, fahrenheit].
# Retorne a matriz ans. Serão aceitas respostas dentro da resposta real.10-5.
# Observe que:

# Kelvin = Celsius + 273.15
# Fahrenheit = Celsius * 1.80 + 32.00
 

# Exemplo 1:

# Entrada: celsius = 36,50
# Saída: [309,65000,97,70000]
# Explicação: A temperatura a 36,50 Celsius convertida em Kelvin é 309,65 e convertida em Fahrenheit é 97,70.

# Exemplo 2:

# Entrada: celsius = 122,11
# Saída: [395,26000,251,79800]
# Explicação: A temperatura a 122,11 Celsius convertida em Kelvin é 395,26 e convertida em Fahrenheit é 251,798.

celsius = 32
def convertTemperature(celsius: float):
        return [celsius + 273.15, celsius * 1.80 + 32.00]

print(convertTemperature(celsius))
