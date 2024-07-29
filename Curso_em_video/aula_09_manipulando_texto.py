""" Curso Python #09 - Manipulando Texto """
############################################################

frase = "Curso em Video Python"

"""Fatiamento: Pegar pedaços de uma string"""
print(frase[9]) # Pega somente a letra 9 da string  ("V")
print(frase[9:13]) #Pega do indice no 9 até o indice 12 (o 13 ele exlui)
print(frase[9:21]) #Fatiará do 9 ao 20
print(frase[9:21:2]) #Começo no 9, termino no 20, pulando de 2 em 2
print(frase[:5]) #Antes dos : é onde ele vai começar, depois dos : é onde ele vai terminar (lembrando que acaba no indice anterior)
print(frase[15:]) #Indiquei o inicio, mas não indiquei o final.
print(frase[9::3]) #Vai começar no 9, vai até o final, porém pulando de 3 em 3

"""Analisando uma string"""
print(len(frase)) #len() - tamanho da string
print(frase.count('o')) #count() - contar quantas vezes existe uma determinada letra (nesse caso o 0)
print(frase.count('o',0,13)) #count() - contar quantas vezes existe uma determinada letra (nesse caso o 0). Porém irá considerar um inicio e fim
print(frase.find('deo')) #find() - diz em qual posição começará a string
print(frase.find("Android")) #Se retornar -1 significa que não foi encontrado

tem_palavra = 'Curso' in frase
print(tem_palavra)

"""Transformação de uma string"""
print(frase.replace("Python", "Andoid")) #Vai procurar a palavra Python e substituir por Android
print(frase.upper()) # Deixa o texto em maiúscula
print(frase.lower()) #Deixa tudo minúsculo
print(frase.capitalize()) #Somente o primeiro caractere em maiúsculo
print(frase.title())


