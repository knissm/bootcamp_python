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
"""
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
"""

# 82
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""
numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input("Digite um número: ")))
    flag = str(input("Deseja continuar? S/N: "))[0].lower().strip()
    if flag == 's':
        print("Continuando . . .")
    elif flag == 'n':
        break
    else:
        print("Entrada inválida! Digite S/N")

for i in numeros:
    if i % 2 ==0:
        pares.append(i)
    else:
        impares.append(i)

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
print(f"Lista completa: {numeros}")
"""

#84

# Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista.
# No final, mostre:

# a: quantas pessoas foram cadastradas.
# b: uma listagem com as pessoas mais pesadas
# c: uma listagem com as pessoas mais leves

# Obs.: Gerar uma lista com os mais leves e mais pesados
# Vai depender de analisar qual é o mais leve e o mais pesado.
# Se houver mais de um com esse peso, insere na lista.
# O mais normal é que a lista de mais pesados tenha apenas 1 pessoa,
# que é o motivo pelo qual a lista existe.
"""
entrada = []
dados = []
pesos = []
cnt = 0
while True:
    entrada.append(str(input("Nome: ")))
    entrada.append(int(input("Peso: ")))
    dados.append(entrada[:])
    entrada.clear()
    cnt +=1

    flag = str(input("Continua? S/N: "))[0].lower().strip()
    if flag =='n':
        break
    elif flag == 's':
        print("Continuando . . .")
    else:
        print('Entrada inválida. S/N para continuar')
print(dados)  

for i in dados:
    pesos.append(i[1])

pesos = sorted(pesos)

menor = pesos[0]
maior = pesos[-1]

# pessoas mais pesadas
mais_pesado = []
mais_leve = []

for i in dados:
    if i[1] == maior:
        mais_pesado.append(i[0])
    if i[1] == menor:
        mais_leve.append(i[0])


print(f"Pessoas cadastradas: {cnt}")
print(f"Maior peso {maior} kg do(a) {mais_pesado}")
print(f"Menor peso {menor} kg do(a) {mais_leve}")
"""

#85

# Crie um programa onde o usuário possa digitar
# sete valores numéricos
# e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares
# em ordem crescente.

"""
lista = [[],[]]

for i in range(0,10):
    entrada = int(input(f"Digite o número {i+1}:"))
    
    if entrada %2 == 0:
        lista[0].append(entrada)
    else:
        lista[1].append(entrada)

print(f"Lista completa: {lista}")
print(f"Lista com os números pares ordenados: {sorted(lista[0])}")
print(f"Lista com os números ímpares ordenados: {sorted(lista[1])}")
"""

#86

# Crie um programa que crie uma matriz 3.3
# e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela com a formatação correta

"""
entrada = []
lista = []

for i in range(0,3): #para cada linha
    for j in range(0,3): #para cada coluna em uma linha
        entrada.append(int(input("Número: ")))
    lista.append(entrada[:])
    entrada.clear()
print(lista)
"""

# 90
"""
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.

No final, mostre o conteúdo da estrutura na tela.
"""
"""
aluno = dict()

aluno['nome'] = str(input("Digite o nome do Aluno: "))
aluno['media'] = int(input("Digite a média do Aluno:"))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] < 7:
    aluno['situacao'] = "Em Recuperação"
else:
    aluno['situacao'] = 'Reprovado'

print(f"O aluno {aluno['nome']} possui média {aluno['media']}. Sua situação é {aluno['situacao'].upper()}")

# 91
"""

"""
Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.

No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado
"""
"""
from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'jogador 01': randint(1,6),
    'jogador 02': randint(1,6),
    'jogador 03': randint(1,6),
    'jogador 04': randint(1,6)
}

ranking = list()

print('Valores sorteados: ')
print('=' * 35)

for k, v in jogo.items():
    print(f"O {k} tirou {v} no dado")
    sleep(1)

ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True)
print(ranking)

for i,v in enumerate(ranking):
    print(f" {i+1} lugar: {v[0]} com {v[1]}.")
    sleep
"""

#92
"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de zero, o dicionário receberá também
o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.

Obs.: aposentadoria em 35 anos de contribuição.
"""
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input("Ano de Nascimento: "))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input("Carteira de Trabalho (0 não tem): "))


if dados['ctps'] != 0:
    dados['contratacao'] = int(input("Ano de contratação: "))
    dados['salario'] = float(input("Salário R$: "))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)

for k,v in dados.items():
    print(f" - {k} tem o valor de {v}")

#93
"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""

#94
"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.

No final, mostre:
a. Quantas pessoas foram cadastradas
b. A média de idade do grupo
c. uma lista com todas as mulheres
d. uma lista com todas as pessoas com idade acima da média.
"""

#95
"""
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes de aproveitamento 
de cada jogador.
"""