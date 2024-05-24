import random

print('--------------------------------------------------')
while True:
    try:
        qnt = int(input('Informe quantos aluno você quer inserir: '))
        print('--------------------------------------------------')
        break  # Se a entrada for válida, sai do loop
    except ValueError:
        print("Por favor, insira um número inteiro.")

numAlunos = 1
nomes = []

while numAlunos <= qnt:
    nome = input('Informe o {}º aluno: '.format(numAlunos))
    nomes.append(nome)
    numAlunos += 1

random.shuffle(nomes)

ordem = "Ordem de apresentação"

print('--------------------------------------------------')
print('{:-^50}'.format(ordem))
print('--------------------------------------------------')

indice = 0
posicao = 1

while indice < qnt and posicao <= qnt:
    print("O {}º aluno é: {}".format(posicao, nomes[indice]))
    indice += 1
    posicao += 1

print('--------------------------------------------------')
'''

print("O primeiro é:", nomes[0])
print("O segundo é:", nomes[1])
print("O terceiro é:", nomes[2])
print("O quarto é:", nomes[3])'''

'''

import random

numAlunos = 1
nomes = []

while numAlunos <= 4:
nome = input('Informe o {}º aluno: '.format(numAlunos))
nomes.append(nome)
numAlunos += 1

random.shuffle(nomes)

print("O aluno sorteado é:", nomes[0])

import random

n1 = input('Informe o primeiro aluno: ')
n2 = input('Informe o segundo aluno: ')
n3 = input('Informe o terceiro aluno: ')
n4 = input('Informe o quarto aluno: ')

lista = [n1, n2, n3, n4]

escolhido = random.choice(lista)

print(escolhido)

'''

# vezes = int(input('Quantas vezes você quer repetir? '))

# count = 0

# while count < vezes:
#     count = count + 1
#     primeiroNumero = float(input('Informe um numero: '))
#     segundoNumero = float(input('Informe outro numero: '))

#     soma = primeiroNumero + segundoNumero

#     print('A soma dos dois números é: {} '.format(soma))

# first_senha = int(input('Informe a senha: '))

# while first_senha != 2002:
#     print('Senha Inválida. ')
#     second_senha = int(input('Informe a senha: '))
#     first_senha = second_senha

# print('Senha Válida')
