import math

me = int(input('Me fala um ângulo: '))

ra = math.radians(me)

coss = math.cos(ra)
se = math.sin(ra)
ta = math.tan(ra)

print('O cosseno é: {:.2f}'.format(coss))
print('O seno é: {:.2f}'.format(se))
print('A tangente é: {:.2f}'.format(ta))