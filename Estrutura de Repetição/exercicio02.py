#                                 Verificando Sinal Numérico

num = int(input("Digite um número: "))

if num > 0:
    print(f"O {num} é positivo!")
elif num == 0:
    print(f"O {num} é neutro!")
else:
    print(f"O {num} é negativo!")