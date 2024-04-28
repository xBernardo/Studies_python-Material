
#Argumento Arbitrário **Kwargs - Keyword Arguments
# Essa função recebe argumentos que serão atribuidos em um dicionário

def imprimir_nomes(**nomes):
    print(f"{nomes ["nomes"]} {nomes["sobrenome"]}")


imprimir_nomes(nomes="Rodrigo", sobrenome="Silva")