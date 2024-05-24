algo = input('Digite algo: ')

print('O tipo primitivo desse valor é:', type(algo))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É um número? {}'.format(algo.isdigit()))
print('É alfabetico? {}'.format(algo.isalpha()))
print('É alfanumérico? {}'.format(algo.isalnum()))
print('Está em letras Maiúsculas? {}'.format(algo.isupper()))
print('Está em letras Minúsculas? {}'.format(algo.islower()))
print('Está capitalizada? {}'.format(algo.isupper() or algo.islower()))

'''
Claro, aqui está uma explicação de cada método is usado em seu código:

algo.isspace(): Este método retorna True se todos os caracteres na string algo são espaços em branco, como espaços, tabs (\t), quebras de linha (\n), etc.

algo.isdigit(): Este método retorna True se todos os caracteres na string algo são dígitos numéricos (0-9). Se a string estiver vazia, também retorna False.

algo.isalpha(): Retorna True se todos os caracteres na string algo forem letras do alfabeto (a-z, A-Z).

algo.isalnum(): Retorna True se todos os caracteres na string algo forem alfanuméricos (letras do alfabeto e números). Se a string estiver vazia, também retorna False.

algo.isupper(): Retorna True se todos os caracteres na string algo forem letras maiúsculas.

algo.islower(): Retorna True se todos os caracteres na string algo forem letras minúsculas.

algo.isupper() or algo.islower(): Este último é uma expressão que retorna True se a string algo estiver completamente em letras maiúsculas ou minúsculas. Se houver uma combinação de maiúsculas e minúsculas, retornará False.algo = input('Digite algo: ')
'''