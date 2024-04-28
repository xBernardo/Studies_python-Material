"""
Comandos if,else e elif ->(else if)

"""
"""
x = 3
y = 3

if y > x:
    print("y é maior do que x")  
elif y < x:
    print("y é menor do que x")
elif y == x:
    print("y é igual a x")

print("Fora do bloco")
print(y>x)
print(y<x)
print(y==x)

"""
a = 5 
b = 3
c = 2

# if b > a: print("A é maior que A")
# print("Fora do bloco")
    
# print("B") if b < a else print("A")  #Operador ternário, Expressões Condicionais

if a > b:
    print("A maior que B")
    if a > c:
        print("A maior C")