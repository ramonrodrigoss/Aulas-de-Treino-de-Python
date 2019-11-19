print('Numeros Primos')
primo = int(input('Digite um número: '))
count = 0
for c in range(1,primo+1,1):
    if primo%c == 0:
    ##cor amarelo se for
        print('\033[33m'+'{}'.format(c),end=' ')
        count+=1

    else:
    ##cor vermelho se nao for
        print('\033[31m'+'{}'.format(c),end=' ')


print(' ')
print('\033[37m'+'O Numero {} foi divisivel {} vezes'.format(primo,count))
if count == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO')







