#Measure some strings
"""
words = ['cat','window','defenestrate']
for w in words:
    print(w,len(w))
"""
#Measure some strings
#Contagem de Palavras em Textos.
# Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
"""
texto = "a raposa marrom salta sobre o cachorro preguiçoso"
palavras = texto.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] +=1
    else:
        contagem_palavras[palavra] = 1
print(contagem_palavras)
"""
#Normalização de Dados. Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.
"""
numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
for i in numeros:
    normalizados = (i - minimo) / (maximo - minimo)
    print(normalizados)
"""
#Filtragem de Dados Faltantes. 
# Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.
"""
usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

for usuario in usuarios:
    if usuario["email"]:
        print(usuario)
"""
#Extração de Subconjuntos de Dados.
# Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.
"""
numeros = range(1,50)

for i in numeros:
    if i%2 == 0:
        print(i)
"""
#Agregação de Dados por Categoria. 
# Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
"""
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

print(total_por_categoria)
"""