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

#Crie um programa que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.
"""
try:
    entrada = input("Digite uma palavra ou frase: ").lower()
    if isinstance(entrada, str):
        formatado = entrada.replace(" ", "")
        if formatado == formatado[::-1]:
            print(f"A palavra {entrada} é um palíndromo.")
        else:
            print(f"A palavra {entrada} não é um palíndromo!")
    else:
        print("Entrada inválida. Digite uma palavra ou frase!")
except KeyboardInterrupt:
    print("Interrompido pelo usuário!")
"""
#Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
try:
    entrada_lista = input("Digite uma lista de números separada por vírgula: ")
    numeros_str = entrada_lista.split(",")
    numeros_int = []

    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print(f"Lista dos numeros inteiros: {numeros_int}")
    
except ValueError:
    print("Verifique a entrada. Somente números inteiros são permitidos")
except KeyboardInterrupt:
    print("Capturado um KeyboardInterrupt. Operação interrompida pelo usuário.")

