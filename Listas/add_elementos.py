#index    [0,        1,         2]
lista = ["Lancer", "Golzin", "Celta"]
print(lista)

#lista.append("HR-V") #não pode adicionar mais de um elemento no argumento
#lista.append(["HR-V", "Tracker", "Renegade", "Prisma"]) #neste modo pode adcionar mais elementos na lista

lista.insert(1, "Renegade") #adicionando elementos definindo qual luagr ele vai ser colocado
print(lista)

#lista.append(["HR-V", "Renegade"]) 
lista.extend(["HR-V", "Palio"]) #Insere elementos na lista sem outra lista dentro []

print(lista)
print(len(lista))

for x in range(len(lista)):
    print(x, lista[x])



"""texto = "O carro mais rápido do mundo, é o:"
lista2 = list(texto)
print(lista2)

texto = texto.split('') #função que retira do texto oq foi inserido dentro das aspas
print(texto)"""