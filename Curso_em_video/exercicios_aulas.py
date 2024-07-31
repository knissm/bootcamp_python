#Desafio 22:
""" Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maisuculas 
O nome com todas as letras minusculas
Quantas letras ao todo (sem considerar os espaços)
Quantas letras tem o primeiro nome"""

"""
RESOLUÇÃO

nome_completo = input("Digite seu nome completo: ")
nome_cortado = nome_completo.split(" ")
nome_junto = "".join(nome_cortado)
print(f"Nome Minúsculo: {nome_completo.lower()}")
print(f"Nome Maiúsculo: {nome_completo.upper()}")
print(f"Total de Letras sem considerar os espaços: {len(nome_junto)}")
print(f"Quantidade de Letras Primeiro Nome: {len(nome_cortado[0])}")
"""


#Desafio 23:
""" Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex:
Digite um numero: 1834
unidade: 4
dezenas: 3
centenas: 8
milhar:1
"""
"""
num = int(input("Digite um numero: "))
u = num // 1 % 10
d = num //10 % 10
c = num //100 % 10
m = num //1000 % 10
print(f"Anlisando o número {num}")
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")
"""

#Desagio 24:
"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO"""

"""
#RESOLUÇÃO
nome_cidade = input("Digite o nome de uma cidade: ").strip()
print(nome_cidade[:5].lower() == "santo")

"""

#Desafio 25:
"""Crie um programa que peça o nome de uma pessoa e diga se ela tem silva no nome"""

"""
RESOLUÇÃO

nome = input("Digite seu nome completo: ").lower()

if "silva" in nome:
    print(f"O nome {nome.title()} contém silva!")
else:
    print(f"O nome {nome.title()} não contém silva no nome")
"""

#Desafio 26:
"""Crie um programa que leia uma frase e mostre:
Quantas vezes aparece a letra "A":
Em qual posição aparece a letra "A" pela primeira vez
Em que posição aparece ela pela ultima vez"""

"""RESOLUÇÃO
frase = input("Digite uma frase: ").lower()


print(f"A letra 'A' aparece na frase {frase.count("a")} vezes")
print(f"A primeira aparição da letra 'A' é no índice {frase.find('a')}")
print(f"A ultima posição da letra 'A' é no índice n° {frase.rfind('a')}")
"""

#Desafio 27:
"""Faça um programa que peça o nome de uma pessoa, mostrando seguido o primeiro nome e o ultimo nome separadamente
Ex: Marcelo Augusto Kniss
primeiro: Marcelo
ultimo: Kniss"""
"""
RESOLUÇÃO
nome_completo = input("Digite seu nome completo: ").title()
lista = nome_completo.split(" ")
print(f"Primeiro nome: {lista[0]}")
print(f"Último nome: {lista[-1]}")
"""

###########################################################################################################

#Desafio 28:
"""Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuario
tentar adivinhar qual foi o numero escolhido pelo computador. O programa devera escrever na tela se o usuario
acertou ou errou
"""
print("Olá")

# Desafio 29:
""" Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7.00 por cada km acima do limite"""
"""
velocidade = int(input("Analisando a velocidade. . . "))
diferenca = velocidade - 80

if velocidade > 80:
    print("VOCÊ FOI MULTADO POR EXCESSO DE VELOCIDADE!")
    print(f"Valor da multa: R${diferenca * 7} reais ")
else:
    print(f"Velocidade atual: {velocidade} km/h")
"""

#Desafio 30:
"""Crie um programa para dizer se o numero digitado é par ou impar"""
"""
numero = int(input("Digite um número: "))
resultado = numero % 2

if resultado == 0:
    print(f"O número {numero} é par!")
else:
    print(f"O número {numero} é ímpar")
"""    

#Desafio 31:
"""
Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço
da passagem cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas
"""
"""
distancia = int(input("Distância percorrida . . ."))
if distancia <= 200:
    print(f"Você percorreu {distancia} km")
    print(f"Valor da corrida: {distancia * 0.50}")
else:
    print(f"Você percorreu {distancia} km")
    print(f"Valor da corrida: {distancia * 0.45}")
"""

#Desafio 32:
"""Faça um programa que diga se o ano é bissexto ou não"""

#Desafio 33:
"""Faça um programa que leia 3 numeros e diga qual o maior e qual o menor"""

#Desafio 34:
"""Calcular o aumento de um usuario. se ele ganha até R$1.250,00 calcular um aumento de 10%. Para inferiores ou iguais, 
aumento de 15%"""

#Desagfio 35:
"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triangulo."""
num1 = int(input(f"Digite o primeiro número: "))
num2 = int(input(f"Digite o segundo número: "))
num3 = int(input(f"Digite o terceiro número: "))

if num1 == num2 == num3:
    print(f"Os números {num1}, {num2} & {num3} formam um triângulo.")
else:
    print(f"Os números {num1}, {num2} & {num3} não formam um triângulo.")