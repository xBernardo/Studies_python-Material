# Maiusculas e Minusculas 
# Simbolos e Espaços

"""
Security = chave
5ecur1ty = senha

hex

1 = 1
2 = 2
até 9 = 9
10 = A
11 = B
12 = C
13 = D
14 = E
15 = F

"""

chave = input("Digite a base da sua senha: ")

senha = ""

for letra in chave:
    if letra in "Aa":
        senha = senha + "10"
    elif letra in "Bb":
        senha = senha + "11"
    elif letra in "Cc":
        senha = senha + "12"
    elif letra in "Dd":
        senha = senha + "13"
    elif letra in "Ee":
        senha = senha + "14"
    elif letra in "Ff":
        senha = senha + "15"
    elif letra in "Rr":
        senha in senha + "."
    elif letra in "Ss":
        senha in senha + ">"
    elif letra in "Tt":
        senha in senha + "<"
    else:
        senha = senha + letra
print(senha)
        