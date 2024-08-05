for c in range(1,6):
    print(c)
print("Fim")
#################
for c in range(-1,6):
    print(c)
print("Fim")
#################
for c in range(0,7,2):
    print(c)
print("Fim")

n = int(input("Digite um numero: "))
for c in range(0, n+1):
    print(c)
print("Fim")

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for c in range(i, f+1, p):
    print(c)
print("Fim")

#####################

s = 0
for c in range(0,4):
    n = int(input("Digite um valor: "))
    s = s+n
print(f"Somatorio: {s}")