"""
7.	Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

"""

numeros = []
soma = 0
multiplicação = 1

for i in range(5):
    n = int(input(f'Digite o {i+1} número inteiro: '))
    soma += n
    numeros.append(n)
    multiplicação *= n 
    print("----------")
print(f'Os números são: ...')

for i in range(5):
    print(f'{i+1}º número: {numeros[i]}')
    print("----------")
 
    
print(f'A soma é {soma} e a multiplicação é: {multiplicação}')   


