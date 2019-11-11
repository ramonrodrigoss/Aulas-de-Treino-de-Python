#Programa para calcular o aumento do salario
print ('Programa para Calcular um aumento de salario!')
sal = float(input('Digite seu Salário para calcular o seu aumento: \n'))
if sal > 1250.00:
    print('Seu salário de R${} vai ganhar um aumento de 10%, ficando R${}'.format(sal,sal+((sal/100)*10)))
if sal <= 1250.00:
    print('Seu salário de R${} terá um aumento de 15%, ficando R${}!'.format(sal,sal+((sal/100)*15)))