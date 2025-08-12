"""
5.	Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

"""
numeros = []
vetorpar = []
vetorimpar = []

for i in range(5):
    n = int(input(f'Digite o {i+1}º número: '))
    numeros.append(n)
    print('----------')

    if n % 2 != 0:
      vetorimpar.append(n)
    else:
      vetorpar.append(n)
    
print('Números pares: ',vetorpar)
print('----------')
print('Números impares: ',vetorimpar)
print('----------')
print('Todos os números: ',numeros)