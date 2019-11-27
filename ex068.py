import random
computador = vitoria = soma = 0
print('VAMOS JOGAR PAR OU ÍMPAR!')
while True:
    jogador = int(input('Diga um valor: '))
    poi = str(input('Par ou Ímpar? [P/I]')).lower().strip()[0]
    while poi not in 'pi':
        poi=input('Opção invalida, por favor, digite novamente sua escolha [ P / I ]').lower().strip()[0]

    computador = random.randrange(0,10)
    soma = jogador + computador

    if soma % 2 == 0:
        print(f'Você escolheu {jogador} e o computador escolheu {computador}. TOTAL de {soma} e deu PAR')
        if poi in 'p':
            print('VOCE VENCEU')
            vitoria += 1
        else:
            print('VOCE PERDEU')
            break
    else:
        print((f'Voce escolheu {jogador} e o computador escolheu {computador}. TOTAL DE {soma} e deu IMPAR'))
        if poi in 'i':
            print('VOCE VENCEU')
            vitoria += 1
        else:
            print('VOCE PERDEU')
            break
print(f'GAME OVER! Você venceu {vitoria} vezes.')