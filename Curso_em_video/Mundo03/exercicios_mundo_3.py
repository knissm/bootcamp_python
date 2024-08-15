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

# 74
# Crie um programa que vai gerar cinco números aleatórios 
# e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados
# e também indice o menor e o maior valor que estão na tupla

""" 
COM FOR 

numeros = []

from random import randint

for i in range (0,5):
    numeros.append(randint(0,999))

numeros_tupla = tuple(numeros)

print(f"Tupla Gerada: {numeros_tupla}")
print(f"O maior número da tupla é o {max(numeros_tupla)} e menor número é o {min(numeros_tupla)}")

"""
"""
COM WHILE
from random import randint
numeros = []
n = 1
while n <6:
    numeros.append(randint(1,99))
    n += 1

tupla = tuple(numeros)

print(f"Valores da Tupla: {tupla}")
print(f"Maior valor: {max(tupla)}")
print(f"Menor valor: {min(tupla)}")
"""

# 75
# Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. # No final, mostre:

# a) quantas vezes apareceu o valor 9
# b) em que posição foi digitado o primeiro valor 3
# b) quais foram os números pares
"""
n_tupla = []
for i in range(1,5):
    n = int(input(f"Digite o número {i}: "))
    n_tupla.append(n)

n_tupla = tuple(n_tupla)

# Quantas vezes aparece o número 9?
print(f"O Número 9 apareceu {n_tupla.count(9)} vezes")

# Em que posição foi digitado o primeiro valor 3
if 3 in n_tupla:
    print(f"O Primeiro valor 3 foi digitado no espaço de memória nº {n_tupla.index(3)}")
else:
    print("Não foi digitado nenhum número 3")
# Quais foram os números pares ?
pares = []
for num in n_tupla:
    if num % 2 == 0:
        pares.append(num)
print(f"Números Pares: {pares}")
"""