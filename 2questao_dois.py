numero = int(input("Qual o valor que você deseja encontrar?: "))
ind1 = 0
ind2 = 1
fibo = [0, 1]
while True:
    if numero in fibo:
        print(f"O número {numero} se encontra na sequência de Fibonacci")
        break
    elif numero < fibo[-1]:
        print(f"O número {numero} não se encontra na sequência de Fibonacci")
        break
    else:
        valor = fibo[ind1] + fibo[ind2]
        fibo.append(valor)
        ind1 += 1
        ind2 += 1
