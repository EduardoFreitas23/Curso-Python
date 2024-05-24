res = float(input('Quantos reais você tem: '))

dolar = 4.95
dolarC = res / dolar
reais = res * dolar

print('Cotação do dolar: {}'.format(dolar))
print('Com US$ {} dolares você teria: R$ {}'.format(res,reais))
print('Com R$ {} reais você teria US$ {:.2f}'.format(res,dolarC))