c = contador = resultado = 0
c = int(input('Digite um número [999 para parar]'))
while c != 999:
    resultado+=c
    contador+=1
    c=int(input('Digite um número [999 para parar]'))

print('Você digitou {} números e a soma entre eles foi {}'.format(contador,resultado))

