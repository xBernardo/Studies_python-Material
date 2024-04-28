lista = ["Lancer", "Golzin", "Celta", "Alfa Romeo"]
print(lista)

#lista.pop() #Remove o último ou um elemento pedido ex:(1)

#lista.remove("Lancer") #Remove o elemento que foi inserido!

#del lista #Deletou toda lista e não existe mais no terminal

#del lista[0] #Comando para deletar apenas um elemento da lista

#lista.clear() #função para limpar todos os elementos da lista

#lista.sort() #ordenação da lista por ordem alfabetica, também funciona com números! Importante lembrar]
#que os nomes em minusculos são imprimidos no final da lista.


#lista.sort(reverse = True) #ordena de foram decrescente a lista , também funcioan com números


for x in range(len(lista)):
    print(x, lista[x])