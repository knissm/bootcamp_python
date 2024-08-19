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

# 76

# Crie um programa que tenha uma tupla única
# com nomes de produtos e seus respectivos precos,
# na sequência

# No final, mostre uma listagem de precos,
# organizando os dados em forma tabular

"""
listagem = (
    "pão", 1,
    "leite", 3.50,
    "frango", 10.90,
    "Arroz",19.90
)
produto = -2
valor = -1

for i in range(0,len(listagem) //2 ):
    produto += 2
    valor += 2
    print(f"{listagem[produto].capitalize()} ... R$ {listagem[valor]}")
"""

# 77

#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

"""
tupla = (
    "Marcelo", "Luthien Tinuviel", "Erik Killmonger", 
    "Kendrick Lamar", "Charlotte Galves", "Roberta Pires", "Amanda", "hue"
    )

vogais = ["a","e","i","o","u"]



for nome in tupla:
    nome = str(nome).lower()
    lista = []
    
    for letra in nome:
       for i in vogais:
            if letra == i:
                lista.append(letra)

    print(f"{nome.capitalize()}: {len(lista)} vogais")
"""

# 78
# Faça um programa que leia 5 valores números e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitados e as suas respectivas posições na lista.

"""
valores = []
maior = menor = 0
pos_maior = []
pos_menor = []
n = 0

while n < 5:
    valores.append(int(input(f"Digite o {n+1}° valor: ")))
    n+=1

maior = max(valores)
menor = min(valores)

print("Os valores digitados são: ")
for index,val in enumerate(valores):
    if val == maior:
        pos_maior.append(index)
    if val == menor:
        pos_menor.append(index)

    print(f" Número {index+1}: {val}")

print(f"O maior número é o número {maior} e sua posição é {pos_maior}")
print(f"O menor número é {menor} e sua posição é {pos_menor}")
"""

# 79

#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.

#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
numeros = []

while True:
    entrada = int(input("Digite um número: "))
    if entrada in numeros:
        print(f"O número {entrada} já conta na lista.")
    else:
        numeros.append(entrada)
        print("Adicionado com sucesso!")

    keep = str(input("Deseja continuar? [S/N]: "))
    if keep[0] == 'n':
        break
    if keep[0] =='s':
        print("Continuando..")
    else:
        print("Entrada inválida! Digite [S/N]: ")

print(sorted(numeros))
"""

# 81

# Crie um programa que vai ler vários números e colocá-los em uma lista
# Depois disso, mostre:
# a) quantos números foram digitados.
# b) a lista de valores, ordenada de forma decrescente
# c) se o valor 5 foi digitado e está ou não na lista.
numeros = []
while True:
    numeros.append(int(input("Digite um número: ")))    
    flag = str(input("Deseja continuar? [S/N]: "))[0].lower().strip()
    if flag == 's':
        print('Continuando . . .')
    elif flag == 'n':
        break
    else:
        print("Entrada invalida. Digite [S/N]")

numeros.sort(reverse = True)

print(f"Foram digitados {len(numeros)} números!")
print(f"Os números em forma reversa são: {numeros}")

if 5 in numeros:
    print(f"O número 5 foi digitado.")
else:
    print("O número 5 não foi digitado nem uma vez")