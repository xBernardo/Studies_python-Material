#Função Input() - Função para receber dados do usuario
#1ª Forma
"""
print("Qual seu nome")
nome = input()
print("Olá, " +nome)

idade = input("Qual sua idade? ")
print("Que bom você tem," +idade)
"""

#2ª Forma
"""
nome = input("Qual é o seu nome? ")
idade = input("Qual sua idade? ")

print("Seu nome é: {0} e Sua idade é {1}" .format(nome,idade))
"""

#3ª Forma

nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")

print(f"Seu nome é: {nome} e sua idade é: {idade}")