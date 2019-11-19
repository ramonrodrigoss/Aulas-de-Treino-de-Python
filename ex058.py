import random
num=int(input('''Sou Seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?
Qual é seu palpite? '''))
maquina = int(random.randint(0,10))
contador = 1
while num != maquina:
    if num > maquina:
        num = int(input('Menos... Tente mais uma vez. '))
        contador += 1
    elif num < maquina:
        num = int(input('Mais... Tente mais uma vez. '))
        contador += 1
print('Acertou! voce usou {} tentativas'.format(contador))
print('O numero que a maquina escolheu foi {}'.format(maquina))
