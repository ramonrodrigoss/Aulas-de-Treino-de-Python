nome = str(input('Digite seu nome: ').strip().lower())
print('A letra A aparece {} vezes em seu nome'.format(nome.count('a')))
print('A letra A aparece a primeira vez na {} posição !'.format(nome.find('a')+1))
print('a Letra A aparece por ultimo na {} posição !'.format(nome.rfind('a')+1))