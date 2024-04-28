"""
Como achar o fatorial de um número
"""
numero = int(input("Insira um número: "))

fatorial = 1

if numero < 0:
    print("Não existe mano infelizmente!")                        
elif numero == 0:
    print(f"O fatorial de {numero} é 1")                           #Lembrando oq é range
else:                                                                  
    for x in range(1, numero + 1):                     # for x in range(1,9)
        fatorial = fatorial * x                        #     print(x)     Este resultado vai de 1 a 8
    print(f"O fatorial de {numero} é: {fatorial}")





