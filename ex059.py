from time import sleep
num1=int(input('Digite o Primeiro Valor: '))
num2=int(input('Digite o Segundo Valor'))
opção=0
while opção != 5:
    print('''---- Escolha a Opção -----
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR \n'''+'------'*4)
    print('Lembrando, seu valor PRIMEIRO é [{}] e SEGUNDO é [{}]'.format(num1,num2))
    opção=int(input('Digite sua Opção:'))
    if opção == 1:
        somar = num1+num2
        print('A SOMA de {} e {} é {}'.format(num1,num2,somar))
        sleep(2)
    elif opção == 2:
        multiplicar = num1*num2
        print('A MULTIPLICAÇÃO DE {} e {} é {}'.format(num1,num2,multiplicar))
        sleep(2)
    elif opção == 3:
        if num1 > num2:
            print('O {} É MAIOR QUE {}'.format(num1,num2))
            sleep(2)
        elif num1 < num2:
            print('O {} É MENOR QUE {}'.format(num1,num2))
            sleep(2)
        else:
            print('O {} É IGUAL A {}'.format(num1,num2))
            sleep(2)
    elif opção ==4:
        num1=int(input('Digite o NOVO VALOR do PRIMEIRO: '))
        num2=int(input('Digite o NOVO VALOR do SEGUNDO: '))
        sleep(2)
    else:
        print('Opção INVALIDA, Por favor, digite outra Opção: ')
        sleep(2)
print('FIM DO PROGRAMA')