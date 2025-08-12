"""
3.	Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

"""
"""
Outra forma de fazer:

n1 = int(input('Digite a primeira nota'))
n2 = int(input('Digite a segunda nota'))
n3 = int(input('Digite a terceira nota'))
n4 = int(input('Digite a quarta nota'))

print('Nota 1 =>', n1)
print('Nota 2 =>', n2)
print('Nota 3 =>', n3)
print('Nota 4 =>', n4)

media = (n1+n2+n3+n4)/4

print('A média calculada é =>', media)

if media >=7:
    print('Situação Aprovado')
elif media >4 and media <7:
    print('Em Recuperação')
else:
    print('Reprovado')

    """
media = 0
soma = 0
notas = []

for i in range(4):
    n = int(input(f'{i+1}ª nota: '))
    notas.append(n)
    print('----------')
    soma += n

media = soma / 4

print(f'As notas são: {notas}, E a média das notas é igual a: {media}')



