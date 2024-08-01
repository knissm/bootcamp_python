"""
Desafio 036:
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar
o valor da casa, o salário do comprador e em 
quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 
30% do salario ou então o empréstimo será negado.
"""

"""
Desafio 037:
Escreva um programa que leia um número inteiro
qualquer e peça para o usuario escolher qual será a base de conversão:
1 para binário
2 para octal
3 hexadecimal
"""

"""
Desafio 038:
Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela
uma mensagem:
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais
"""

"""
Desafio 039:
Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com a idade:
Se ele ainda vai se alistar no serviço militar
Se é hora de se alistar
Se já passou do tempo de alistamento

O programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

"""
Desafio 040:
É aquele classico da média, não vou fazer
"""

"""
Desafio 041:
É bem de boa, não vou fazer
"""

"""
Desafio 042:
Não vou fazer agora
"""

"""
Desafio 043:
Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e 
mostre seu status, de acorod com a tabela abaixo:
Abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade mórbida 
"""

"""
Desfio 044:
Vou fazer na aula
"""

"""
Desafio 045:
Crie um programa que faça o computador jogar Jokenpô com você
"""
from random import choice

computador = choice(["Pedra", "Papel", "Tesoura"])
usuario = input("Pedra, Papel ou Tesoura?")

if computador == usuario:
    print("Acertou!!!!!")
else:
    print(f"Computador escolheu {computador}. Usuario escolheu {usuario}")
