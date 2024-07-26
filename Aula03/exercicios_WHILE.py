"""
import time

while True:
    print("Verificando novos dados...")
    # Aqui você pode adicionar o código para verificar novos dados,
    # por exemplo, checar a existência de novos arquivos em um diretório,
    # fazer uma consulta a um banco de dados ou API, etc.
    
    time.sleep(10)  # Pausa o loop por 10 segundos
"""
#Leitura de Dados até Flag. 
# Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.]
"""
dados = []
entrada = ""
while entrada.lower() != 'sair':
    entrada = input("Digite um valor (ou 'sair' para terminar): ")
"""
#Validação de Entrada. 
# Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
while True:
    numero = input("Digite um número entre 1 e 10: ")
    if numero.isdigit() == False:
        print("Digite uma entrada válida!")
        escolha = input("Deseja entrar com um numero novamente? S/N ").lower()
        if escolha == "n":
            break
          
        numero_convertido = int(numero)
        while numero_convertido < 1 or numero_convertido > 10:
            print("Numero fora do intervalo")
            break
        print(f"Número: {numero_convertido} ")
