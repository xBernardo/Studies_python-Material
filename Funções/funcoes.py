# Paradgma Imperativo
# Imperare

# Variaveis,a tribuições e sequência

marca = "Chevrolet" #variavel global


def carros():
    #bloco interno * bloco interno de uma função é conhecido como corpo da função
    marca = "Wolksvagen" # variável local
    tupla = 1, 3, 5, 7
    print(marca) 
    print(tupla)
    if marca == "Wolksvagen":
        print("Essa marca existe no seu script")
    for x in tupla:
        print(x)


carros()
print(marca)
