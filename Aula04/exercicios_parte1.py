# typing, listas e dicionário
#O Python é uma linguagem dinamica, forte
"""
1- Type Hint 
ele ajuda o desenvolvedor a se comunicar melhor
assim a gente sabe oque a variavel
foi criada para aquele proposito (Hint)
"""
"""
idade: int = 30
altura: float = 1.75
nome: str = "Marcelo"
is_estudante: bool = True
"""

#LISTAS 
"""

produto: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "videogame"

produtos: list = []
produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)

produtos.pop() #tira o ultimo produto que entrou
#produtos.remove(produto_3) #ou escolhe o item a tirar

print(produtos)
"""

# DICIONARIOS
nome = "sapato"
quantidade = 39
preco = 10.38,
disponibilidade = True
"""
dicionario = {
    "nome":"sapato",
    "quantidade":39,
    "preco":10.38,
    "disponibilidade":True
}
"""
#Crie um dicionario para armazenar informações de um livro,
#incluindo titulo, autor e ano de publicação. Imprima cada informação.
"""
from typing import Dict, Any

livro1: dict[str, Any] = {
    "Titulo":"Game of Thrones",
    "Autor":"N/A",
    "Ano":2005
}

livro2: dict[str, Any] = {
    "Titulo":"Game of Thrones2",
    "Autor":"N/A",
    "Ano":2005
}

lista_elementos:list = livro1.items()

for elemento in lista_elementos:
    print(elemento)
"""