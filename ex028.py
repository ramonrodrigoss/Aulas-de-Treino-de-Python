import random
num = int(input('Digite um numero de 0 a 5\n'))
num1 = random.randrange(1,5)
if num == num1:
    print('Voce acertou, o numero é {} !'.format(num1))
else:
    print('Voce errou, melhor sorte na proxima, o numero escolhido era {}'.format(num1))
