n1 = int(input('Digite a tabuada do: '))
n2 = int(input('Digite o valor máximo da tabuada: '))
n3 = int(input('Informe o começo: '))
n4 = int(input('Pulo: '))

count = n3

while count <= n2:
    mult = n1 * count
    print('{} X {} = {}'.format(n1, count, mult))
    count = count + n4