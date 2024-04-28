
# Argumentos arbritrários *args - guarda argumntos dentro de uma tupla

def imprimir_imovel(nomeImovel, n_quartos, vagaGaragem=None, *telefone):
    print("------------------")
    print("Título: ", nomeImovel)
    print("Quartos: ", n_quartos)
    if vagaGaragem != None:
        print("Vagas na garagem: ", vagaGaragem)
    print("Telefones: ", telefone)

imprimir_imovel("Loja Comercial", 2, 5, "81 99792-8245", "81 9587-1234")


"""def imprimir_nomes(*nomes):
    print(nomes)


imprimir_nomes("Rodrigo", "Bernardo", "Silva") # Argumentos que vão imprimir uma tupla"""

