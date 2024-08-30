""" DOCSTRINGS """
def contador(i,f,p):
    """
    Faz uma contagem e mostra na tela
    param i: inicio da contagem 
    param f: final da contagem
    param p:passo da contagem
    return: sem retorno
    """
    c = i
    while c <= f:
        print(f" {c}",end = "..")
        c +=p
    print('FIM!')


""" PARÂMETROS OPCIONAIS"""

def somar(a,b,c = 0):
    s = a + b + c
    print(f"A soma vale: {s}")


somar(1,2,97)


""" RETORNO DE VALORES """

def somar(a,b=0,c = 0):
    s = a + b + c
    return s

r1 = somar(1,2,3)
r2 = somar(5,1)
r3 = somar(1)

print(f'Os resultados foram: {r1}, {r2} e {r3} ')