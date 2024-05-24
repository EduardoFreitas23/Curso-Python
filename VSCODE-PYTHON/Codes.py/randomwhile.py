import random

numAlunos = 1
nomes = []

while numAlunos <= 4:
    nome = input('Informe o {}º aluno: '.format(numAlunos))
    nomes.append(nome)
    numAlunos += 1

random.shuffle(nomes)

print("O aluno sorteado é:", nomes[0])

#while 2 
import random

qnt = int(input('Quantos alunos você quer: '))
nmA = 1 
nomes = []

while nmA <= qnt:
    nome = input('Informe o {}º: '.format(nmA))
    nomes.append(nome)
    nmA += 1 

random.shuffle(nomes)

indice = 0
posicao = 1 

while indice < qnt and posicao <= qnt:
    print('O aluno {} está na posição: {}º'.format(nomes[indice], posicao))
    indice += 1 
    posicao += 1 