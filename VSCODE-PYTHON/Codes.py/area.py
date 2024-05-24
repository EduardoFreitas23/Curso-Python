paredeT = float(input('Qual tamanho da sua parede em METROS: '))
paredeC = float(input('Qual comprimento da sua parede em METROS: '))

area = paredeC * paredeT
tinta = area / 2

print('A cada litro de tinta pinta uma área de 2m².')
print('A área da sua parede é: {:.2f}m²'.format(area))
print('Em uma parede de {:.2f}m², será necessário {:.2f} litros de tinta para pintar.'.format(area, tinta))