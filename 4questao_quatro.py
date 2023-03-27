valores = {"sp": 67836.43, "rj": 36678.66, "mg": 29229.88, "es": 27165.48, "outros": 19849.53}
cem_pc = 0
for valor in valores:
    cem_pc += valores[valor]
teste = 0
for valor in valores:
    porc = (valores[valor] / cem_pc) * 100
    teste += porc
    print(f"O estado de {valor} representa {porc}% dos valores")
