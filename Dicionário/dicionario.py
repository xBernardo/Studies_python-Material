
#            COLEÇÃO NÃO ORDENADA, MUTÁVEL E QUE NÃO PERMITE VALORES DUPLICADOS

#chave:valor
dicio = {"Chave", "Rodrigo", "Chave2", 5, True, 3.0}
print(dicio)

carros = {
    "Marca": "Mitsubishi",
    "Modelo": "Lancer",
    "Nacionalidade": "Japones"
}

print(carros)

print(carros["Marca"])

print(carros.get("Modelo"))

print(carros.keys()) #Puxa todas chaves que foram inseridas nos carros

print(len(carros))

print(carros.values()) #Puxa toda os valores que foram inseridos nos carros

if "Marca" in carros:
    print("A chave marca existe")
else:
    print("Não existe")

print(carros.items()) #Puxa Valores de uma tupla dos carros
