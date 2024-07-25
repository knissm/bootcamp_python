#Imagine que você está trabalhando com dados de sensores IoT. 
#Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. 
# Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'
"""
try:
    entrada = int(input("Temperatura atual: "))
    if entrada < 18:
        print(f"{entrada}° - Baixa")
    elif entrada >= 18 and entrada <=26:
        print(f"{entrada}° - Normal")
    else:
        print("Alta")
except ValueError:
    print("Por favor, verifique a entrada.")
except KeyboardInterrupt:
    print("Interrompido pelo usuario")
"""
#Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. 
# Dado um registro de log em formato de dicionário como 
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
"""
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log['level']=="ERROR":
    print(log['message'])
"""
#Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
# Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

try:
    email = input("Digite seu e-mail:")
    if "@" not in email or "." not in email:
        print("E-mail inválido, verifique!")
        exit()
    idade = input("Digite sua idade: ")
    if idade.isdigit() == False:
        print("Verifique o valor digitado")

    else:
        idade_validada = int(idade)

    if idade_validada <18 or idade_validada >65:
        print("Idade não permitida! A idade precisa ser entre 18 e 65 anos")
    else:
        print(f"E-mail: {email} | Idade: {idade_validada}. \nDados de usuário válidos!")
except KeyboardInterrupt:
    print("\nOperação cancelada pelo usuário!")

