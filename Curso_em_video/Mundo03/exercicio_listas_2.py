pessoas = [['pedro',25],['marcelo',31],['josé','21']]
print(pessoas[0])
print(pessoas[1])
print(pessoas[2])
totmaior = totmenor = 0

for i in pessoas:
    print(f'{i[0]} tem {i[1]} anos')

pessoas = []
dado = []

for c in range(0,3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    pessoas.append(dado[:])
    dado.clear()

for i in pessoas:
    if i[1] >=21:
        print(f" {i[0]} é maior de idade!")
        totmaior += 1
    else:
        print(f" {i[0]} é menor de idade!")
        totmenor += 1

print(f"Maiores de idade:  {totmaior} e menores de idade: {totmenor}")