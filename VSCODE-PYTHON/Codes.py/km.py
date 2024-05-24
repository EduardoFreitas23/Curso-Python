dias = float(input('Quantos dias alugado: '))
km = float(input('Quantos km ele andou: '))

c = dias * 60 
s = km * 0.15 

res = c + s

print('O total a pagar é R$: {:.2f}'.format(res))