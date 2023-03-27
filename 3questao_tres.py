import json
with open("dados.json") as arq_json:
    dados = json.load(arq_json)
novo_dicionario = []
for dicionario in dados:
    if dicionario["valor"] == 0:
        pass
    else:
        novo_dicionario.append(dicionario)

dia_maior = 0
valor_maior = novo_dicionario[0]["valor"]
dia_menor = 0
valor_menor = novo_dicionario[0]["valor"]
dias_zerados = 0
fat_total = 0
for dicionario in novo_dicionario:
    valor = dicionario["valor"]
    fat_total += valor
    if valor > valor_maior:
        valor_maior = valor
        dia_maior = dicionario["dia"]
    elif valor < valor_menor:
        valor_menor = valor
        dia_menor = dicionario["dia"]
med = fat_total / len(novo_dicionario)

print(f"O dia com maior lucro foi o dia {dia_maior} com R${valor_maior} em faturamento")
print(f"O dia com maior lucro foi o dia {dia_menor} com R${valor_menor} em faturamento")
print(f"A média de faturamento do mês foi R${med:.4f}")
print("==="*23)
print("Os dias em que estivemos acima da média de vendas foram:")
for dicionario in novo_dicionario:
    if dicionario["valor"] > med:
        print(f"Dia {dicionario['dia']} com R${dicionario['valor']} em faturamento")
