sexo = str(input('Informe seu Sexo: [M/F]').strip().upper())[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo:'))
print('Sexo {} registrado com sucesso'.format(sexo).upper())