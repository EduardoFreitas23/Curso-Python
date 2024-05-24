# horas = int(input('Me informe qualquer hora: '))

# if horas >= 00 and horas <= 12:
#     print('Bom dia!')
# elif horas >= 12 and horas <= 18:
#     print('Boa Tarde!')
# elif horas >= 18 and horas <= 24:
#     print('Boa Noite!')
# else:
#     print('Hora Inválida')

# horas_str = input('Me informe qualquer hora: ')

# if horas_str.isdigit():
#     horas = int(horas_str)
#     if horas >= 0 and horas <= 12:
#         print('Bom dia!')
#     elif horas > 12 and horas <= 18:
#         print('Boa Tarde!')
#     elif horas > 18 and horas <= 24:
#         print('Boa Noite!')
#     else:
#         print('Hora Inválida')
# else:
#     print('Por favor, insira apenas números.')

# while True:
#     horas_str = input('Me informe qualquer hora (ou "s" para sair): ')

#     if horas_str.lower() == 's':
#         print('Saindo...')
#         break

#     if horas_str.isdigit():
#         horas = int(horas_str)
#         if horas >= 0 and horas <= 12:
#             print('Bom dia!')
#         elif horas > 12 and horas <= 18:
#             print('Boa Tarde!')
#         elif horas > 18 and horas <= 24:
#             print('Boa Noite!')
#         else:
#             print('Hora Inválida')
#     else:
#         print('Por favor, insira apenas números.')

# massa = float(input('Informe seu peso em (KG): '))

# altura = float(input('Informe sua altura em (M): '))

# imc = massa / (altura * altura)

# print('O seu IMC é: {:.2f}'.format(imc))

# if imc >= 18.5 and imc <= 25:
#     print('Você está no peso ideal!')
# else:
#     print('Você está fora do peso ideal!')
    

# ano = int(input('Em que ano você está: '))
# nasc = int(input('Em que ano você nasceu? '))

# idade = ano - nasc

# if idade >= 18:
#     print('Você pode tirar a carteira para dirigir!! :)')
# else:
#     print('Você não pode dirigir ainda!! :( F')

primeiraNota = (float(input('Qual sua primeira nota: ')))
segundaNota = (float(input('Qual sua segunda nota: ')))

media = float((primeiraNota + segundaNota) / 2)

if media >= 9 and media <= 10:
    print('A sua média é: {}'.format(media))
    print('---------------------------------')
    print('APROVEITAMENTO A')
elif media >= 8 and media <= 8.9:
    print('A sua média é: {}'.format(media))
    print('---------------------------------')
    print('APROVEITAMENTO B')
elif media >= 7 and media <= 7.9:
    print('A sua média é: {}'.format(media))
    print('---------------------------------')
    print('APROVEITAMENTO C')
elif media >= 6 and media <= 6.9:
    print('A sua média é: {}'.format(media))
    print('---------------------------------')
    print('APROVEITAMENTO D')
elif media >= 5 and media <= 5.9:
    print('A sua média é: {}'.format(media))
    print('---------------------------------')
    print('APROVEITAMENTO E')
else:
    print('A sua média é: {}'.format(media)) 
    print('---------------------------------')
    print('APROVEITAMENTO F')