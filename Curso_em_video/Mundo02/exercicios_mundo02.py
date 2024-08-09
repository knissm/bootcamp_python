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

#46
# Faça um programa que mostre na tela
# Uma contagem regressiva para o estouro e fogos de artifício,
# Indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
from time import sleep
for c in range(-10,0):
    print(c * -1)
    sleep(1)
print("BUM")
"""

#47
# Crie um programa que mostre na tela todos os números pares
# que estão no intervalo entre 1 e 50
"""
from time import sleep
for num in range(1,51):
    if num % 2 == 0:
        print(num)
        sleep(0.2)
"""

#48
# Faça um programa que calcule a soma entre todos os números impares
# que são múltiplos de três (3) e que se encontram no intervalo de 1 até 500.
"""
s = 0
for n in range(1,51):
    if n % 2 != 0: 
        if n % 3 == 0:
            s += n #s = s + n
print(f"Soma dos multiplos de 3: {s}")
"""

#49
#Refaça o desafio 009, mostrando a tabuada de um número
#que o usuário escolher, só que agora utilizando um laço for
"""
print("_" *25)
print("TABUADA")
print("_" *25)
numero = int(input("Digite um número: "))
for i in range(1,11):
    print(f"{i} x {numero} = {i*numero}")
"""

#50
#Desenvolva um programa que leia seis números inteiros
#e mostre a soma apenas daqueles que forem pares
#Se o valor digitado for ímpar, desconsidere-o.
"""
soma = 0
for i in range(1,7):
    numeros = int(input(f"Digite o {i}º número: "))

    if numeros % 2 == 0:
        soma+=numeros
print(soma)
"""

#53
#Crie um programa que leia uma frase qualquer
#E diga se ela é um palíndromo, desconsiderando os espaços
"""
frase = str(input("Digite uma frase: \n")).lower()
frase = "".join(frase.split(" "))
if frase == frase[::-1]:
    print(f"A frase {frase} é um palíndromo!")
else:
    print(f"A frase {frase} não é um palíndromo!")
"""
#54
#Crie um programa que leia o ano de nascimento de sete pessoas
#No final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores
"""
soma_maior = 0
soma_menor = 0
from datetime import date
ano_atual = date.today().year
for i in range(1,8):
    idades = int(input(f"Digite a idade da {i}° pessoa: "))
    if ano_atual - idades >=18:
        soma_maior += 1
    elif ano_atual - idades <= 17:
        soma_menor += 1

print(f"{soma_maior} já são maiores de idade.")
print(f"{soma_menor} ainda não são maiores de idade")
"""

#56
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa mostre:
# A media de idade do grupo
# Qual o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos.
"""
soma_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
menor_vinte = 0

for i in range(1,5):
    nome = str(input(f"Nome da {i}º pessoa: "))
    idade = int(input(f"Idade: "))
    sexo = str(input(f"Sexo (M/F): ")).lower()

    soma_idade += idade
    
    if i == 1 and sexo == 'm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo == 'm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    
    if sexo == 'f':
        menor_vinte += 1

    media_idade = soma_idade / 4

print(f"A Média de idade do grupo é: {int(media_idade)}")
print(f"O homem mais velho tem {maior_idade_homem} anos e e chama {nome_mais_velho}")
print(f"Menores de 20 e mulheres: {menor_vinte}")
"""

#57
#Faça um programa que leia o sexo de uma pessoa
#mas só aceite os valores "M" ou "F".
#Caso esteja errado, peça a digitação novamente
#até ter um valor correto.
"""
sexo = str(input("Digite seu sexo: ")).strip().lower()[0]
while sexo not in "mMfF":
    sexo = str(input("Entrada inválida. Digite M ou F: "))
    
if sexo == 'm' or sexo =='f':
    if sexo =='m':
        print("Entrada inserida com sucesso! Sexo Masculino!")
    elif sexo == 'f':
        print("Entrada inserida com sucesso! Sexo Feminino!")
print("Bye!")
"""

#59
#Crie um programa que leia dois valores e mostre um menu na tela:
# 1: somar
# 2: multiplicar
# 3: maior
# 4: novos números
# 5: sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

escolha = int(input(" 1: Somar \n 2: Multiplicar \n 3: Maior \n 4: Novos números \n 5: Sair do Programa \n "))

while escolha != 5:
    if escolha >5:
        print("ESCOLHA UMA DAS OPÇÕES ABAIXO!")
        escolha = int(input(" 1: Somar \n 2: Multiplicar \n 3: Maior \n 4: Novos números \n 5: Sair do Programa \n "))

    elif escolha <1:
        print("ESCOLHA UMA DAS OPÇÕES ABAIXO!")
        escolha = int(input(" 1: Somar \n 2: Multiplicar \n 3: Maior \n 4: Novos números \n 5: Sair do Programa \n "))

    elif escolha == 1:
        print("Você escolheu: SOMA")
        print(f"A Soma dos números {num1} e {num2} é: {num1 + num2}")
        print("")
        escolha = int(input(" 1: Somar \n 2: Multiplicar \n 3: Maior \n 4: Novos números \n 5: Sair do Programa \n "))
    
    elif escolha == 2:
        print("Você escolheu: MULTIPLICAR")
        print(f"A multiplicação do número {num1} com o número {num2} é: {num1 * num2} ")
        print("")
        escolha = int(input(" 1: Somar \n 2: Multiplicar \n 3: Maior \n 4: Novos números \n 5: Sair do Programa \n "))

    elif escolha == 3:
        print("Você escolheu: MAIOR")
        print(f"Entre os números{num1} e {num2}, o maior é: {max(num1,num2)} ")
        print("")
        escolha = int(input(" 1: Somar \n 2: Multiplicar \n 3: Maior \n 4: Novos números \n 5: Sair do Programa \n "))

    elif escolha == 4:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        escolha = int(input(" 1: Somar \n 2: Multiplicar \n 3: Maior \n 4: Novos números \n 5: Sair do Programa \n "))
print(". . . ENCERRANDO SISTEMA. . . ")
"""

#65
# Crie um programa que leia vários números inteiros pelo teclado
# No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continua = "s"
soma = 0
cnt = 0
maior = 0
menor = 0
while continua not in "nN":
    num = int(input("Digite um número: "))
    continua = str(input("Continuar a Digitar valores? "))[0]

    soma = soma + num #soma +=n
    cnt = cnt + 1 # cnt +=1
    media = soma / cnt

    if num > maior:
        maior = num
    if menor == 0:
        menor = num
    elif num < menor:
        menor = num

print(f"Soma dos números: {soma}")
print(f"Quantidade de números inseridos: {cnt}")
print(f"Media dos números inseridos: {media:.0f}")
print(f"Número mais baixo: {menor}")
print(f"Número mais alto: {maior}")
