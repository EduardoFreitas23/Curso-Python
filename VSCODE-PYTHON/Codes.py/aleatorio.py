import random

n1 = input('Informe o primeiro aluno: ')
n2 = input('Informe o segundo aluno: ')
n3 = input('Informe o terceiro aluno: ')
n4 = input('Informe o quarto aluno: ')

ale1 = [n1, n2, n3, n4]

alea = random.choice(ale1)

print('O aluno escolhido foi: {}'.format(alea))