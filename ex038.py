print('Programa para verificar se o o valor 1 é maior ou menor que o valor 2')
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print('O Primeiro Valor ({}) é MAIOR que o Segundo Valor ({})'.format(num1,num2))
elif num1 < num2:
    print('O Primeiro Valor({}) é MENOR que o Segundo Valor ({})'.format(num1,num2))
elif num1 == num2:
    print('O Primeiro valor ({}) é IGUAL ao Segundo Valor ({})'.format(num1,num2))


