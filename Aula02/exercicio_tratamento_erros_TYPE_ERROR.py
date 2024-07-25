#Exemplo de Type Error
"""
try:
    resultado = len(5)
except TypeError as e:
    print(e) #Imprime a mensagem de erro
"""

#Exemplo de Type Check (IF)
"""
numero = 10    
if isinstance(numero, int):
    print("Inteiro")
else:
    print("Não é inteiro")
"""

#TRY EXCEPT
# 
"""
try:
    # Código que pode gerar uma exceção
    resultado = 10/0
except ZeroDivisionError:
    # Código que executa se a exceção ZeroDivisionError for levantada
    print("Divisão por zero não é permitida")
"""

# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, 
# tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
"""
try:
    numero = int(input("Digite o valor em Graus: "))
    resultado = (numero * 9/5) +32
    print(f"{numero}° -> {resultado:.0f}°F")
except ValueError:
    print("Por favor, insira uma entrada válida")
"""