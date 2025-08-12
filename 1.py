"""
1.	Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

"""
#Criando a lista

lista = []

#Varrer a lista para 5 números

for i in range(6):
    l = int(input(f'Digite o {i+1}º número da lista: '))

#Gravando números na lista
    lista.append(l)
print('----------')

#Imprimir o conteúdo da lista    

for i in range(6):
    print(f'Posição -> {i} na lista, é equivalente a: {lista[i]}')

print('----------')
print(f'Sequência de números: {lista}')
print('----------')

"""
Neste caso foi utilizado o for justamente para mostrar não só o número, mas também em que
posição da lista ele se encontra.
"""