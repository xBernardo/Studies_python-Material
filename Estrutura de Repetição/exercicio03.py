# RESPOSTA

maior = int(input("Digite o número: "))
menor = maior

for x in range(2, 6):
    valor = int(input(f"Digite o {x}: "))
    if valor > maior:
            maior = valor

    elif valor < menor:
            menor = valor

print(f"O maior valor foi de: {maior}")
print(f"O menor valor foi de: {menor}")