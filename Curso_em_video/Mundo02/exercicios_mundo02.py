"""
Desafio 036:
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar
o valor da casa, o salário do comprador e em 
quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 
30% do salario ou então o empréstimo será negado.

valor_casa = float(input("Valor da casa: "))
salario_comprador = float(input("Salario com comprador: "))
tempo_pagamento = int(input("Em quantos meses para pagar? "))

salario_parcela = salario_comprador * 0.3
tempo_pagamento_valor = salario_comprador//valor_casa

if tempo_pagamento_valor > salario_parcela:
    print("NEGADO!")
else:
    print("LIBERADO") 
"""

"""
Desafio 037:
Escreva um programa que leia um número inteiro
qualquer e peça para o usuario escolher qual será a base de conversão:
1 para binário
2 para octal
3 hexadecimal

numero = int(input("Digite um número: "))
print("***" *15)
print("")
print("Converter para Binário (Pressione a letra 'b')")
print("Converter para Octal (Pressione a letra 'o')")
print("Converter para Hexadecimal (Pressione a letra 'h')")
print("")
print("***" *15)
escolha = str(input("Oque você deseja fazer? - ")).lower()

if escolha == 'b':
    print(f"O número {numero} convertido para binário é: {bin(numero)}")
elif escolha == 'o':
    print(f"O número {numero} convertido para Octal é: {oct(numero)}")
elif escolha == 'h':
    print(f"O número {numero} convertido para Hexadecimal é: {hex(numero)}")
else:
    print("Você não digitou uma entrada válida!")

"""
    
"""
Desafio 038:
Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela
uma mensagem:
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais

num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))

if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}")
elif num2 > num1:
    print(f"O número {num2} é maior que o número {num1}")
elif num1 == num2:
    print(f"Não existe número maior ou menor. Os números {num1} e {num2} são iguais!")
"""
    
"""
Desafio 039:
Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com a idade:
Se ele ainda vai se alistar no serviço militar
Se é hora de se alistar
Se já passou do tempo de alistamento

O programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_atual = date.today().year

ano_nascimento = int(input("Em qual ano você nasceu? - "))
diff = ano_atual - ano_nascimento

if diff < 18:
    print(f"Você tem {diff} anos! Ainda faltam {18 - diff} anos para se alistar no serviço militar!")
elif diff == 18:
    print(f"Você tem {diff} anos. Vá se alistar no serviço militar!")
elif diff > 18:
    print(f"Você tem {diff} anos. Já passou {diff - 18} anos do alistamento!")
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
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/(altura * altura)

if imc < 18.5:
    print("Abaixo do Peso")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Obeso")
elif imc > 40:
    print("Obeso morbido")


"""
Desfio 044:
Vou fazer na aula
"""

"""
Desafio 045:
Crie um programa que faça o computador jogar Jokenpô com você

from random import choice

computador = choice(["Pedra", "Papel", "Tesoura"])
usuario = input("Pedra, Papel ou Tesoura?")

if computador == usuario:
    print("Acertou!!!!!")
else:
    print(f"Computador escolheu {computador}. Usuario escolheu {usuario}")
"""