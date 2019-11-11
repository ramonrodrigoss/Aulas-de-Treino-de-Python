print('Programa para calculcar o IMC')
peso = float(input('Digite o seu Peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura*altura)

print('O seu IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Você está no Peso Ideal')
elif 25 <= imc < 30:
    print('Você está com Sobrepeso')
elif 30 <= imc < 40:
    print('Você está com Obesidade')
elif imc >= 40 :
    print('Você está com Obesidade Mórbida')