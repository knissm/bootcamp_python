tupla = () 
lista = []
dicionario = {}
"""
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
"""
""" 
Cadastro de Estudantes: Crie um dicionário para armazenar informações de estudantes. 
As chaves devem ser os nomes dos estudantes, e os valores devem ser as idades. 
Adicione pelo menos três estudantes ao dicionário e depois imprima as idades deles. 
"""
estudantes = []

for i in range(0,3):
    estudante = {}
    estudante['nome'] = str(input("Nome do Estudante: "))
    estudante['idade'] = int(input("Idade do Estudante: "))
    estudantes.append(estudante.copy())
    #estudante.clear()

for lista in estudantes:
    for k, v in lista.items():
        print(f"{k} : {v}")

