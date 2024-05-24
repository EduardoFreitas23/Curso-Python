import math
c1 = float(input('Digite o comprimento do cateto: '))
c2 = float(input('Digite o comprimento do outro: '))

h = (c1**2 + c2**2)
print('O comprimento da hipotenusa é: {:.2f}'.format(math.sqrt(h)))