print('-=' * 10)
print('Gerador de P.A. V3.0')
print('-=' * 10)

termo = int(input('Primeiro termo: '))
razão = int(input('Razão da P.A.: '))

c=1
total=0
mais = 10

while mais != 0:
    total += mais
    while c <= total:
        print(termo,end=' -> ')
        termo += razão
        c +=1
    print('PAUSA')
    mais=int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizaca com {} termos mostrados'.format(total))
print('FIM')