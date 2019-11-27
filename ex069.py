maior = homem = mulher = 0
while True:
    print('Cadastro de Pessoas')
    idade = int(input('Idade:  '))
    if idade >= 18:
        maior+=1
    sexo = str(input('Sexo: ')).strip().lower()[0]
    while sexo not in 'mf':
        sexo = str(input('Sexo Invalido, por favor [M / F]')).strip().lower()[0]
    if idade < 20 and sexo in 'f':
        mulher += 1
    if sexo in 'm':
        homem += 1
    escolha=input('Deseja Continuar? [S/N]').strip().lower()[0]
    while escolha not in 'sn':
        escolha=input('Valor Invalido, Digite [S/N]: ')
    if escolha in 'n':
        break
print(f'Total de Pessoas com mais de 18 anos: {maior}')
print(f'Ao todo, temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')

