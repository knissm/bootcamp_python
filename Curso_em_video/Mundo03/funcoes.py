"""
def mostraLinha():
    print('-' * 30)


mostraLinha()
print("Curso")
mostraLinha()
"""

"""
def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


titulo("Olá")
"""

"""
def soma(a,b):
    s = a + b
    print(s)


soma(4,6)
"""

"""
def soma(a,b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f" A soma A+B é {s}")

soma(4,5)
"""

"""
def contador(* num):
    tam = len(num)
    print(tam)

contador(1,2,3)
"""

"""
def dobra(lst):
    pos = 0
    while pos <len(lst):
        lst[pos] *= 2
        pos +=1


valores = [7,2,5,0,4]
dobra(valores)
print(valores)
"""

def soma(* valores):
    s = 0
    for num in valores:
        s +=num
    print(s)


soma(2,1,5)