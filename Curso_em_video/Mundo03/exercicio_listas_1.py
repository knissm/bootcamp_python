lanche = ['hamburger','suco','pizza','picole']
lanche.append('cookie')
# APPEND adiciona no final

print(lanche)

lanche.insert(0,'cachorro quente')

# INSERT adiciona em uma posição especifico
print(lanche)

del lanche[3]
lanche.pop(3) # sem o número dentro do parenteses faz com que seja removido o ultimo elemento da lista

if 'pizza' in lanche:
    lanche.remove('pizza')


print(lanche)

valores = list(range(4,11))
print(valores)

valores.sort() # Ordena todos os valores
valores.sort(reverse = True) # Ordena todos os valores de forma reversa

print(len(valores))


##############################
num = [2,5,9,1]
num[2] = 3

print(num)

num.append(7) #adicionando ao final do elemento
print(num)

num.sort() # coloca em ordem
print(num)

num.sort(reverse = True) # coloca em ordem contrária
print(num)

print(f"Essa lista tem {len(num)} elementos")

num.insert(2,0) # insere na posição 2 o 0

num.pop() # elimina o ultimo valor
num.pop(2) # elimina o 2
num.remove(2) # procura do inicio da lista e a primeira ocorrencia do numero ele deleta


valores = [] # out list()
valores.append(5)
valores.append(9)
valores.append(4)

for valor in valores:
    print(f"{valor} . . ." , end =" ")


valores = list()

for i in range(0,5):
    valor = int(input(f"Digite o valor número {i+1}: "))
    valores.append(valor)

print(f"Os valores digitados foram: {valores}")