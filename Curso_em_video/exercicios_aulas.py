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
#Desagio 24:
"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO"""
"""
RESOLUÇÃO
nome_cidade = input("Digite o nome de uma cidade: ")
nome_cidade_limpo = nome_cidade.lower()

if "santo" in nome_cidade_limpo:
    print(f"A cidade {nome_cidade} contém SANTO em seu nome!")
else:
    print(f"A cidade {nome_cidade} não contém SANTO em seu nome")
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
nome_completo = input("Digite seu nome completo: ").title()
lista = nome_completo.split(" ")
print(f"Primeiro nome: {lista[0]}")
print(f"Último nome: {lista[-1]}")