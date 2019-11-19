import math
print('Calculo do Fatorial')
num=int(input('Digite um número para calcular o seu Fatorial: '))
fat = math.factorial(num)
while num > 0:
    print('{}'.format(num), end='')
    print(' x ' if num > 1 else ' = ', end='')
    num -=1
print (fat)