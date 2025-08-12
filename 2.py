"""
2.	Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

"""

lista = []

for i in range(3):
    l = float(input(f'Digite o {i+1}º número da lista: '))

    lista.append(l)

lista.reverse()
print('----------')


print(lista)