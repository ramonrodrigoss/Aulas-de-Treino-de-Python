print('-=' * 10)
print('Gerador de P.A. V2.0')
print('-=' * 10)

num=int(input('Primeiro termo: '))
razão=int(input('Razão da P.A.: '))

c=1
while c <= 10:
    print(num,end=' -> ')
    num += razão
    c +=1
print('FIM')