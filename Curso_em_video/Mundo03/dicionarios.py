tupla = () 
lista = []
dicionario = {}

dados = {'nome': 'pedro'}
print(dados['nome'])

filme = {
    'titulo':"Star Wars",
    'ano':1977,
    'diretor':'George Lucas'
}

print(filme.values())
print(filme.keys())
print(filme.items())

for k,v in filme.items():
    print(f"O {k} é {v}")
print('Fim do laço')

pessoas = {
    'nome':'Marcelo',
    'sexo':'Masculino',
    'idade':'21'
}
del pessoas['sexo']

print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

for k,v in pessoas.items():
    print(k,v)

estado1 = {'uf':'Rio de Janeiro', 'sigla':"RJ"}
estado2 = {'uf':'São Paulo', 'sigla':"SP"}

brasil = []

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estado = {}
brasil = []

for i in range(0,3):
    estado['uf'] = str(input("UF: "))
    estado['sigla'] = str(input("Sigla: "))
    brasil.append(estado.copy())

for e in brasil: #esse for é da lista
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}", end = " ") 
        print()



