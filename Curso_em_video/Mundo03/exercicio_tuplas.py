lanche = ("Hambúrger", "Suco", "Pizza", "Pudim")
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-1])
print(lanche[-2:])
print(lanche[-3])

print(lanche)
for c in lanche:
    print(f"Lanche: {c}")

for cont in range(0, len(lanche)):
    print(f"Vou comer {lanche[cont]} na posição {cont}")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")

print(sorted(lanche)) # mostra a tupla em ordenada

a = (2,5,4)
b = (5,8,1,2)
c = a + b #concatena tuplas
print(a)
print(b)
print(c)

print(len(c))
print(c.count(5))
print(c.index(2))
print(c.index(2,1))
pessoa = ("Marcelo", 31, "M", 90)
print(pessoa)
del(pessoa)
print(pessoa)