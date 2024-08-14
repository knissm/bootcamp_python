#72
#Crie um programa que tenha uma tupla totalmente preenchida
#com uma contagem por extenso de zero até vinte
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

"""
num_extenso = ("zero","um", "dois","três","quatro","cinco","seis","sete","oito","nove","dez",
"onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")

while True:
    numero = int(input("Digite um número [0 - 20]: "))
    for i, n in enumerate(num_extenso):
        if numero <0 or numero >20:
            numero = int(input("Entrada Inválida. Digite um número [0 - 20]: "))

        if numero == i:
            print(num_extenso[numero])
    
    escolha = str(input("Deseja continuar? [S/N]: ")).lower().strip()[0]
    if escolha == 'n':
        break
"""

#73

# Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro, na ordem de colocação.
# Depois mostre:
# a) apenas os 5 primeiros colocados
# b) os últimos 4 colocados da tabela
# c) uma lista com os times em ordem alfabética
# d) em que posição na tabela está o time da Chapecoense

"""
times = (
    "Atlético", "Flamengo", "Corinthians", "Palmeiras", "Fluminense",
    "América-MG", "São Paulo", "Grêmio", "Vasco da Gama", "Botafogo",
    "Sport Recife", "Cruzeiro", "EC Vitória", "Santos", "Chapecoense",
    "Atlético-PR", "Internacional", "Bahia", "Ceará SC", "Paraná"
)
print("=" * 20)
for i, t in enumerate(times[0:5]):
    print(f"Colocado número {i+1}: {t}")

print("=" * 20)
print("Últimos colocados:")
print("=" * 20)
for i, t in enumerate(times[-4:]):
    print(f"{i+1} : {t}")

print("=" * 20)

for indice, ordenados in enumerate(sorted(times)):
    print(f"Ordenado número {indice + 1} : {ordenados}")

print("=" * 20)

print(f"Time 'Chapecoense' está posição número {times.index("Chapecoense")}")

"""