"""
4.	Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
Imprima as consoantes.
"""
vogais = ['a','e','i','o','u']
#consoantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

consoantes = []

for i in range(10):
    v = (input(f'Digite as consoantes: ')).lower()

    if len(v) == 1 and v.isalpha() and v not in vogais:
     consoantes.append(v)
     
print('----------')

print('A quantidade de consoantes é igual a: ',len(consoantes))


