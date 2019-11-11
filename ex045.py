import random
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

print('Jogo de JOKENPO')
jogador = int(input("""Escolha sua jogada:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é sua jogada?
"""))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(0.5)

computador = random.randint(0,2)
print('-=' * 11)
print('O Jogador jogou {}'.format(itens[jogador]))
print('O Computador escolheu {}'.format(itens[computador]))
print(('-=' * 11))

if computador == 0: #Computador escolheu PEDRA
    if jogador == 0: # Jogador escolheu PEDRA
        print('EMPATE')
    elif jogador == 1: # jogador escolheu PAPEL
        print('JOGADOR VENCEU')
    elif jogador == 2: #Jogador escolheu TESOURA
        print('COMPUTADOR VENCEU')
    else:
        print('Jogada Invalida')
if computador == 1: #Computador escolheu PAPEL
    if jogador == 0: #pedra
        print('COMPUTADOR VENCEU')
    elif jogador == 1: # papel
        print('EMPATE')
    elif jogador == 2: # tesoura
        print("JOGADOR VENCEU VENCEU")
    else:
        print('Jogada Invalida')
if computador == 2: #Computador escolheu TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Invalida')