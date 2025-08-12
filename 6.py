"""
6.	Faça um Programa que peça as quatro notas de 3 alunos, calcule e armazene num vetor a média de cada 
aluno, imprima o número de alunos com média maior ou igual a 7.0.

"""
media = []
soma = media = nota = 0

for i in range(3): #3 alunos
    for j in range(4): #4 notas para cada aluno
        nota = float(input(f'Digite a {j+1}ª nota do {i+1} Aluno: '))
        soma += nota
        print("----------")
    m = soma / 4
    media.append(m)
    soma = 0
    print("----------")
