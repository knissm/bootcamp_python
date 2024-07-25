#Imagine que você está trabalhando com dados de sensores IoT. 
#Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. 
# Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'
try:
    entrada = int(input("Temperatura atual: "))
    if entrada < 18:
        print(f"{entrada}° - Baixa")
    elif entrada >= 18 and entrada <=26:
        print(f"{entrada}° - Normal")
    else:
        print("Alta")
except ValueError:
    print("Por favor, verifique a entrada.")
except KeyboardInterrupt:
    print("Interrompido pelo usuario")