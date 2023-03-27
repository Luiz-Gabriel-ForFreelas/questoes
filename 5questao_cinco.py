frase = str(input("Digite a frase: "))
letra_fim = ""
for val in range(len(frase) -1, -1, -1):
    letra_fim += frase[val]
print(letra_fim)