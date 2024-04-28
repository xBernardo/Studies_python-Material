
#        COLEÇÃO ORDENNADA, MUTÁVEL E QUE PERMITE VALORES DUPLICADOS

nome = ["Rodrigo", "Bernardo", "Silva"]
print(nome)

nome1 = [1, 3, 5, 7, 9]
print(nome1)

nome2 = [1.4, 2.3, 5.2, 7.5]
print(nome2)

nome3 = [True, False]
print(nome3)

nome4 = ["Rodrigo", False, 3.1, 5, True]
print(nome4)


print(nome4[-2]) # o numero negattivo volta para o final da fila


print(nome4[::]) # retora todos os elementos da lista
print(nome4[1:]) # retorna do 1 ao fim da lista 
print(nome4[:2]) # retorna do começo da lista até o -1 (primeiro e último)
print(nome4[1:4]) # retorna do numero pedido até o -1
print(nome4[1:4:2])
