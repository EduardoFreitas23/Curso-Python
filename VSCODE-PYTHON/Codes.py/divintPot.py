n1 = int(input('Um número: '))
n2 = int(input('Outro número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é: {} a multiplicação é: {} a divisão é: {}'.format(s, m, d), end='-')
print('A divisão inteira é: {} a potência é: {}'.format(di, e))