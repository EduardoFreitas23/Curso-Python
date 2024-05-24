#1-Criar uma variavel do número de sua escolha
#2-Criar uma variavel do número até onde ele vai multiplicar
#3-Contador = -1 pra começar a partir do 0
#4-Criar uma estrutura de repetição (While)
#5-Colocar o contador dentro do (While) para fazer uma verificação se o número do contador for menor que o estipulado.
#6-Contador = Contador + 1 
#7-Pegar a primeira variavel e multiplicar até o número desejado
#8-Mostrar oque foi feito com (Print)

n1 = int(input('Digite a tabuada do: '))
n2 = int(input('Digite o valor maxímo da tabuada: '))

count = -1

while count < n2 :
    count = count + 1 
    mult = n1 * count 
    print('{} X {} = {}'.format(n1, count, mult))