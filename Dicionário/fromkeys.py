#                  Criando dicionarios apertir de dicionarios ou tuplas


tupla = ("Gol", "Palio", "Celta")

dicio = dict.fromkeys(tupla, )
print(dicio)

dicio = {
    "dicio1" : {
        "Modelo": "Uno",
        "Ano" : "2008"
    },
    "dicio2" :{
        "Modelo": "Polo",
        "Ano" : "2010",
        "dicio3" :{        # Dicionario dentro de outro dicionario
            "Marca" : "VW",
            "Motor" : 10
        }
    }
}

print(dicio)