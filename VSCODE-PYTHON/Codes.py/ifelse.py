digito = input('Digite algo: ')

isalnum = digito.isalnum()
if isalnum == True :
    validacao = 'Verdadeiro, ele é alfanumérico!'
elif isalnum == False :
    validacao = 'Falso, ele não é alfanumérico!'

print('O digito é: {}. Resultado: {}'.format(digito, validacao))

#linha separadas----------------

digito = input('Digite algo: ')

isalnum = digito.isalnum()

if isalnum == True :
    validacao = 'Verdadeiro, ele é alfanumérico!'
elif isalnum == False :
    validacao = 'Falso, ele não é alfanumérico!'

print('O digito é: {}.'.format(digito))
print('Resultado: {}'.format(validacao))

# valor1 = int(input('Me Informe um número: '))
# valor2 = int(input('Me Informe um número: '))
# valor3 = int(input('Me Informe um número: '))

# if valor1 > valor2 and valor1 > valor3:
#     print('Este é o maior número dos três: {}'.format(valor1))
# elif valor2 > valor3 and valor2 > valor3:
#     print('Este é o maior número dos três: {}'.format(valor2))
# elif valor3 > valor1 and valor3 > valor2:
#     print('Este é o maior número dos três: {}'.format(valor3))

# valor1 = int(input('Me Informe um número: '))
# valor2 = int(input('Me Informe um número: '))
# valor3 = int(input('Me Informe um número: '))

# if valor1 > valor2 and valor1 > valor3:
#     print('Esse número é o maior: {}'.format(valor1))
# elif valor2 > valor3:
#     print('Esse número é o maior: {}'.format(valor2))
# else:
#     print('Esse número é o maior: {}'.format(valor3))

horas = int(input('Me informe qualquer hora: '))

if horas >= 00 and horas <= 12:
    print('Bom dia!')
elif horas >= 12 and horas <= 18:
    print('Boa Tarde!')
elif horas >= 18 and horas <= 24:
    print('Boa Noite!')
else:
    print('Hora Inválida')
